# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2


class LoggerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppendMessage = channel.unary_unary(
                '/Logger/AppendMessage',
                request_serializer=api__pb2.AppendMessageRequest.SerializeToString,
                response_deserializer=api__pb2.AppendMessageResponse.FromString,
                )
        self.ListMessages = channel.unary_unary(
                '/Logger/ListMessages',
                request_serializer=api__pb2.ListMessagesRequest.SerializeToString,
                response_deserializer=api__pb2.ListMessagesResponse.FromString,
                )


class LoggerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AppendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoggerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AppendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.AppendMessage,
                    request_deserializer=api__pb2.AppendMessageRequest.FromString,
                    response_serializer=api__pb2.AppendMessageResponse.SerializeToString,
            ),
            'ListMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMessages,
                    request_deserializer=api__pb2.ListMessagesRequest.FromString,
                    response_serializer=api__pb2.ListMessagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Logger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Logger(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AppendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Logger/AppendMessage',
            api__pb2.AppendMessageRequest.SerializeToString,
            api__pb2.AppendMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Logger/ListMessages',
            api__pb2.ListMessagesRequest.SerializeToString,
            api__pb2.ListMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
