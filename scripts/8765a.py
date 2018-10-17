#!/usr/bin/env python3

import threading
import rospy
import std_msgs.msg

import NASCORX_System.device.A11713C as A11713C

name = "switch_8765a"

class A8765(object):

    def __init__(self, ip, port, ch = '1X'):
        self.pa = A11713C.a11713c(ip, port)
        self.ch = ch

        self.pub_level = rospy.Publisher(
	        name = '/8765a_level',
		data_class = std_msgs.msg.Bool,
		latch = True,
		queue_size = 1
		)

        self.pub_vol = rospy.Publisher(
	        name = '/8765a_voltage',
		data_class = std_msgs.msg.String,
		latch = True,
		queue_size = 1
		)

        self.sub_level = rospy.Subscriber(
	        name = '/8765a_level_cmd',
		data_class = std_msgs.msg.Bool,
		callback = self.callback_level,
		queue_size = 1,
		)

        self.sub_vol = rospy.Subscriber(
	        name = '/8765a_voltage_cmd',
		data_class = std_msgs.msg.String,
		callback = self.callback_vol,
		queue_size = 1,
		)

        self.pub_function_level()
        self.pub_function_vol()
        pass

    def callback_level(self, status):
        self.cmd = status.data

        if self.cmd == True: # NASCO
            self.pa.set_level(level = 1, ch = self.ch)
        elif self.cmd == False: # SMART
            self.pa.set_level(level = 0, ch = self.ch)
        self.pub_function_level()
        return

    def callback_vol(self, status):
        self.pa.set_voltage(status.data, bank=1)
        self.pub_function_vol()
        return

    def pub_function_level(self):
        mode = self.pa.query_level()
        self.pub_level.publish(mode[0])
        return

    def pub_function_vol(self):
        mode = self.pa.query_voltage()
        self.pub_vol.publish(mode[0])
        return


if __name__ == "__main__":
    rospy.init_node(name)
    switch = A8765(ip = '192.168.100.114', port = 5025)

    rospy.spin()
