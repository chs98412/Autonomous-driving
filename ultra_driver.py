#!/usr/bin/env python

import rospy, math
from std_msgs.msg import Int32MultiArray

global a
a=()
def callback(msg):
    print(msg.data)

    global a
    a=msg.data
   

rospy.init_node('guide')
motor_pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)
ultra_sub = rospy.Subscriber('ultrasonic', Int32MultiArray, callback)

xycar_msg = Int32MultiArray()

while not rospy.is_shutdown():
    angle = 0
    if(len(a)>0):
        if(a[0]!=a[2]):
            if(a[0]-a[2] > 30): angle=-85
            elif(a[2] - a[0] >30): angle=85
    xycar_msg.data = [angle, 1000]
    motor_pub.publish(xycar_msg)
