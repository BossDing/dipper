// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: BaseService.proto

package com.dipper.proto.rpc;

public interface RpcResultOrBuilder extends
    // @@protoc_insertion_point(interface_extends:com.dipper.proto.rpc.RpcResult)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>int32 rpc_code = 1;</code>
   * @return The rpcCode.
   */
  int getRpcCode();

  /**
   * <code>string message = 2;</code>
   * @return The message.
   */
  java.lang.String getMessage();
  /**
   * <code>string message = 2;</code>
   * @return The bytes for message.
   */
  com.google.protobuf.ByteString
      getMessageBytes();

  /**
   * <code>.google.protobuf.Any data = 3;</code>
   * @return Whether the data field is set.
   */
  boolean hasData();
  /**
   * <code>.google.protobuf.Any data = 3;</code>
   * @return The data.
   */
  com.google.protobuf.Any getData();
  /**
   * <code>.google.protobuf.Any data = 3;</code>
   */
  com.google.protobuf.AnyOrBuilder getDataOrBuilder();
}
