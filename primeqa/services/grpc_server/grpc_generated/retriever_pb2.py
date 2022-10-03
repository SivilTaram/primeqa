# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: retriever.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import pipelines_pb2 as pipelines__pb2
from . import indexer_pb2 as indexer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fretriever.proto\x12\x08retrieve\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0fpipelines.proto\x1a\rindexer.proto\"\xa4\x01\n\rSearchRequest\x12%\n\x08pipeline\x18\x01 \x01(\x0b\x32\x13.pipelines.Pipeline\x12\x10\n\x08index_id\x18\x02 \x01(\t\x12\r\n\x05query\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x04 \x01(\r\x12\x11\n\tthreshold\x18\x05 \x01(\x01\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\"b\n\x03Hit\x12!\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\x0f.index.Document\x12\r\n\x05score\x18\x02 \x01(\x01\x12)\n\x08metadata\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct2?\n\tRetriever\x12\x32\n\x06Search\x12\x17.retrieve.SearchRequest\x1a\r.retrieve.Hit0\x01\x62\x06proto3')



_SEARCHREQUEST = DESCRIPTOR.message_types_by_name['SearchRequest']
_HIT = DESCRIPTOR.message_types_by_name['Hit']
SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'retriever_pb2'
  # @@protoc_insertion_point(class_scope:retrieve.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

Hit = _reflection.GeneratedProtocolMessageType('Hit', (_message.Message,), {
  'DESCRIPTOR' : _HIT,
  '__module__' : 'retriever_pb2'
  # @@protoc_insertion_point(class_scope:retrieve.Hit)
  })
_sym_db.RegisterMessage(Hit)

_RETRIEVER = DESCRIPTOR.services_by_name['Retriever']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SEARCHREQUEST._serialized_start=92
  _SEARCHREQUEST._serialized_end=256
  _HIT._serialized_start=258
  _HIT._serialized_end=356
  _RETRIEVER._serialized_start=358
  _RETRIEVER._serialized_end=421
# @@protoc_insertion_point(module_scope)
