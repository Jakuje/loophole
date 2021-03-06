# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pftp_notification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pftp_notification.proto',
  package='protocol',
  serialized_pb=_b('\n\x17pftp_notification.proto\x12\x08protocol\x1a\x0btypes.proto\"P\n\x1ePbPFtpFilesystemModifiedParams\x12 \n\x06\x61\x63tion\x18\x01 \x02(\x0e\x32\x10.protocol.Action\x12\x0c\n\x04path\x18\x02 \x02(\t\"*\n\x15PbPFtpInactivityAlert\x12\x11\n\tcountdown\x18\x01 \x02(\r\"1\n\x1bPbPFtpTrainingSessionStatus\x12\x12\n\ninprogress\x18\x01 \x02(\x08\"D\n\x1aPbPFtpAutoSyncStatusParams\x12\x11\n\tsucceeded\x18\x01 \x02(\x08\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"H\n\x14PbPftpPnsDHAttribute\x12\x30\n\x04type\x18\x01 \x02(\x0e\x32\".protocol.PbPftpPnsDHAttributeType\"n\n\x1fPbPftpPnsDHNotificationResponse\x12\x17\n\x0fnotification_id\x18\x01 \x02(\r\x12\x32\n\nattributes\x18\x02 \x03(\x0b\x32\x1e.protocol.PbPftpPnsDHAttribute\"H\n\x0ePbPftpPnsState\x12\x1d\n\x15notifications_enabled\x18\x01 \x02(\x08\x12\x17\n\x0fpreview_enabled\x18\x02 \x01(\x08\">\n\x14PbPFtpStopSyncParams\x12\x11\n\tcompleted\x18\x01 \x02(\x08\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"i\n\x18PbPFtpFactoryResetParams\x12\r\n\x05sleep\x18\x01 \x02(\x08\x12!\n\x13\x64o_factory_defaults\x18\x02 \x01(\x08:\x04true\x12\x1b\n\x0cota_fwupdate\x18\x03 \x01(\x08:\x05\x66\x61lse\",\n\x19PbPFtpStartAutosyncParams\x12\x0f\n\x07timeout\x18\x01 \x02(\r\"s\n\x14PbPftpPnsHDAttribute\x12\x30\n\x04type\x18\x01 \x02(\x0e\x32\".protocol.PbPftpPnsHDAttributeType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x1b\n\x13\x61ttribute_full_size\x18\x03 \x01(\r\"\xb9\x02\n\x17PbPftpPnsHDNotification\x12\x17\n\x0fnotification_id\x18\x01 \x02(\r\x12\x34\n\x0b\x63\x61tegory_id\x18\x02 \x02(\x0e\x32\x1f.protocol.PbPftpPnsHDCategoryID\x12 \n\x06\x61\x63tion\x18\x03 \x02(\x0e\x32\x10.protocol.Action\x12$\n\nissue_time\x18\x04 \x02(\x0b\x32\x10.PbLocalDateTime\x12\'\n\x1fnew_same_category_notifications\x18\x05 \x01(\r\x12*\n\"unread_same_category_notifications\x18\x06 \x01(\r\x12\x32\n\nattributes\x18\x07 \x03(\x0b\x32\x1e.protocol.PbPftpPnsHDAttribute*\xfe\x01\n\x1bPbPFtpDevToHostNotification\x12\x17\n\x13\x46ILESYSTEM_MODIFIED\x10\x00\x12\x17\n\x13INTERNAL_TEST_EVENT\x10\x01\x12\n\n\x06IDLING\x10\x02\x12\x12\n\x0e\x42\x41TTERY_STATUS\x10\x03\x12\x14\n\x10INACTIVITY_ALERT\x10\x04\x12\x1b\n\x17TRAINING_SESSION_STATUS\x10\x05\x12\x11\n\rSYNC_REQUIRED\x10\x07\x12\x13\n\x0f\x41UTOSYNC_STATUS\x10\x08\x12 \n\x1cPNS_DH_NOTIFICATION_RESPONSE\x10\t\x12\x10\n\x0cPNS_SETTINGS\x10\n*/\n\x06\x41\x63tion\x12\x0b\n\x07\x43REATED\x10\x00\x12\x0b\n\x07UPDATED\x10\x01\x12\x0b\n\x07REMOVED\x10\x02*j\n\x18PbPftpPnsDHAttributeType\x12\x12\n\x0eUNKNOWN_ACTION\x10\x01\x12\x13\n\x0fPOSITIVE_ACTION\x10\x02\x12\x13\n\x0fNEGATIVE_ACTION\x10\x03\x12\x10\n\x0c\x43LEAR_ACTION\x10\x04*\xe1\x01\n\x1bPbPFtpHostToDevNotification\x12\x0e\n\nSTART_SYNC\x10\x00\x12\r\n\tSTOP_SYNC\x10\x01\x12\t\n\x05RESET\x10\x02\x12\x18\n\x14LOCK_PRODUCTION_DATA\x10\x03\x12\x12\n\x0eTERMINATE_SYNC\x10\x04\x12\x0e\n\nKEEP_ALIVE\x10\x05\x12\x12\n\x0eSTART_AUTOSYNC\x10\x06\x12\x17\n\x13PNS_HD_NOTIFICATION\x10\x07\x12\x16\n\x12INITIALIZE_SESSION\x10\x08\x12\x15\n\x11TERMINATE_SESSION\x10\t*\xf9\x03\n\x15PbPftpPnsHDCategoryID\x12\x15\n\x11\x43\x41TEGORY_ID_OTHER\x10\x00\x12\x15\n\x11\x43\x41TEGORY_ID_POLAR\x10\x01\x12\x1c\n\x18\x43\x41TEGORY_ID_INCOMINGCALL\x10\x02\x12\x1a\n\x16\x43\x41TEGORY_ID_MISSEDCALL\x10\x03\x12\x19\n\x15\x43\x41TEGORY_ID_VOICEMAIL\x10\x04\x12\x16\n\x12\x43\x41TEGORY_ID_SOCIAL\x10\x05\x12\x18\n\x14\x43\x41TEGORY_ID_SCHEDULE\x10\x06\x12\x15\n\x11\x43\x41TEGORY_ID_EMAIL\x10\x07\x12\x14\n\x10\x43\x41TEGORY_ID_NEWS\x10\x08\x12 \n\x1c\x43\x41TEGORY_ID_HEALTHANDFITNESS\x10\t\x12\"\n\x1e\x43\x41TEGORY_ID_BUSINESSANDFINANCE\x10\n\x12\x18\n\x14\x43\x41TEGORY_ID_LOCATION\x10\x0b\x12\x1d\n\x19\x43\x41TEGORY_ID_ENTERTAINMENT\x10\x0c\x12\x15\n\x11\x43\x41TEGORY_ID_ALARM\x10\r\x12\x15\n\x11\x43\x41TEGORY_ID_PROMO\x10\x0e\x12\x1e\n\x1a\x43\x41TEGORY_ID_RECOMMENDATION\x10\x0f\x12\x16\n\x12\x43\x41TEGORY_ID_STATUS\x10\x10\x12\x19\n\x15\x43\x41TEGORY_ID_TRANSPORT\x10\x11*\xa4\x01\n\x18PbPftpPnsHDAttributeType\x12\t\n\x05TITLE\x10\x00\x12\x0c\n\x08SUBTITLE\x10\x01\x12\x0b\n\x07MESSAGE\x10\x02\x12\x19\n\x15POSITIVE_ACTION_LABEL\x10\x03\x12\x19\n\x15NEGATIVE_ACTION_LABEL\x10\x04\x12\x14\n\x10\x41PPLICATION_NAME\x10\x05\x12\x16\n\x12\x43LEAR_ACTION_LABEL\x10\x06')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PBPFTPDEVTOHOSTNOTIFICATION = _descriptor.EnumDescriptor(
  name='PbPFtpDevToHostNotification',
  full_name='protocol.PbPFtpDevToHostNotification',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILESYSTEM_MODIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_TEST_EVENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_STATUS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INACTIVITY_ALERT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING_SESSION_STATUS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_REQUIRED', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOSYNC_STATUS', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNS_DH_NOTIFICATION_RESPONSE', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNS_SETTINGS', index=9, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1208,
  serialized_end=1462,
)
_sym_db.RegisterEnumDescriptor(_PBPFTPDEVTOHOSTNOTIFICATION)

PbPFtpDevToHostNotification = enum_type_wrapper.EnumTypeWrapper(_PBPFTPDEVTOHOSTNOTIFICATION)
_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='protocol.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1464,
  serialized_end=1511,
)
_sym_db.RegisterEnumDescriptor(_ACTION)

Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_PBPFTPPNSDHATTRIBUTETYPE = _descriptor.EnumDescriptor(
  name='PbPftpPnsDHAttributeType',
  full_name='protocol.PbPftpPnsDHAttributeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ACTION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITIVE_ACTION', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE_ACTION', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR_ACTION', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1513,
  serialized_end=1619,
)
_sym_db.RegisterEnumDescriptor(_PBPFTPPNSDHATTRIBUTETYPE)

PbPftpPnsDHAttributeType = enum_type_wrapper.EnumTypeWrapper(_PBPFTPPNSDHATTRIBUTETYPE)
_PBPFTPHOSTTODEVNOTIFICATION = _descriptor.EnumDescriptor(
  name='PbPFtpHostToDevNotification',
  full_name='protocol.PbPFtpHostToDevNotification',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START_SYNC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_SYNC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCK_PRODUCTION_DATA', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TERMINATE_SYNC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEEP_ALIVE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_AUTOSYNC', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNS_HD_NOTIFICATION', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZE_SESSION', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TERMINATE_SESSION', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1622,
  serialized_end=1847,
)
_sym_db.RegisterEnumDescriptor(_PBPFTPHOSTTODEVNOTIFICATION)

PbPFtpHostToDevNotification = enum_type_wrapper.EnumTypeWrapper(_PBPFTPHOSTTODEVNOTIFICATION)
_PBPFTPPNSHDCATEGORYID = _descriptor.EnumDescriptor(
  name='PbPftpPnsHDCategoryID',
  full_name='protocol.PbPftpPnsHDCategoryID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_OTHER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_POLAR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_INCOMINGCALL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_MISSEDCALL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_VOICEMAIL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_SOCIAL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_SCHEDULE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_EMAIL', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_NEWS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_HEALTHANDFITNESS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_BUSINESSANDFINANCE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_LOCATION', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_ENTERTAINMENT', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_ALARM', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_PROMO', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_RECOMMENDATION', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_STATUS', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_ID_TRANSPORT', index=17, number=17,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1850,
  serialized_end=2355,
)
_sym_db.RegisterEnumDescriptor(_PBPFTPPNSHDCATEGORYID)

PbPftpPnsHDCategoryID = enum_type_wrapper.EnumTypeWrapper(_PBPFTPPNSHDCATEGORYID)
_PBPFTPPNSHDATTRIBUTETYPE = _descriptor.EnumDescriptor(
  name='PbPftpPnsHDAttributeType',
  full_name='protocol.PbPftpPnsHDAttributeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TITLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTITLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITIVE_ACTION_LABEL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE_ACTION_LABEL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_NAME', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLEAR_ACTION_LABEL', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2358,
  serialized_end=2522,
)
_sym_db.RegisterEnumDescriptor(_PBPFTPPNSHDATTRIBUTETYPE)

PbPftpPnsHDAttributeType = enum_type_wrapper.EnumTypeWrapper(_PBPFTPPNSHDATTRIBUTETYPE)
FILESYSTEM_MODIFIED = 0
INTERNAL_TEST_EVENT = 1
IDLING = 2
BATTERY_STATUS = 3
INACTIVITY_ALERT = 4
TRAINING_SESSION_STATUS = 5
SYNC_REQUIRED = 7
AUTOSYNC_STATUS = 8
PNS_DH_NOTIFICATION_RESPONSE = 9
PNS_SETTINGS = 10
CREATED = 0
UPDATED = 1
REMOVED = 2
UNKNOWN_ACTION = 1
POSITIVE_ACTION = 2
NEGATIVE_ACTION = 3
CLEAR_ACTION = 4
START_SYNC = 0
STOP_SYNC = 1
RESET = 2
LOCK_PRODUCTION_DATA = 3
TERMINATE_SYNC = 4
KEEP_ALIVE = 5
START_AUTOSYNC = 6
PNS_HD_NOTIFICATION = 7
INITIALIZE_SESSION = 8
TERMINATE_SESSION = 9
CATEGORY_ID_OTHER = 0
CATEGORY_ID_POLAR = 1
CATEGORY_ID_INCOMINGCALL = 2
CATEGORY_ID_MISSEDCALL = 3
CATEGORY_ID_VOICEMAIL = 4
CATEGORY_ID_SOCIAL = 5
CATEGORY_ID_SCHEDULE = 6
CATEGORY_ID_EMAIL = 7
CATEGORY_ID_NEWS = 8
CATEGORY_ID_HEALTHANDFITNESS = 9
CATEGORY_ID_BUSINESSANDFINANCE = 10
CATEGORY_ID_LOCATION = 11
CATEGORY_ID_ENTERTAINMENT = 12
CATEGORY_ID_ALARM = 13
CATEGORY_ID_PROMO = 14
CATEGORY_ID_RECOMMENDATION = 15
CATEGORY_ID_STATUS = 16
CATEGORY_ID_TRANSPORT = 17
TITLE = 0
SUBTITLE = 1
MESSAGE = 2
POSITIVE_ACTION_LABEL = 3
NEGATIVE_ACTION_LABEL = 4
APPLICATION_NAME = 5
CLEAR_ACTION_LABEL = 6



_PBPFTPFILESYSTEMMODIFIEDPARAMS = _descriptor.Descriptor(
  name='PbPFtpFilesystemModifiedParams',
  full_name='protocol.PbPFtpFilesystemModifiedParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='protocol.PbPFtpFilesystemModifiedParams.action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='protocol.PbPFtpFilesystemModifiedParams.path', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=50,
  serialized_end=130,
)


_PBPFTPINACTIVITYALERT = _descriptor.Descriptor(
  name='PbPFtpInactivityAlert',
  full_name='protocol.PbPFtpInactivityAlert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='countdown', full_name='protocol.PbPFtpInactivityAlert.countdown', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=132,
  serialized_end=174,
)


_PBPFTPTRAININGSESSIONSTATUS = _descriptor.Descriptor(
  name='PbPFtpTrainingSessionStatus',
  full_name='protocol.PbPFtpTrainingSessionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inprogress', full_name='protocol.PbPFtpTrainingSessionStatus.inprogress', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=176,
  serialized_end=225,
)


_PBPFTPAUTOSYNCSTATUSPARAMS = _descriptor.Descriptor(
  name='PbPFtpAutoSyncStatusParams',
  full_name='protocol.PbPFtpAutoSyncStatusParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='succeeded', full_name='protocol.PbPFtpAutoSyncStatusParams.succeeded', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='protocol.PbPFtpAutoSyncStatusParams.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=227,
  serialized_end=295,
)


_PBPFTPPNSDHATTRIBUTE = _descriptor.Descriptor(
  name='PbPftpPnsDHAttribute',
  full_name='protocol.PbPftpPnsDHAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.PbPftpPnsDHAttribute.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=297,
  serialized_end=369,
)


_PBPFTPPNSDHNOTIFICATIONRESPONSE = _descriptor.Descriptor(
  name='PbPftpPnsDHNotificationResponse',
  full_name='protocol.PbPftpPnsDHNotificationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_id', full_name='protocol.PbPftpPnsDHNotificationResponse.notification_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='protocol.PbPftpPnsDHNotificationResponse.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=371,
  serialized_end=481,
)


_PBPFTPPNSSTATE = _descriptor.Descriptor(
  name='PbPftpPnsState',
  full_name='protocol.PbPftpPnsState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notifications_enabled', full_name='protocol.PbPftpPnsState.notifications_enabled', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preview_enabled', full_name='protocol.PbPftpPnsState.preview_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=483,
  serialized_end=555,
)


_PBPFTPSTOPSYNCPARAMS = _descriptor.Descriptor(
  name='PbPFtpStopSyncParams',
  full_name='protocol.PbPFtpStopSyncParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='completed', full_name='protocol.PbPFtpStopSyncParams.completed', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='protocol.PbPFtpStopSyncParams.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=557,
  serialized_end=619,
)


_PBPFTPFACTORYRESETPARAMS = _descriptor.Descriptor(
  name='PbPFtpFactoryResetParams',
  full_name='protocol.PbPFtpFactoryResetParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sleep', full_name='protocol.PbPFtpFactoryResetParams.sleep', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='do_factory_defaults', full_name='protocol.PbPFtpFactoryResetParams.do_factory_defaults', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ota_fwupdate', full_name='protocol.PbPFtpFactoryResetParams.ota_fwupdate', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=621,
  serialized_end=726,
)


_PBPFTPSTARTAUTOSYNCPARAMS = _descriptor.Descriptor(
  name='PbPFtpStartAutosyncParams',
  full_name='protocol.PbPFtpStartAutosyncParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='protocol.PbPFtpStartAutosyncParams.timeout', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=728,
  serialized_end=772,
)


_PBPFTPPNSHDATTRIBUTE = _descriptor.Descriptor(
  name='PbPftpPnsHDAttribute',
  full_name='protocol.PbPftpPnsHDAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.PbPftpPnsHDAttribute.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='protocol.PbPftpPnsHDAttribute.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_full_size', full_name='protocol.PbPftpPnsHDAttribute.attribute_full_size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=774,
  serialized_end=889,
)


_PBPFTPPNSHDNOTIFICATION = _descriptor.Descriptor(
  name='PbPftpPnsHDNotification',
  full_name='protocol.PbPftpPnsHDNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_id', full_name='protocol.PbPftpPnsHDNotification.notification_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category_id', full_name='protocol.PbPftpPnsHDNotification.category_id', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='protocol.PbPftpPnsHDNotification.action', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='issue_time', full_name='protocol.PbPftpPnsHDNotification.issue_time', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_same_category_notifications', full_name='protocol.PbPftpPnsHDNotification.new_same_category_notifications', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unread_same_category_notifications', full_name='protocol.PbPftpPnsHDNotification.unread_same_category_notifications', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='protocol.PbPftpPnsHDNotification.attributes', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=892,
  serialized_end=1205,
)

_PBPFTPFILESYSTEMMODIFIEDPARAMS.fields_by_name['action'].enum_type = _ACTION
_PBPFTPPNSDHATTRIBUTE.fields_by_name['type'].enum_type = _PBPFTPPNSDHATTRIBUTETYPE
_PBPFTPPNSDHNOTIFICATIONRESPONSE.fields_by_name['attributes'].message_type = _PBPFTPPNSDHATTRIBUTE
_PBPFTPPNSHDATTRIBUTE.fields_by_name['type'].enum_type = _PBPFTPPNSHDATTRIBUTETYPE
_PBPFTPPNSHDNOTIFICATION.fields_by_name['category_id'].enum_type = _PBPFTPPNSHDCATEGORYID
_PBPFTPPNSHDNOTIFICATION.fields_by_name['action'].enum_type = _ACTION
_PBPFTPPNSHDNOTIFICATION.fields_by_name['issue_time'].message_type = types_pb2._PBLOCALDATETIME
_PBPFTPPNSHDNOTIFICATION.fields_by_name['attributes'].message_type = _PBPFTPPNSHDATTRIBUTE
DESCRIPTOR.message_types_by_name['PbPFtpFilesystemModifiedParams'] = _PBPFTPFILESYSTEMMODIFIEDPARAMS
DESCRIPTOR.message_types_by_name['PbPFtpInactivityAlert'] = _PBPFTPINACTIVITYALERT
DESCRIPTOR.message_types_by_name['PbPFtpTrainingSessionStatus'] = _PBPFTPTRAININGSESSIONSTATUS
DESCRIPTOR.message_types_by_name['PbPFtpAutoSyncStatusParams'] = _PBPFTPAUTOSYNCSTATUSPARAMS
DESCRIPTOR.message_types_by_name['PbPftpPnsDHAttribute'] = _PBPFTPPNSDHATTRIBUTE
DESCRIPTOR.message_types_by_name['PbPftpPnsDHNotificationResponse'] = _PBPFTPPNSDHNOTIFICATIONRESPONSE
DESCRIPTOR.message_types_by_name['PbPftpPnsState'] = _PBPFTPPNSSTATE
DESCRIPTOR.message_types_by_name['PbPFtpStopSyncParams'] = _PBPFTPSTOPSYNCPARAMS
DESCRIPTOR.message_types_by_name['PbPFtpFactoryResetParams'] = _PBPFTPFACTORYRESETPARAMS
DESCRIPTOR.message_types_by_name['PbPFtpStartAutosyncParams'] = _PBPFTPSTARTAUTOSYNCPARAMS
DESCRIPTOR.message_types_by_name['PbPftpPnsHDAttribute'] = _PBPFTPPNSHDATTRIBUTE
DESCRIPTOR.message_types_by_name['PbPftpPnsHDNotification'] = _PBPFTPPNSHDNOTIFICATION
DESCRIPTOR.enum_types_by_name['PbPFtpDevToHostNotification'] = _PBPFTPDEVTOHOSTNOTIFICATION
DESCRIPTOR.enum_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['PbPftpPnsDHAttributeType'] = _PBPFTPPNSDHATTRIBUTETYPE
DESCRIPTOR.enum_types_by_name['PbPFtpHostToDevNotification'] = _PBPFTPHOSTTODEVNOTIFICATION
DESCRIPTOR.enum_types_by_name['PbPftpPnsHDCategoryID'] = _PBPFTPPNSHDCATEGORYID
DESCRIPTOR.enum_types_by_name['PbPftpPnsHDAttributeType'] = _PBPFTPPNSHDATTRIBUTETYPE

PbPFtpFilesystemModifiedParams = _reflection.GeneratedProtocolMessageType('PbPFtpFilesystemModifiedParams', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPFILESYSTEMMODIFIEDPARAMS,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpFilesystemModifiedParams)
  ))
_sym_db.RegisterMessage(PbPFtpFilesystemModifiedParams)

PbPFtpInactivityAlert = _reflection.GeneratedProtocolMessageType('PbPFtpInactivityAlert', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPINACTIVITYALERT,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpInactivityAlert)
  ))
_sym_db.RegisterMessage(PbPFtpInactivityAlert)

PbPFtpTrainingSessionStatus = _reflection.GeneratedProtocolMessageType('PbPFtpTrainingSessionStatus', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPTRAININGSESSIONSTATUS,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpTrainingSessionStatus)
  ))
_sym_db.RegisterMessage(PbPFtpTrainingSessionStatus)

PbPFtpAutoSyncStatusParams = _reflection.GeneratedProtocolMessageType('PbPFtpAutoSyncStatusParams', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPAUTOSYNCSTATUSPARAMS,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpAutoSyncStatusParams)
  ))
_sym_db.RegisterMessage(PbPFtpAutoSyncStatusParams)

PbPftpPnsDHAttribute = _reflection.GeneratedProtocolMessageType('PbPftpPnsDHAttribute', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPPNSDHATTRIBUTE,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPftpPnsDHAttribute)
  ))
_sym_db.RegisterMessage(PbPftpPnsDHAttribute)

PbPftpPnsDHNotificationResponse = _reflection.GeneratedProtocolMessageType('PbPftpPnsDHNotificationResponse', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPPNSDHNOTIFICATIONRESPONSE,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPftpPnsDHNotificationResponse)
  ))
_sym_db.RegisterMessage(PbPftpPnsDHNotificationResponse)

PbPftpPnsState = _reflection.GeneratedProtocolMessageType('PbPftpPnsState', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPPNSSTATE,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPftpPnsState)
  ))
_sym_db.RegisterMessage(PbPftpPnsState)

PbPFtpStopSyncParams = _reflection.GeneratedProtocolMessageType('PbPFtpStopSyncParams', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPSTOPSYNCPARAMS,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpStopSyncParams)
  ))
_sym_db.RegisterMessage(PbPFtpStopSyncParams)

PbPFtpFactoryResetParams = _reflection.GeneratedProtocolMessageType('PbPFtpFactoryResetParams', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPFACTORYRESETPARAMS,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpFactoryResetParams)
  ))
_sym_db.RegisterMessage(PbPFtpFactoryResetParams)

PbPFtpStartAutosyncParams = _reflection.GeneratedProtocolMessageType('PbPFtpStartAutosyncParams', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPSTARTAUTOSYNCPARAMS,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPFtpStartAutosyncParams)
  ))
_sym_db.RegisterMessage(PbPFtpStartAutosyncParams)

PbPftpPnsHDAttribute = _reflection.GeneratedProtocolMessageType('PbPftpPnsHDAttribute', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPPNSHDATTRIBUTE,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPftpPnsHDAttribute)
  ))
_sym_db.RegisterMessage(PbPftpPnsHDAttribute)

PbPftpPnsHDNotification = _reflection.GeneratedProtocolMessageType('PbPftpPnsHDNotification', (_message.Message,), dict(
  DESCRIPTOR = _PBPFTPPNSHDNOTIFICATION,
  __module__ = 'pftp_notification_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PbPftpPnsHDNotification)
  ))
_sym_db.RegisterMessage(PbPftpPnsHDNotification)


# @@protoc_insertion_point(module_scope)
