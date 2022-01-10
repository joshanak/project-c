; Auto-generated. Do not edit!


(cl:in-package med_uav_control-msg)


;//! \htmlinclude PIDController.msg.html

(cl:defclass <PIDController> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (ref
    :reader ref
    :initarg :ref
    :type cl:float
    :initform 0.0)
   (meas
    :reader meas
    :initarg :meas
    :type cl:float
    :initform 0.0)
   (P
    :reader P
    :initarg :P
    :type cl:float
    :initform 0.0)
   (I
    :reader I
    :initarg :I
    :type cl:float
    :initform 0.0)
   (D
    :reader D
    :initarg :D
    :type cl:float
    :initform 0.0)
   (U
    :reader U
    :initarg :U
    :type cl:float
    :initform 0.0))
)

(cl:defclass PIDController (<PIDController>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PIDController>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PIDController)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name med_uav_control-msg:<PIDController> is deprecated: use med_uav_control-msg:PIDController instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:header-val is deprecated.  Use med_uav_control-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'ref-val :lambda-list '(m))
(cl:defmethod ref-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:ref-val is deprecated.  Use med_uav_control-msg:ref instead.")
  (ref m))

(cl:ensure-generic-function 'meas-val :lambda-list '(m))
(cl:defmethod meas-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:meas-val is deprecated.  Use med_uav_control-msg:meas instead.")
  (meas m))

(cl:ensure-generic-function 'P-val :lambda-list '(m))
(cl:defmethod P-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:P-val is deprecated.  Use med_uav_control-msg:P instead.")
  (P m))

(cl:ensure-generic-function 'I-val :lambda-list '(m))
(cl:defmethod I-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:I-val is deprecated.  Use med_uav_control-msg:I instead.")
  (I m))

(cl:ensure-generic-function 'D-val :lambda-list '(m))
(cl:defmethod D-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:D-val is deprecated.  Use med_uav_control-msg:D instead.")
  (D m))

(cl:ensure-generic-function 'U-val :lambda-list '(m))
(cl:defmethod U-val ((m <PIDController>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader med_uav_control-msg:U-val is deprecated.  Use med_uav_control-msg:U instead.")
  (U m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PIDController>) ostream)
  "Serializes a message object of type '<PIDController>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ref))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'meas))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'P))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'I))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'D))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'U))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PIDController>) istream)
  "Deserializes a message object of type '<PIDController>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ref) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'meas) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'P) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'I) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'D) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'U) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PIDController>)))
  "Returns string type for a message object of type '<PIDController>"
  "med_uav_control/PIDController")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PIDController)))
  "Returns string type for a message object of type 'PIDController"
  "med_uav_control/PIDController")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PIDController>)))
  "Returns md5sum for a message object of type '<PIDController>"
  "40c7eb50c8af809a4f7f350f7833a17f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PIDController)))
  "Returns md5sum for a message object of type 'PIDController"
  "40c7eb50c8af809a4f7f350f7833a17f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PIDController>)))
  "Returns full string definition for message of type '<PIDController>"
  (cl:format cl:nil "Header header~%~%float32 ref     # referent control value~%float32 meas    # measured control value~%float32 P       # proportional component~%float32 I       # integral component~%float32 D       # derivative component~%float32 U       # sum of three components~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PIDController)))
  "Returns full string definition for message of type 'PIDController"
  (cl:format cl:nil "Header header~%~%float32 ref     # referent control value~%float32 meas    # measured control value~%float32 P       # proportional component~%float32 I       # integral component~%float32 D       # derivative component~%float32 U       # sum of three components~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PIDController>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PIDController>))
  "Converts a ROS message object to a list"
  (cl:list 'PIDController
    (cl:cons ':header (header msg))
    (cl:cons ':ref (ref msg))
    (cl:cons ':meas (meas msg))
    (cl:cons ':P (P msg))
    (cl:cons ':I (I msg))
    (cl:cons ':D (D msg))
    (cl:cons ':U (U msg))
))
