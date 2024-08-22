#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String

def callback_func(msg:String):

    print(f"\nNew message Broadcasted : {msg.data}")
    

if __name__ == '__main__':
    node_name = input("Enter a node name : ")

    rospy.init_node(f"{node_name}")
    pub = rospy.Publisher("/channel", String, queue_size=10)
    lis = rospy.Subscriber('/channel', String, callback=callback_func)

    rate = rospy.Rate(10)
    while 1:
        temp = input()
        data = String(temp)
    
        pub.publish(data)
        print(f"Message sent to channel : {data.data}")
        rate.sleep()

    rospy.spin()