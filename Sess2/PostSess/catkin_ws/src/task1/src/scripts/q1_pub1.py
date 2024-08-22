#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String

def publisher1():
    rospy.init_node('pub1')
    pub = rospy.Publisher('/t1', String, queue_size=10)

    rate = rospy.Rate(10)
    while 1:
        temp = input("Enter your message for t1 : ")
        data = String(temp)
    
        pub.publish(data)
        print(f"Published to t1 : {data}")
        rate.sleep()
    
if __name__ == '__main__':
    try:
        publisher1()
    except rospy.ROSInterruptException:
        pass

	
