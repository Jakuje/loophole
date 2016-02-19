# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sport.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import structures_pb2
import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sport.proto',
  package='data',
  serialized_pb=_b('\n\x0bsport.proto\x12\x04\x64\x61ta\x1a\x10structures.proto\x1a\x0btypes.proto\"M\n\x12PbSportTranslation\x12\x19\n\x02id\x18\x01 \x02(\x0b\x32\r.PbLanguageId\x12\x1c\n\x04text\x18\x02 \x02(\x0b\x32\x0e.PbOneLineText\"\x81\x04\n\x07PbSport\x12&\n\nidentifier\x18\x01 \x02(\x0b\x32\x12.PbSportIdentifier\x12-\n\x11parent_identifier\x18\x02 \x02(\x0b\x32\x12.PbSportIdentifier\x12-\n\x0btranslation\x18\x03 \x03(\x0b\x32\x18.data.PbSportTranslation\x12\x0e\n\x06\x66\x61\x63tor\x18\x04 \x01(\x02\x12\"\n\x06stages\x18\x05 \x03(\x0b\x32\x12.PbSportIdentifier\x12\x46\n\nsport_type\x18\x06 \x01(\x0e\x32\x19.data.PbSport.PbSportType:\x17SPORT_TYPE_SINGLE_SPORT\x12\"\n\x13speed_zones_enabled\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\"\n\x07\x63reated\x18\x64 \x01(\x0b\x32\x11.PbSystemDateTime\x12(\n\rlast_modified\x18\x65 \x01(\x0b\x32\x11.PbSystemDateTime\"\x81\x01\n\x0bPbSportType\x12\x1b\n\x17SPORT_TYPE_SINGLE_SPORT\x10\x01\x12\x1a\n\x16SPORT_TYPE_MULTI_SPORT\x10\x02\x12\x18\n\x14SPORT_TYPE_SUB_SPORT\x10\x03\x12\x1f\n\x1bSPORT_TYPE_FREE_MULTI_SPORT\x10\x04')
  ,
  dependencies=[structures_pb2.DESCRIPTOR,types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PBSPORT_PBSPORTTYPE = _descriptor.EnumDescriptor(
  name='PbSportType',
  full_name='data.PbSport.PbSportType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPORT_TYPE_SINGLE_SPORT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TYPE_MULTI_SPORT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TYPE_SUB_SPORT', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPORT_TYPE_FREE_MULTI_SPORT', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=516,
  serialized_end=645,
)
_sym_db.RegisterEnumDescriptor(_PBSPORT_PBSPORTTYPE)


_PBSPORTTRANSLATION = _descriptor.Descriptor(
  name='PbSportTranslation',
  full_name='data.PbSportTranslation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='data.PbSportTranslation.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='data.PbSportTranslation.text', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=129,
)


_PBSPORT = _descriptor.Descriptor(
  name='PbSport',
  full_name='data.PbSport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='data.PbSport.identifier', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_identifier', full_name='data.PbSport.parent_identifier', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translation', full_name='data.PbSport.translation', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor', full_name='data.PbSport.factor', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stages', full_name='data.PbSport.stages', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sport_type', full_name='data.PbSport.sport_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_zones_enabled', full_name='data.PbSport.speed_zones_enabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='data.PbSport.created', index=7,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='data.PbSport.last_modified', index=8,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBSPORT_PBSPORTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=645,
)

_PBSPORTTRANSLATION.fields_by_name['id'].message_type = structures_pb2._PBLANGUAGEID
_PBSPORTTRANSLATION.fields_by_name['text'].message_type = structures_pb2._PBONELINETEXT
_PBSPORT.fields_by_name['identifier'].message_type = structures_pb2._PBSPORTIDENTIFIER
_PBSPORT.fields_by_name['parent_identifier'].message_type = structures_pb2._PBSPORTIDENTIFIER
_PBSPORT.fields_by_name['translation'].message_type = _PBSPORTTRANSLATION
_PBSPORT.fields_by_name['stages'].message_type = structures_pb2._PBSPORTIDENTIFIER
_PBSPORT.fields_by_name['sport_type'].enum_type = _PBSPORT_PBSPORTTYPE
_PBSPORT.fields_by_name['created'].message_type = types_pb2._PBSYSTEMDATETIME
_PBSPORT.fields_by_name['last_modified'].message_type = types_pb2._PBSYSTEMDATETIME
_PBSPORT_PBSPORTTYPE.containing_type = _PBSPORT
DESCRIPTOR.message_types_by_name['PbSportTranslation'] = _PBSPORTTRANSLATION
DESCRIPTOR.message_types_by_name['PbSport'] = _PBSPORT

PbSportTranslation = _reflection.GeneratedProtocolMessageType('PbSportTranslation', (_message.Message,), dict(
  DESCRIPTOR = _PBSPORTTRANSLATION,
  __module__ = 'sport_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSportTranslation)
  ))
_sym_db.RegisterMessage(PbSportTranslation)

PbSport = _reflection.GeneratedProtocolMessageType('PbSport', (_message.Message,), dict(
  DESCRIPTOR = _PBSPORT,
  __module__ = 'sport_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSport)
  ))
_sym_db.RegisterMessage(PbSport)


# @@protoc_insertion_point(module_scope)