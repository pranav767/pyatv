# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/CryptoPairingMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7pyatv/protocols/mrp/protobuf/CryptoPairingMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"|\n\x14\x43ryptoPairingMessage\x12\x13\n\x0bpairingData\x18\x01 \x01(\x0c\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x12\n\nisRetrying\x18\x03 \x01(\x08\x12\x1c\n\x14isUsingSystemPairing\x18\x04 \x01(\x08\x12\r\n\x05state\x18\x05 \x01(\x05:E\n\x14\x63ryptoPairingMessage\x12\x10.ProtocolMessage\x18\' \x01(\x0b\x32\x15.CryptoPairingMessage')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.CryptoPairingMessage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(cryptoPairingMessage)

  DESCRIPTOR._options = None
  _CRYPTOPAIRINGMESSAGE._serialized_start=111
  _CRYPTOPAIRINGMESSAGE._serialized_end=235
# @@protoc_insertion_point(module_scope)
