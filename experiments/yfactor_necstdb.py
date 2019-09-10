#!/usr/bin/env python3


name = 'yfactor_necstdb'


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
dir_name_hot = name + '/hot/' + date + '.necstdb'
dir_name_cold = name + '/cold/' + date + '.necstdb'
dir_name_jpynb = name + '/' + date

# initialize
print('[INFO] : initialize...')
# set bias point...??

# measure hot.
print('[INFO] : Start to measure HOT.')
logger.start(dir_name_hot)
time.sleep(1.)
logger.stop()

# move. ( hot --> cold )
print('[INFO] : Movo chopper from HOT to COLD...')
# con.??
time.sleep(1.)

# measure cold.
print('[INFO] : Start to measure COLD.')
logger.start(dir_name_cold)
time.sleep(1.)

# setup plot_tool.
jpynb.make(dir_name_jpynb)
time.sleep(1.)

# finalize.
print('[INFO] : finalize...')
print('[INFO] : Movo chopper from COLD to HOT...')
# con.??
time.sleep(1.)
