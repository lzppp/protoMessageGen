# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testgen.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='testgen.proto',
  package='',
  syntax='proto3',
  serialized_pb=b'\n\rtestgen.proto\"u\n\rRequestCommon\x12\x0e\n\x06userid\x18\x01 \x01(\x05\x12\x0f\n\x07userkey\x18\x02 \x01(\t\x12\r\n\x05\x63mdid\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x10\n\x08platform\x18\x06 \x01(\x05\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTCOMMON = _descriptor.Descriptor(
  name='RequestCommon',
  full_name='RequestCommon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='RequestCommon.userid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userkey', full_name='RequestCommon.userkey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmdid', full_name='RequestCommon.cmdid', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='RequestCommon.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='RequestCommon.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='RequestCommon.platform', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['RequestCommon'] = _REQUESTCOMMON

RequestCommon = _reflection.GeneratedProtocolMessageType('RequestCommon', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTCOMMON,
  __module__ = 'testgen_pb2'
  # @@protoc_insertion_point(class_scope:RequestCommon)
  ))
_sym_db.RegisterMessage(RequestCommon)


# @@protoc_insertion_point(module_scope)
