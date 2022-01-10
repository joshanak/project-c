
(cl:in-package :asdf)

(defsystem "med_uav_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "PIDController" :depends-on ("_package_PIDController"))
    (:file "_package_PIDController" :depends-on ("_package"))
  ))