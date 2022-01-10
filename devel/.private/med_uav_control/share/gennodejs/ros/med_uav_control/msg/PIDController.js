// Auto-generated. Do not edit!

// (in-package med_uav_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class PIDController {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.ref = null;
      this.meas = null;
      this.P = null;
      this.I = null;
      this.D = null;
      this.U = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('ref')) {
        this.ref = initObj.ref
      }
      else {
        this.ref = 0.0;
      }
      if (initObj.hasOwnProperty('meas')) {
        this.meas = initObj.meas
      }
      else {
        this.meas = 0.0;
      }
      if (initObj.hasOwnProperty('P')) {
        this.P = initObj.P
      }
      else {
        this.P = 0.0;
      }
      if (initObj.hasOwnProperty('I')) {
        this.I = initObj.I
      }
      else {
        this.I = 0.0;
      }
      if (initObj.hasOwnProperty('D')) {
        this.D = initObj.D
      }
      else {
        this.D = 0.0;
      }
      if (initObj.hasOwnProperty('U')) {
        this.U = initObj.U
      }
      else {
        this.U = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PIDController
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [ref]
    bufferOffset = _serializer.float32(obj.ref, buffer, bufferOffset);
    // Serialize message field [meas]
    bufferOffset = _serializer.float32(obj.meas, buffer, bufferOffset);
    // Serialize message field [P]
    bufferOffset = _serializer.float32(obj.P, buffer, bufferOffset);
    // Serialize message field [I]
    bufferOffset = _serializer.float32(obj.I, buffer, bufferOffset);
    // Serialize message field [D]
    bufferOffset = _serializer.float32(obj.D, buffer, bufferOffset);
    // Serialize message field [U]
    bufferOffset = _serializer.float32(obj.U, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PIDController
    let len;
    let data = new PIDController(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [ref]
    data.ref = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [meas]
    data.meas = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [P]
    data.P = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [I]
    data.I = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [D]
    data.D = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [U]
    data.U = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'med_uav_control/PIDController';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '40c7eb50c8af809a4f7f350f7833a17f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
    float32 ref     # referent control value
    float32 meas    # measured control value
    float32 P       # proportional component
    float32 I       # integral component
    float32 D       # derivative component
    float32 U       # sum of three components
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PIDController(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.ref !== undefined) {
      resolved.ref = msg.ref;
    }
    else {
      resolved.ref = 0.0
    }

    if (msg.meas !== undefined) {
      resolved.meas = msg.meas;
    }
    else {
      resolved.meas = 0.0
    }

    if (msg.P !== undefined) {
      resolved.P = msg.P;
    }
    else {
      resolved.P = 0.0
    }

    if (msg.I !== undefined) {
      resolved.I = msg.I;
    }
    else {
      resolved.I = 0.0
    }

    if (msg.D !== undefined) {
      resolved.D = msg.D;
    }
    else {
      resolved.D = 0.0
    }

    if (msg.U !== undefined) {
      resolved.U = msg.U;
    }
    else {
      resolved.U = 0.0
    }

    return resolved;
    }
};

module.exports = PIDController;
