# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc



class GroupMessageServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """


class GroupMessageServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass


def add_GroupMessageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.dipper.proto.rpc.GroupMessageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
