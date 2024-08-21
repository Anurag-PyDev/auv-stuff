#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from msg import mydata

def Talker():
    pub = rospy.Publisher('chatter', mydata, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        hello_str = int(input("Enter number: "))
        msg=mydata()
        msg.a = hello_str
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()   

if __name__ =='__main__':
    try:
        Talker()
    except rospy.ROSInterruptException:
        pass

