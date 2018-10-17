#!/usr/bin/env python3

import sys
import time

import rospy
import std_msgs.msg

rospy.init_node("switch_controller")

args = sys.argv

def switch_control(command):
    pub = rospy.Publisher(
         name = "switch_level_cmd",
         data_class = std_msgs.msg.String,
	 latch = True,
	 queue_size = 1
	 )

    pub.publish(command)
    time.sleep(0.1)
    return

if str(args[1]) == "SMART" or str(args[1]) == "NASCO":
    switch_control(str(args[1]))
    print("COMMAND PUBLISHED")
else:
    print("COMMAND ERROR")
    print("Please input 'SMART' or 'NASCO'")
