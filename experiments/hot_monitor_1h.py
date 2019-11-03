#!/usr/bin/env python3

name = 'hot_monitor_1h'

import sys
import rospy

sys.path.append('/home/amigos/ros/src/nasco_system/scripts/')
import nasco_controller
import logger_controller
import time
import datetime
import std_msgs.msg

rospy.init_node(name)

con = nasco_controller.controller(node=False)
logger = logger_controller.logger()
date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name_hot = name  + date + '.necstdb'

logging_time = 3600. # sec.

#Hot
con.slider0.set_step('u', 0)
print('[INFO] : Hot')
time.sleep(2.)


logger.start(dir_name_hot)

time.sleep(logging_time)
logger.stop()

#Cold
con.slider0.set_step('u', 250)
print('[INFO] : Finish')
