# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/GetKeyboardSessionMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<pyatv/protocols/mrp/protobuf/GetKeyboardSessionMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"\x1b\n\x19GetKeyboardSessionMessage:3\n\x19getKeyboardSessionMessage\x12\x10.ProtocolMessage\x18\x1d \x01(\t')


GETKEYBOARDSESSIONMESSAGE_FIELD_NUMBER = 29
getKeyboardSessionMessage = DESCRIPTOR.extensions_by_name['getKeyboardSessionMessage']

_GETKEYBOARDSESSIONMESSAGE = DESCRIPTOR.message_types_by_name['GetKeyboardSessionMessage']
GetKeyboardSessionMessage = _reflection.GeneratedProtocolMessageType('GetKeyboardSessionMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETKEYBOARDSESSIONMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.GetKeyboardSessionMessage_pb2'
  # @@protoc_insertion_point(class_scope:GetKeyboardSessionMessage)
  })
_sym_db.RegisterMessage(GetKeyboardSessionMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(getKeyboardSessionMessage)

  DESCRIPTOR._options = None
  _GETKEYBOARDSESSIONMESSAGE._serialized_start=116
  _GETKEYBOARDSESSIONMESSAGE._serialized_end=143
# @@protoc_insertion_point(module_scope)
