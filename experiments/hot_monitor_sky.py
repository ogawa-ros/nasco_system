#!/usr/bin/env python3

name = 'hot_monitor_sky'

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

logging_time = int(sys.argv[1]) # sec.

#sky
con.slider0.set_step('u', 250)
print('[INFO] : Sky')
time.sleep(2.)


logger.start(dir_name_hot)

time.sleep(logging_time)
logger.stop()

#Cold
con.slider0.set_step('u', 250)
print('[INFO] : Finish')
