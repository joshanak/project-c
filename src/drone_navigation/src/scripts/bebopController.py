#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Vector3
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

class BebopController:    
    def __init__(self):
        self.positionPublisher = rospy.Publisher("/bebop/pos_ref", Vector3, queue_size = 1)
        rospy.Subscriber("/bebop/pose", PoseStamped, self.bebopPositionCallback)
        rospy.Subscriber("/odom", Odometry, self.robotPositionCallback)

        self.bebopPosition = PoseStamped()
        self.robotPosition = Odometry()

        self.firstPass = True


    def robotPositionCallback(self, data):
        self.robotPosition = data

    def bebopPositionCallback(self, data):
        self.bebopPosition = data

    def fetchPose(self):
        self.x = self.bebopPosition.pose.position.x
        self.y = self.bebopPosition.pose.position.y
        self.z = self.bebopPosition.pose.position.z

    def run(self):
        rate = rospy.Rate(100)

        if self.firstPass:
            self.fetchPose()
            self.firstPass = False

        while not rospy.is_shutdown():
            rate.sleep()

            self.x = self.robotPosition.pose.pose.position.x
            self.y = self.robotPosition.pose.pose.position.y
            self.z = 0.05

            print("X: {}\nY: {}\nZ: {}".format(self.x, self.y, self.z))

            self.positionPublisher.publish(self.x, self.y, self.z)

if __name__ == '__main__':
    rospy.init_node('rviz2bebop')

    try:
        bC = BebopController()
        bC.run()
    except rospy.ROSInterruptException: 
        rospy.signal_shutdown(0)