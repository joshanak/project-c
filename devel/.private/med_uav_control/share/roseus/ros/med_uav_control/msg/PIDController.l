;; Auto-generated. Do not edit!


(when (boundp 'med_uav_control::PIDController)
  (if (not (find-package "MED_UAV_CONTROL"))
    (make-package "MED_UAV_CONTROL"))
  (shadow 'PIDController (find-package "MED_UAV_CONTROL")))
(unless (find-package "MED_UAV_CONTROL::PIDCONTROLLER")
  (make-package "MED_UAV_CONTROL::PIDCONTROLLER"))

(in-package "ROS")
;;//! \htmlinclude PIDController.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass med_uav_control::PIDController
  :super ros::object
  :slots (_header _ref _meas _P _I _D _U ))

(defmethod med_uav_control::PIDController
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:ref __ref) 0.0)
    ((:meas __meas) 0.0)
    ((:P __P) 0.0)
    ((:I __I) 0.0)
    ((:D __D) 0.0)
    ((:U __U) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _ref (float __ref))
   (setq _meas (float __meas))
   (setq _P (float __P))
   (setq _I (float __I))
   (setq _D (float __D))
   (setq _U (float __U))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:ref
   (&optional __ref)
   (if __ref (setq _ref __ref)) _ref)
  (:meas
   (&optional __meas)
   (if __meas (setq _meas __meas)) _meas)
  (:P
   (&optional __P)
   (if __P (setq _P __P)) _P)
  (:I
   (&optional __I)
   (if __I (setq _I __I)) _I)
  (:D
   (&optional __D)
   (if __D (setq _D __D)) _D)
  (:U
   (&optional __U)
   (if __U (setq _U __U)) _U)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _ref
    4
    ;; float32 _meas
    4
    ;; float32 _P
    4
    ;; float32 _I
    4
    ;; float32 _D
    4
    ;; float32 _U
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _ref
       (sys::poke _ref (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _meas
       (sys::poke _meas (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _P
       (sys::poke _P (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _I
       (sys::poke _I (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _D
       (sys::poke _D (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _U
       (sys::poke _U (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _ref
     (setq _ref (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _meas
     (setq _meas (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _P
     (setq _P (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _I
     (setq _I (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _D
     (setq _D (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _U
     (setq _U (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get med_uav_control::PIDController :md5sum-) "40c7eb50c8af809a4f7f350f7833a17f")
(setf (get med_uav_control::PIDController :datatype-) "med_uav_control/PIDController")
(setf (get med_uav_control::PIDController :definition-)
      "Header header

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

")



(provide :med_uav_control/PIDController "40c7eb50c8af809a4f7f350f7833a17f")


