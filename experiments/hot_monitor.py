#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import controller as ctrl

import rospy
from std_msgs.msg import String

monitor_time = 60. #sec

# Set Param
ctrl.output_loatt_current(config=True)
#ctrl.set_1st_lo(config=True)
ctrl.output_sis_voltage(config=True)
ctrl.output_hemt_voltage(config=True)

# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'hot_monitor_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5)
pub.publish(msg)


time.sleep(monitor_time)

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# Unset LO.
#ctrl.unset_1st_lo()
