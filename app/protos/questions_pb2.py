# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: questions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fquestions.proto\x12\x0equestionAnswer\"#\n\x0fQuestionRequest\x12\x10\n\x08question\x18\x01 \x01(\t\" \n\x0e\x41nswerResponse\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t2`\n\x0eQuestionAnswer\x12N\n\tGetAnswer\x12\x1f.questionAnswer.QuestionRequest\x1a\x1e.questionAnswer.AnswerResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'questions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_QUESTIONREQUEST']._serialized_start=35
  _globals['_QUESTIONREQUEST']._serialized_end=70
  _globals['_ANSWERRESPONSE']._serialized_start=72
  _globals['_ANSWERRESPONSE']._serialized_end=104
  _globals['_QUESTIONANSWER']._serialized_start=106
  _globals['_QUESTIONANSWER']._serialized_end=202
# @@protoc_insertion_point(module_scope)
