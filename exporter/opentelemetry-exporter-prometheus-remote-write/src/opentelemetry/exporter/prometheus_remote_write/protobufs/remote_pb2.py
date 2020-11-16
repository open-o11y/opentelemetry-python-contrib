# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2 as types__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='remote.proto',
  package='prometheus',
  syntax='proto3',
  serialized_options=b'Z\006prompb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cremote.proto\x12\nprometheus\x1a\x0btypes.proto\x1a\x14gogoproto/gogo.proto\"@\n\x0cWriteRequest\x12\x30\n\ntimeseries\x18\x01 \x03(\x0b\x32\x16.prometheus.TimeSeriesB\x04\xc8\xde\x1f\x00\"\xae\x01\n\x0bReadRequest\x12\"\n\x07queries\x18\x01 \x03(\x0b\x32\x11.prometheus.Query\x12\x45\n\x17\x61\x63\x63\x65pted_response_types\x18\x02 \x03(\x0e\x32$.prometheus.ReadRequest.ResponseType\"4\n\x0cResponseType\x12\x0b\n\x07SAMPLES\x10\x00\x12\x17\n\x13STREAMED_XOR_CHUNKS\x10\x01\"8\n\x0cReadResponse\x12(\n\x07results\x18\x01 \x03(\x0b\x32\x17.prometheus.QueryResult\"\x8f\x01\n\x05Query\x12\x1a\n\x12start_timestamp_ms\x18\x01 \x01(\x03\x12\x18\n\x10\x65nd_timestamp_ms\x18\x02 \x01(\x03\x12*\n\x08matchers\x18\x03 \x03(\x0b\x32\x18.prometheus.LabelMatcher\x12$\n\x05hints\x18\x04 \x01(\x0b\x32\x15.prometheus.ReadHints\"9\n\x0bQueryResult\x12*\n\ntimeseries\x18\x01 \x03(\x0b\x32\x16.prometheus.TimeSeries\"]\n\x13\x43hunkedReadResponse\x12\x31\n\x0e\x63hunked_series\x18\x01 \x03(\x0b\x32\x19.prometheus.ChunkedSeries\x12\x13\n\x0bquery_index\x18\x02 \x01(\x03\x42\x08Z\x06prompbb\x06proto3'
  ,
  dependencies=[types__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])



_READREQUEST_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='prometheus.ReadRequest.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SAMPLES', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STREAMED_XOR_CHUNKS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=252,
  serialized_end=304,
)
_sym_db.RegisterEnumDescriptor(_READREQUEST_RESPONSETYPE)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='prometheus.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeseries', full_name='prometheus.WriteRequest.timeseries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=63,
  serialized_end=127,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='prometheus.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='queries', full_name='prometheus.ReadRequest.queries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accepted_response_types', full_name='prometheus.ReadRequest.accepted_response_types', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _READREQUEST_RESPONSETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=304,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='prometheus.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='prometheus.ReadResponse.results', index=0,
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
  serialized_start=306,
  serialized_end=362,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='prometheus.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_timestamp_ms', full_name='prometheus.Query.start_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_timestamp_ms', full_name='prometheus.Query.end_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matchers', full_name='prometheus.Query.matchers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hints', full_name='prometheus.Query.hints', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=365,
  serialized_end=508,
)


_QUERYRESULT = _descriptor.Descriptor(
  name='QueryResult',
  full_name='prometheus.QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeseries', full_name='prometheus.QueryResult.timeseries', index=0,
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
  serialized_start=510,
  serialized_end=567,
)


_CHUNKEDREADRESPONSE = _descriptor.Descriptor(
  name='ChunkedReadResponse',
  full_name='prometheus.ChunkedReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunked_series', full_name='prometheus.ChunkedReadResponse.chunked_series', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_index', full_name='prometheus.ChunkedReadResponse.query_index', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=569,
  serialized_end=662,
)

_WRITEREQUEST.fields_by_name['timeseries'].message_type = types__pb2._TIMESERIES
_READREQUEST.fields_by_name['queries'].message_type = _QUERY
_READREQUEST.fields_by_name['accepted_response_types'].enum_type = _READREQUEST_RESPONSETYPE
_READREQUEST_RESPONSETYPE.containing_type = _READREQUEST
_READRESPONSE.fields_by_name['results'].message_type = _QUERYRESULT
_QUERY.fields_by_name['matchers'].message_type = types__pb2._LABELMATCHER
_QUERY.fields_by_name['hints'].message_type = types__pb2._READHINTS
_QUERYRESULT.fields_by_name['timeseries'].message_type = types__pb2._TIMESERIES
_CHUNKEDREADRESPONSE.fields_by_name['chunked_series'].message_type = types__pb2._CHUNKEDSERIES
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT
DESCRIPTOR.message_types_by_name['ChunkedReadResponse'] = _CHUNKEDREADRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'remote_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'remote_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'remote_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'remote_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.Query)
  })
_sym_db.RegisterMessage(Query)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULT,
  '__module__' : 'remote_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.QueryResult)
  })
_sym_db.RegisterMessage(QueryResult)

ChunkedReadResponse = _reflection.GeneratedProtocolMessageType('ChunkedReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHUNKEDREADRESPONSE,
  '__module__' : 'remote_pb2'
  # @@protoc_insertion_point(class_scope:prometheus.ChunkedReadResponse)
  })
_sym_db.RegisterMessage(ChunkedReadResponse)


DESCRIPTOR._options = None
_WRITEREQUEST.fields_by_name['timeseries']._options = None
# @@protoc_insertion_point(module_scope)
