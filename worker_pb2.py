# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cworker.proto\x12\rworkerpackage\"\x1a\n\nDriverPort\x12\x0c\n\x04port\x18\x01 \x01(\x05\"#\n\x06Status\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"=\n\x08MapInput\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x13\n\x0bmap_task_id\x18\x02 \x01(\x05\x12\t\n\x01m\x18\x03 \x01(\x05\"\"\n\x08ReduceId\x12\x16\n\x0ereduce_task_id\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty2\xf6\x01\n\x06Worker\x12\x41\n\rSetDriverPort\x12\x19.workerpackage.DriverPort\x1a\x15.workerpackage.Status\x12\x35\n\x03Map\x12\x17.workerpackage.MapInput\x1a\x15.workerpackage.Status\x12\x38\n\x06Reduce\x12\x17.workerpackage.ReduceId\x1a\x15.workerpackage.Status\x12\x38\n\tTerminate\x12\x14.workerpackage.Empty\x1a\x15.workerpackage.Statusb\x06proto3')



_DRIVERPORT = DESCRIPTOR.message_types_by_name['DriverPort']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_MAPINPUT = DESCRIPTOR.message_types_by_name['MapInput']
_REDUCEID = DESCRIPTOR.message_types_by_name['ReduceId']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
DriverPort = _reflection.GeneratedProtocolMessageType('DriverPort', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERPORT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerpackage.DriverPort)
  })
_sym_db.RegisterMessage(DriverPort)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerpackage.Status)
  })
_sym_db.RegisterMessage(Status)

MapInput = _reflection.GeneratedProtocolMessageType('MapInput', (_message.Message,), {
  'DESCRIPTOR' : _MAPINPUT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerpackage.MapInput)
  })
_sym_db.RegisterMessage(MapInput)

ReduceId = _reflection.GeneratedProtocolMessageType('ReduceId', (_message.Message,), {
  'DESCRIPTOR' : _REDUCEID,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerpackage.ReduceId)
  })
_sym_db.RegisterMessage(ReduceId)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:workerpackage.Empty)
  })
_sym_db.RegisterMessage(Empty)

_WORKER = DESCRIPTOR.services_by_name['Worker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DRIVERPORT._serialized_start=31
  _DRIVERPORT._serialized_end=57
  _STATUS._serialized_start=59
  _STATUS._serialized_end=94
  _MAPINPUT._serialized_start=96
  _MAPINPUT._serialized_end=157
  _REDUCEID._serialized_start=159
  _REDUCEID._serialized_end=193
  _EMPTY._serialized_start=195
  _EMPTY._serialized_end=202
  _WORKER._serialized_start=205
  _WORKER._serialized_end=451
# @@protoc_insertion_point(module_scope)