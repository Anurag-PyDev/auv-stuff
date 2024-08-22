#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def sub_callback(msg):
    print(f"Message recieved from t2 : {msg.data}")

def subscriber2():
    rospy.init_node('sub2')
    

    lis = rospy.Subscriber("/t2", String, callback=sub_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber2()
    except rospy.ROSInterruptException:
        pass