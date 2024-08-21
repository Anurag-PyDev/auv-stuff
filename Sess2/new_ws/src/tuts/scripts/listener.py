#!/usr/bin/env python3

import rospy
# from std_msgs.msg import String
from tuts.msg import Num

def callback(data):
    rospy.loginfo(f'Number entered is {data.num}')

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Num, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
