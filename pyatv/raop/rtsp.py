"""Implementation of the RTSP protocol."""
import asyncio
import logging
import plistlib
from random import randrange
from typing import Dict, Mapping, Optional, Tuple, Union

from pyatv.dmap import tags
from pyatv.raop import timing
from pyatv.raop.metadata import AudioMetadata
from pyatv.support.http import HttpConnection, HttpResponse

_LOGGER = logging.getLogger(__name__)

FRAMES_PER_PACKET = 352
USER_AGENT = "AirPlay/540.31"

ANNOUNCE_PAYLOAD = (
    "v=0\r\n"
    + "o=iTunes {session_id} 0 IN IP4 {local_ip}\r\n"
    + "s=iTunes\r\n"
    + "c=IN IP4 {remote_ip}\r\n"
    + "t=0 0\r\n"
    + "m=audio 0 RTP/AVP 96\r\n"
    + "a=rtpmap:96 AppleLossless\r\n"
    + f"a=fmtp:96 {FRAMES_PER_PACKET} 0 "
    + "{bits_per_channel} 40 10 14 {channels} 255 0 0 {sample_rate}\r\n"
)

# Used to signal that traffic is to be unencrypted
AUTH_SETUP_UNENCRYPTED = b"\x01"

# Just a static Curve25519 public key used to satisfy the auth-setup step for devices
# requiring that (e.g. AirPort Express). We never verify anything. Source:
# https://github.com/owntone/owntone-server/blob/
# c1db4d914f5cd8e7dbe6c1b6478d68a4c14824af/src/outputs/raop.c#L276
CURVE25519_PUB_KEY = (
    b"\x59\x02\xed\xe9\x0d\x4e\xf2\xbd"
    b"\x4c\xb6\x8a\x63\x30\x03\x82\x07"
    b"\xa9\x4d\xbd\x50\xd8\xaa\x46\x5b"
    b"\x5d\x8c\x01\x2a\x0c\x7e\x1d\x4e"
)


class RtspContext:
    """Data used for one RTSP session.

    This class holds a bit too much information, should be
    restructured a bit.
    """

    def __init__(self) -> None:
        """Initialize a new RtspContext."""
        self.sample_rate: int = 44100
        self.channels: int = 2
        self.bytes_per_channel: int = 2
        self.latency = 22050 + self.sample_rate

        self.rtpseq: int = 0
        self.start_ts = 0
        self.head_ts = 0

        self.server_port: int = 0
        self.control_port: int = 0
        self.timing_port: int = 0
        self.rtsp_session: int = 0

        # TODO: Not entirely sure about the ranges for these
        self.session_id: int = randrange(2 ** 32)
        self.dacp_id: str = f"{randrange(2 ** 64):X}"
        self.active_remote: int = randrange(2 ** 32)

        self.volume: Optional[float] = None

    def reset(self) -> None:
        """Reset seasion.

        Must be done when sample rate changes.
        """
        self.rtpseq = randrange(2 ** 16)
        self.start_ts = timing.ntp2ts(timing.ntp_now(), self.sample_rate)
        self.head_ts = self.start_ts
        self.latency = 22050 + self.sample_rate

    @property
    def rtptime(self) -> int:
        """Current RTP time with latency."""
        return self.head_ts - (self.start_ts - self.latency)

    @property
    def position(self) -> float:
        """Current position in stream (seconds with fraction)."""
        # Do not consider latency here (so do not use rtptime)
        return timing.ts2ms(self.head_ts - self.start_ts, self.sample_rate) / 1000.0


class RtspSession:
    """Representation of an RTSP session."""

    def __init__(self, connection: HttpConnection, context: RtspContext) -> None:
        """Initialize a new RtspSession."""
        super().__init__()
        self.connection = connection
        self.context = context
        self.requests: Dict[int, Tuple[asyncio.Event, Optional[HttpResponse]]] = {}
        self.cseq = 0

    @property
    def uri(self) -> str:
        """Return URI used for session requests."""
        return f"rtsp://{self.connection.local_ip}/{self.context.session_id}"

    @staticmethod
    def error_received(exc) -> None:
        """Handle a connection error."""
        _LOGGER.error("Error received: %s", exc)

    async def info(self) -> Dict[str, object]:
        """Return device information."""
        device_info = await self.exchange("GET", "/info", allow_error=True)

        # If not supported, just return an empty dict
        if device_info.code != 200:
            _LOGGER.debug("Device does not support /info")
            return {}

        body = (
            device_info.body
            if isinstance(device_info.body, bytes)
            else device_info.body.encode("utf-8")
        )
        return plistlib.loads(body)

    async def auth_setup(self) -> HttpResponse:
        """Send auth-setup message."""
        # Payload to say that we want to proceed unencrypted
        body = AUTH_SETUP_UNENCRYPTED + CURVE25519_PUB_KEY

        return await self.exchange(
            "POST",
            "/auth-setup",
            content_type="application/octet-stream",
            body=body,
        )

    async def announce(self) -> HttpResponse:
        """Send ANNOUNCE message."""
        body = ANNOUNCE_PAYLOAD.format(
            session_id=self.context.session_id,
            local_ip=self.connection.local_ip,
            remote_ip=self.connection.remote_ip,
            bits_per_channel=8 * self.context.bytes_per_channel,
            channels=self.context.channels,
            sample_rate=self.context.sample_rate,
        )
        return await self.exchange(
            "ANNOUNCE",
            content_type="application/sdp",
            body=body,
        )

    async def setup(self, control_port: int, timing_port: int) -> HttpResponse:
        """Send SETUP message."""
        return await self.exchange(
            "SETUP",
            headers={
                "Transport": "RTP/AVP/UDP;unicast;interleaved=0-1;mode=record;"
                + f"control_port={control_port};timing_port={timing_port}",
            },
        )

    async def record(self, rtpseq: int, rtptime: int) -> HttpResponse:
        """Send RECORD message."""
        return await self.exchange(
            "RECORD",
            headers={
                "Range": "npt=0-",
                "Session": self.context.rtsp_session,
                "RTP-Info": f"seq={rtpseq};rtptime={rtptime}",
            },
        )

    async def set_parameter(self, parameter: str, value: str) -> HttpResponse:
        """Send SET_PARAMETER message."""
        return await self.exchange(
            "SET_PARAMETER",
            content_type="text/parameters",
            body=f"{parameter}: {value}",
        )

    async def set_metadata(
        self,
        rtpseq: int,
        rtptime: int,
        metadata: AudioMetadata,
    ) -> HttpResponse:
        """Change metadata for what is playing."""
        payload = b""
        if metadata.title:
            payload += tags.string_tag("minm", metadata.title)
        if metadata.album:
            payload += tags.string_tag("asal", metadata.album)
        if metadata.artist:
            payload += tags.string_tag("asar", metadata.artist)

        return await self.exchange(
            "SET_PARAMETER",
            content_type="application/x-dmap-tagged",
            headers={
                "Session": self.context.rtsp_session,
                "RTP-Info": f"seq={rtpseq};rtptime={rtptime}",
            },
            body=tags.container_tag("mlit", payload),
        )

    async def feedback(self, allow_error=False) -> HttpResponse:
        """Send SET_PARAMETER message."""
        return await self.exchange("POST", uri="/feedback", allow_error=allow_error)

    async def teardown(self, allow_error=False) -> HttpResponse:
        """Send TEARDOWN message."""
        return await self.exchange(
            "TEARDOWN", headers={"Session": self.context.rtsp_session}
        )

    async def exchange(
        self,
        method: str,
        uri: Optional[str] = None,
        content_type: Optional[str] = None,
        headers: Mapping[str, object] = None,
        body: Union[str, bytes] = None,
        allow_error: bool = False,
    ) -> HttpResponse:
        """Send a RTSP message and return response."""
        cseq = self.cseq
        self.cseq += 1

        hdrs = {
            "CSeq": cseq,
            "DACP-ID": self.context.dacp_id,
            "Active-Remote": self.context.active_remote,
            "Client-Instance": self.context.dacp_id,
        }
        if headers:
            hdrs.update(headers)

        # Map an asyncio Event to current CSeq and make the request
        self.requests[cseq] = (asyncio.Event(), None)
        resp = await self.connection.send_and_receive(
            method,
            uri or self.uri,
            protocol="RTSP/1.0",
            user_agent=USER_AGENT,
            content_type=content_type,
            headers=hdrs,
            body=body,
            allow_error=allow_error,
        )

        # The response most likely contains a CSeq and it is also very likely to be
        # the one we expect, but it could be for someone else. So set the correct event
        # and save response.
        resp_cseq = int(resp.headers.get("CSeq", "-1"))
        if resp_cseq in self.requests:
            # Insert response for correct CSeq and activate event
            event, _ = self.requests[resp_cseq]
            self.requests[resp_cseq] = (event, resp)
            event.set()

        # Wait for response to the CSeq we expect
        try:
            await asyncio.wait_for(self.requests[cseq][0].wait(), 4)
            response = self.requests[cseq][1]
        except asyncio.TimeoutError as ex:
            raise TimeoutError(
                f"no response to CSeq {cseq} ({uri or self.uri})"
            ) from ex
        finally:
            del self.requests[cseq]

        # Programming error: forgot to store response before activating event
        if response is None:
            raise RuntimeError(f"no response was saved for {cseq}")

        return response
