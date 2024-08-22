#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String

def callback_func(msg:String):

    print(f"{msg.data}")
    

if __name__ == '__main__':

    rospy.init_node("jolyne")
    pub = rospy.Publisher("/chat", String, queue_size=10)
    lis = rospy.Subscriber('/chat', String, callback=callback_func)

    rate = rospy.Rate(10)
    while 1:
        temp = input()
        # print(f"Me : {temp}")
        temp = "Jolyne : " + temp
        data = String(temp)
        lis.unregister()
        pub.publish(data)
        lis = rospy.Subscriber('/chat', String, callback=callback_func)
        rate.sleep()

    rospy.spin()
