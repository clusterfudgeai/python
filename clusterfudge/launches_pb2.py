# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: launches/launches.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import resources_pb2 as resources_dot_resources__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17launches/launches.proto\x12\x0c\x63lusterfudge\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19resources/resources.proto"\x1e\n\x10GetLaunchRequest\x12\n\n\x02id\x18\x01 \x01(\t"\x15\n\x13ListLaunchesRequest">\n\x14ListLaunchesResponse\x12&\n\x08launches\x18\x01 \x03(\x0b\x32\x14.clusterfudge.Launch"\x1f\n\x11StopLaunchRequest\x12\n\n\x02id\x18\x01 \x01(\t"\x14\n\x12StopLaunchResponse"\x8c\x04\n\x06Launch\x12\x11\n\tlaunch_id\x18\x01 \x01(\x05\x12\x13\n\x0blaunched_by\x18\x02 \x01(\t\x12\x30\n\x0csubmitted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0e\x63ommand_to_run\x18\x04 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x08 \x03(\t\x12\x11\n\thostnames\x18\x05 \x03(\t\x12+\n\x06status\x18\x06 \x01(\x0e\x32\x1b.clusterfudge.Launch.Status\x12\n\n\x02id\x18\x07 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t\x12\x10\n\x08replicas\x18\x0b \x01(\x05\x12\x32\n\x11replica_resources\x18\x0c \x01(\x0b\x32\x17.clusterfudge.Resources"\xc8\x01\n\x06Status\x12\x19\n\x15LAUNCH_STATUS_UNKNOWN\x10\x00\x12\x19\n\x15LAUNCH_STATUS_PENDING\x10\x01\x12\x19\n\x15LAUNCH_STATUS_RUNNING\x10\x02\x12\x1b\n\x17LAUNCH_STATUS_COMPLETED\x10\x03\x12\x18\n\x14LAUNCH_STATUS_FAILED\x10\x04\x12\x1b\n\x17LAUNCH_STATUS_UNMANAGED\x10\x05\x12\x19\n\x15LAUNCH_STATUS_STOPPED\x10\x06"d\n\'ListLaunchesWithCommandStatusesResponse\x12\x39\n\x08launches\x18\x01 \x03(\x0b\x32\'.clusterfudge.LaunchWithCommandStatuses"\xed\x02\n\x19LaunchWithCommandStatuses\x12$\n\x06launch\x18\x01 \x01(\x0b\x32\x14.clusterfudge.Launch\x12\x1e\n\x16\x63ommands_unknown_count\x18\x02 \x01(\x03\x12%\n\x1d\x63ommands_unacknowledged_count\x18\x03 \x01(\x03\x12#\n\x1b\x63ommands_acknowledged_count\x18\x04 \x01(\x03\x12\x1e\n\x16\x63ommands_running_count\x18\x05 \x01(\x03\x12 \n\x18\x63ommands_succeeded_count\x18\x06 \x01(\x03\x12\x1d\n\x15\x63ommands_failed_count\x18\x07 \x01(\x03\x12\x1d\n\x15\x63ommands_killed_count\x18\x08 \x01(\x03\x12 \n\x18\x63ommands_cancelled_count\x18\t \x01(\x03\x12\x1c\n\x14\x63ommands_total_count\x18\n \x01(\x03"\xd0\x01\n\x13\x43reateLaunchRequest\x12\x13\n\x0blaunched_by\x18\x01 \x01(\t\x12\x16\n\x0e\x63ommand_to_run\x18\x02 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x04 \x03(\t\x12\x11\n\thostnames\x18\x03 \x03(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x10\n\x08replicas\x18\x07 \x01(\x05\x12\x32\n\x11replica_resources\x18\x08 \x01(\x0b\x32\x17.clusterfudge.Resources2\xc5\x03\n\x08Launches\x12\x43\n\tGetLaunch\x12\x1e.clusterfudge.GetLaunchRequest\x1a\x14.clusterfudge.Launch"\x00\x12W\n\x0cListLaunches\x12!.clusterfudge.ListLaunchesRequest\x1a".clusterfudge.ListLaunchesResponse"\x00\x12}\n\x1fListLaunchesWithCommandStatuses\x12!.clusterfudge.ListLaunchesRequest\x1a\x35.clusterfudge.ListLaunchesWithCommandStatusesResponse"\x00\x12I\n\x0c\x43reateLaunch\x12!.clusterfudge.CreateLaunchRequest\x1a\x14.clusterfudge.Launch"\x00\x12Q\n\nStopLaunch\x12\x1f.clusterfudge.StopLaunchRequest\x1a .clusterfudge.StopLaunchResponse"\x00\x42\x30Z.github.com/clusterfudgeai/fudge/proto/launchesb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "launches.launches_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z.github.com/clusterfudgeai/fudge/proto/launches"
    )
    _globals["_GETLAUNCHREQUEST"]._serialized_start = 101
    _globals["_GETLAUNCHREQUEST"]._serialized_end = 131
    _globals["_LISTLAUNCHESREQUEST"]._serialized_start = 133
    _globals["_LISTLAUNCHESREQUEST"]._serialized_end = 154
    _globals["_LISTLAUNCHESRESPONSE"]._serialized_start = 156
    _globals["_LISTLAUNCHESRESPONSE"]._serialized_end = 218
    _globals["_STOPLAUNCHREQUEST"]._serialized_start = 220
    _globals["_STOPLAUNCHREQUEST"]._serialized_end = 251
    _globals["_STOPLAUNCHRESPONSE"]._serialized_start = 253
    _globals["_STOPLAUNCHRESPONSE"]._serialized_end = 273
    _globals["_LAUNCH"]._serialized_start = 276
    _globals["_LAUNCH"]._serialized_end = 800
    _globals["_LAUNCH_STATUS"]._serialized_start = 600
    _globals["_LAUNCH_STATUS"]._serialized_end = 800
    _globals["_LISTLAUNCHESWITHCOMMANDSTATUSESRESPONSE"]._serialized_start = 802
    _globals["_LISTLAUNCHESWITHCOMMANDSTATUSESRESPONSE"]._serialized_end = 902
    _globals["_LAUNCHWITHCOMMANDSTATUSES"]._serialized_start = 905
    _globals["_LAUNCHWITHCOMMANDSTATUSES"]._serialized_end = 1270
    _globals["_CREATELAUNCHREQUEST"]._serialized_start = 1273
    _globals["_CREATELAUNCHREQUEST"]._serialized_end = 1481
    _globals["_LAUNCHES"]._serialized_start = 1484
    _globals["_LAUNCHES"]._serialized_end = 1937
# @@protoc_insertion_point(module_scope)
