#!/usr/bin/env python3


name = 'sisiv_necstdb'


import sys
import rospy
import time
import std_msgs.msg
import datetime

sys.path.append('/home/amigos/ros/src/nasco_system/scripts/')
import nasco_controller
import logger_controller
import jpynb_controller


rospy.init_node(name)

con = nasco_controller.controller(node=False)
logger = logger_controller.logger()
jpynb = jpynb_controller.jpynb()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name_hot = name + date + '.necstdb'
dir_name_jpynb = name + '/' + date


# measure hot.
print('[INFO] : Start to measure HOT.')
logger.start(dir_name_hot)
time.sleep(1.)
logger.stop()

# move
print('[INFO] : Movo chopper from HOT to COLD...')
# con.??
time.sleep(1.)

# measure cold.
print('[INFO] : Start to measure COLD.')
logger.start(dir_name_cold)
time.sleep(1.)

# setup plot_tool
jpynb.make(dir_name_jpynb)
time.sleep(1.)

