#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def pose_callback(msg):
    print(f"Message recieved from t1 : {msg.data}")

def subscriber1():
    rospy.init_node('sub1')
    

    lis = rospy.Subscriber("/t1", String, callback=pose_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber1()
    except rospy.ROSInterruptException:
        pass