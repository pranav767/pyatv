# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/UpdateClientMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import NowPlayingClient_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_NowPlayingClient__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6pyatv/protocols/mrp/protobuf/UpdateClientMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a\x33pyatv/protocols/mrp/protobuf/NowPlayingClient.proto\"8\n\x13UpdateClientMessage\x12!\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x11.NowPlayingClient:C\n\x13updateClientMessage\x12\x10.ProtocolMessage\x18; \x01(\x0b\x32\x14.UpdateClientMessage')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.UpdateClientMessage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(updateClientMessage)

  DESCRIPTOR._options = None
  _UPDATECLIENTMESSAGE._serialized_start=163
  _UPDATECLIENTMESSAGE._serialized_end=219
# @@protoc_insertion_point(module_scope)
