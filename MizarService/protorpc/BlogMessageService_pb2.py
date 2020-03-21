# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BlogMessageService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BlogMessageService.proto',
  package='com.dipper.proto.rpc',
  syntax='proto3',
  serialized_options=b'\n\024com.dipper.proto.rpcB\020BlogMessageProtoP\001',
  serialized_pb=b'\n\x18\x42logMessageService.proto\x12\x14\x63om.dipper.proto.rpc\"u\n\x0e\x42logMessagePro\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x62log_id\x18\x02 \x01(\x05\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\x10\n\x08msg_type\x18\x04 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x12\n\nbuild_time\x18\x06 \x01(\x05\x32\x14\n\x12\x42logMessageServiceB*\n\x14\x63om.dipper.proto.rpcB\x10\x42logMessageProtoP\x01\x62\x06proto3'
)




_BLOGMESSAGEPRO = _descriptor.Descriptor(
  name='BlogMessagePro',
  full_name='com.dipper.proto.rpc.BlogMessagePro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.dipper.proto.rpc.BlogMessagePro.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blog_id', full_name='com.dipper.proto.rpc.BlogMessagePro.blog_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.dipper.proto.rpc.BlogMessagePro.user_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='com.dipper.proto.rpc.BlogMessagePro.msg_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='com.dipper.proto.rpc.BlogMessagePro.content', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_time', full_name='com.dipper.proto.rpc.BlogMessagePro.build_time', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['BlogMessagePro'] = _BLOGMESSAGEPRO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlogMessagePro = _reflection.GeneratedProtocolMessageType('BlogMessagePro', (_message.Message,), {
  'DESCRIPTOR' : _BLOGMESSAGEPRO,
  '__module__' : 'BlogMessageService_pb2'
  # @@protoc_insertion_point(class_scope:com.dipper.proto.rpc.BlogMessagePro)
  })
_sym_db.RegisterMessage(BlogMessagePro)


DESCRIPTOR._options = None

_BLOGMESSAGESERVICE = _descriptor.ServiceDescriptor(
  name='BlogMessageService',
  full_name='com.dipper.proto.rpc.BlogMessageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=169,
  serialized_end=189,
  methods=[
])
_sym_db.RegisterServiceDescriptor(_BLOGMESSAGESERVICE)

DESCRIPTOR.services_by_name['BlogMessageService'] = _BLOGMESSAGESERVICE

# @@protoc_insertion_point(module_scope)
