#!/usr/bin/env python3


name = 'yfactor_necstdb'


import sys
import rospy
import time
import std_msgs.msg
import datetime

import nasco_controller


rospy.init_node(name)
con = nasco_controller.controller(node=False)
logger = logger_controller.logger()
jpynb = jpynb_controller.jpynb()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name_hot = name + '/hot/' + date + '.necstdb'
dir_name_cold = name + '/cold/' + date + '.necstdb'
dir_name_jpynb = name + '/' + date


# measure hot.
print('info : start to measure hot')
logger.start(dir_name_hot)
time.sleep(5.)
logger.stop()
print('info : Saved to amigos@172.20.0.11:/media/usbdisk/data/rx/{}'.format(dir_name_hot))

# move
print('info : movo chopper from hot to cold...')
con.??
time.sleep(3.)

# measure cold.
print('info : start to measure cold')
logger.start(dir_name_cold)
time.sleep(5.)
logger.stop()
print('info : Saved to amigos@172.20.0.11:/media/usbdisk/data/rx/{}'.format(dir_name_cold))

# setup plot_tool
jpynb.make(dir_name_jpynb)
time.sleep(1.)
print('info : Setup plot_tool to amigos@172.20.0.20:/home/amigos/analysis/rx/{}'.format(dir_name_jpynb)

