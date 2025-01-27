# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/Common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)pyatv/protocols/mrp/protobuf/Common.proto\"<\n\nRepeatMode\".\n\x04\x45num\x12\x0b\n\x07Unknown\x10\x00\x12\x07\n\x03Off\x10\x01\x12\x07\n\x03One\x10\x02\x12\x07\n\x03\x41ll\x10\x03\"B\n\x0bShuffleMode\"3\n\x04\x45num\x12\x0b\n\x07Unknown\x10\x00\x12\x07\n\x03Off\x10\x01\x12\n\n\x06\x41lbums\x10\x02\x12\t\n\x05Songs\x10\x03\"\x89\x01\n\x0b\x44\x65viceClass\"z\n\x04\x45num\x12\x0b\n\x07Invalid\x10\x00\x12\n\n\x06iPhone\x10\x01\x12\x08\n\x04iPod\x10\x02\x12\x08\n\x04iPad\x10\x03\x12\x0b\n\x07\x41ppleTV\x10\x04\x12\t\n\x05iFPGA\x10\x05\x12\t\n\x05Watch\x10\x06\x12\r\n\tAccessory\x10\x07\x12\n\n\x06\x42ridge\x10\x08\x12\x07\n\x03Mac\x10\t\"b\n\nDeviceType\"T\n\x04\x45num\x12\x0b\n\x07Unknown\x10\x00\x12\x0b\n\x07\x41irPlay\x10\x01\x12\r\n\tBluetooth\x10\x02\x12\x0b\n\x07\x43\x61rPlay\x10\x03\x12\x0b\n\x07\x42uiltIn\x10\x04\x12\t\n\x05Wired\x10\x05\"\x80\x02\n\rDeviceSubType\"\xee\x01\n\x04\x45num\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x0b\n\x07Speaker\x10\x01\x12\x0e\n\nHeadphones\x10\x02\x12\x0b\n\x07Headset\x10\x03\x12\x0c\n\x08Receiver\x10\x04\x12\x0b\n\x07LineOut\x10\x05\x12\x07\n\x03USB\x10\x06\x12\x0f\n\x0b\x44isplayPort\x10\x07\x12\x08\n\x04HDMI\x10\x08\x12\r\n\tLowEnergy\x10\t\x12\t\n\x05SPDIF\x10\n\x12\x06\n\x02TV\x10\x0b\x12\x0b\n\x07HomePod\x10\x0c\x12\x0b\n\x07\x41ppleTV\x10\r\x12\x0b\n\x07Vehicle\x10\x0e\x12\x0b\n\x07\x43luster\x10\x0f\x12\r\n\tSetTopBox\x10\x10\x12\x0b\n\x07TVStick\x10\x11\"h\n\rPlaybackState\"W\n\x04\x45num\x12\x0b\n\x07Unknown\x10\x00\x12\x0b\n\x07Playing\x10\x01\x12\n\n\x06Paused\x10\x02\x12\x0b\n\x07Stopped\x10\x03\x12\x0f\n\x0bInterrupted\x10\x04\x12\x0b\n\x07Seeking\x10\x05')



_REPEATMODE = DESCRIPTOR.message_types_by_name['RepeatMode']
_SHUFFLEMODE = DESCRIPTOR.message_types_by_name['ShuffleMode']
_DEVICECLASS = DESCRIPTOR.message_types_by_name['DeviceClass']
_DEVICETYPE = DESCRIPTOR.message_types_by_name['DeviceType']
_DEVICESUBTYPE = DESCRIPTOR.message_types_by_name['DeviceSubType']
_PLAYBACKSTATE = DESCRIPTOR.message_types_by_name['PlaybackState']
_REPEATMODE_ENUM = _REPEATMODE.enum_types_by_name['Enum']
_SHUFFLEMODE_ENUM = _SHUFFLEMODE.enum_types_by_name['Enum']
_DEVICECLASS_ENUM = _DEVICECLASS.enum_types_by_name['Enum']
_DEVICETYPE_ENUM = _DEVICETYPE.enum_types_by_name['Enum']
_DEVICESUBTYPE_ENUM = _DEVICESUBTYPE.enum_types_by_name['Enum']
_PLAYBACKSTATE_ENUM = _PLAYBACKSTATE.enum_types_by_name['Enum']
RepeatMode = _reflection.GeneratedProtocolMessageType('RepeatMode', (_message.Message,), {
  'DESCRIPTOR' : _REPEATMODE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Common_pb2'
  # @@protoc_insertion_point(class_scope:RepeatMode)
  })
_sym_db.RegisterMessage(RepeatMode)

ShuffleMode = _reflection.GeneratedProtocolMessageType('ShuffleMode', (_message.Message,), {
  'DESCRIPTOR' : _SHUFFLEMODE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Common_pb2'
  # @@protoc_insertion_point(class_scope:ShuffleMode)
  })
_sym_db.RegisterMessage(ShuffleMode)

DeviceClass = _reflection.GeneratedProtocolMessageType('DeviceClass', (_message.Message,), {
  'DESCRIPTOR' : _DEVICECLASS,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Common_pb2'
  # @@protoc_insertion_point(class_scope:DeviceClass)
  })
_sym_db.RegisterMessage(DeviceClass)

DeviceType = _reflection.GeneratedProtocolMessageType('DeviceType', (_message.Message,), {
  'DESCRIPTOR' : _DEVICETYPE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Common_pb2'
  # @@protoc_insertion_point(class_scope:DeviceType)
  })
_sym_db.RegisterMessage(DeviceType)

DeviceSubType = _reflection.GeneratedProtocolMessageType('DeviceSubType', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESUBTYPE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Common_pb2'
  # @@protoc_insertion_point(class_scope:DeviceSubType)
  })
_sym_db.RegisterMessage(DeviceSubType)

PlaybackState = _reflection.GeneratedProtocolMessageType('PlaybackState', (_message.Message,), {
  'DESCRIPTOR' : _PLAYBACKSTATE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Common_pb2'
  # @@protoc_insertion_point(class_scope:PlaybackState)
  })
_sym_db.RegisterMessage(PlaybackState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPEATMODE._serialized_start=45
  _REPEATMODE._serialized_end=105
  _REPEATMODE_ENUM._serialized_start=59
  _REPEATMODE_ENUM._serialized_end=105
  _SHUFFLEMODE._serialized_start=107
  _SHUFFLEMODE._serialized_end=173
  _SHUFFLEMODE_ENUM._serialized_start=122
  _SHUFFLEMODE_ENUM._serialized_end=173
  _DEVICECLASS._serialized_start=176
  _DEVICECLASS._serialized_end=313
  _DEVICECLASS_ENUM._serialized_start=191
  _DEVICECLASS_ENUM._serialized_end=313
  _DEVICETYPE._serialized_start=315
  _DEVICETYPE._serialized_end=413
  _DEVICETYPE_ENUM._serialized_start=329
  _DEVICETYPE_ENUM._serialized_end=413
  _DEVICESUBTYPE._serialized_start=416
  _DEVICESUBTYPE._serialized_end=672
  _DEVICESUBTYPE_ENUM._serialized_start=434
  _DEVICESUBTYPE_ENUM._serialized_end=672
  _PLAYBACKSTATE._serialized_start=674
  _PLAYBACKSTATE._serialized_end=778
  _PLAYBACKSTATE_ENUM._serialized_start=691
  _PLAYBACKSTATE_ENUM._serialized_end=778
# @@protoc_insertion_point(module_scope)
