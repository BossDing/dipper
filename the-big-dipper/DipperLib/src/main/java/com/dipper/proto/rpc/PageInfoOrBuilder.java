// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: BaseService.proto

package com.dipper.proto.rpc;

public interface PageInfoOrBuilder extends
    // @@protoc_insertion_point(interface_extends:com.dipper.proto.rpc.PageInfo)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>.com.dipper.proto.rpc.MessageType type = 1;</code>
   * @return The enum numeric value on the wire for type.
   */
  int getTypeValue();
  /**
   * <code>.com.dipper.proto.rpc.MessageType type = 1;</code>
   * @return The type.
   */
  com.dipper.proto.rpc.MessageType getType();

  /**
   * <code>int32 page_num = 2;</code>
   * @return The pageNum.
   */
  int getPageNum();

  /**
   * <code>int32 page_size = 3;</code>
   * @return The pageSize.
   */
  int getPageSize();
}
