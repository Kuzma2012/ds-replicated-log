# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\nua.edu.ucuB\rLoggerServiceP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\"\x19\n\nLogMessage\x12\x0b\n\x03log\x18\x01 \x01(\t\"0\n\x14\x41ppendMessageRequest\x12\x18\n\x03log\x18\x01 \x01(\x0b\x32\x0b.LogMessage\"\x17\n\x15\x41ppendMessageResponse\"\x15\n\x13ListMessagesRequest\"1\n\x14ListMessagesResponse\x12\x19\n\x04logs\x18\x01 \x03(\x0b\x32\x0b.LogMessage2\x89\x01\n\x06Logger\x12@\n\rAppendMessage\x12\x15.AppendMessageRequest\x1a\x16.AppendMessageResponse\"\x00\x12=\n\x0cListMessages\x12\x14.ListMessagesRequest\x1a\x15.ListMessagesResponse\"\x00\x42\x1d\n\nua.edu.ucuB\rLoggerServiceP\x01\x62\x06proto3'
)




_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='LogMessage.log', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=13,
  serialized_end=38,
)


_APPENDMESSAGEREQUEST = _descriptor.Descriptor(
  name='AppendMessageRequest',
  full_name='AppendMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log', full_name='AppendMessageRequest.log', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=40,
  serialized_end=88,
)


_APPENDMESSAGERESPONSE = _descriptor.Descriptor(
  name='AppendMessageResponse',
  full_name='AppendMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=90,
  serialized_end=113,
)


_LISTMESSAGESREQUEST = _descriptor.Descriptor(
  name='ListMessagesRequest',
  full_name='ListMessagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=115,
  serialized_end=136,
)


_LISTMESSAGESRESPONSE = _descriptor.Descriptor(
  name='ListMessagesResponse',
  full_name='ListMessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logs', full_name='ListMessagesResponse.logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=138,
  serialized_end=187,
)

_APPENDMESSAGEREQUEST.fields_by_name['log'].message_type = _LOGMESSAGE
_LISTMESSAGESRESPONSE.fields_by_name['logs'].message_type = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['AppendMessageRequest'] = _APPENDMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['AppendMessageResponse'] = _APPENDMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['ListMessagesRequest'] = _LISTMESSAGESREQUEST
DESCRIPTOR.message_types_by_name['ListMessagesResponse'] = _LISTMESSAGESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:LogMessage)
  })
_sym_db.RegisterMessage(LogMessage)

AppendMessageRequest = _reflection.GeneratedProtocolMessageType('AppendMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPENDMESSAGEREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:AppendMessageRequest)
  })
_sym_db.RegisterMessage(AppendMessageRequest)

AppendMessageResponse = _reflection.GeneratedProtocolMessageType('AppendMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPENDMESSAGERESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:AppendMessageResponse)
  })
_sym_db.RegisterMessage(AppendMessageResponse)

ListMessagesRequest = _reflection.GeneratedProtocolMessageType('ListMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMESSAGESREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:ListMessagesRequest)
  })
_sym_db.RegisterMessage(ListMessagesRequest)

ListMessagesResponse = _reflection.GeneratedProtocolMessageType('ListMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMESSAGESRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:ListMessagesResponse)
  })
_sym_db.RegisterMessage(ListMessagesResponse)


DESCRIPTOR._options = None

_LOGGER = _descriptor.ServiceDescriptor(
  name='Logger',
  full_name='Logger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=190,
  serialized_end=327,
  methods=[
  _descriptor.MethodDescriptor(
    name='AppendMessage',
    full_name='Logger.AppendMessage',
    index=0,
    containing_service=None,
    input_type=_APPENDMESSAGEREQUEST,
    output_type=_APPENDMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListMessages',
    full_name='Logger.ListMessages',
    index=1,
    containing_service=None,
    input_type=_LISTMESSAGESREQUEST,
    output_type=_LISTMESSAGESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGGER)

DESCRIPTOR.services_by_name['Logger'] = _LOGGER

# @@protoc_insertion_point(module_scope)
