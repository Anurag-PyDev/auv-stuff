#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String

def publisher2():
    rospy.init_node('pub2')
    pub = rospy.Publisher('/t2', String, queue_size=10)

    rate = rospy.Rate(10)
    while 1:
        temp = input("Enter your message for t2 : ")
        data = String(temp)
    
        pub.publish(data)
        print(f"Published to t2 : {data}")
        rate.sleep()
    
if __name__ == '__main__':
    try:
        publisher2()
    except rospy.ROSInterruptException:
        pass
