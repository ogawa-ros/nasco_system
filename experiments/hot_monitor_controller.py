#!/usr/bin/env python3

import os
import sys
import time
import glob
import shutil
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import controller
con = controller

import rospy
from std_msgs.msg import String

monitor_time = 10 * 60  #  10 minute

# Set Param
# ctrl.output_loatt_current(config=True)
# ctrl.set_1st_lo(config=True)
# ctrl.output_sis_voltage(config=True)
# ctrl.output_hemt_voltage(config=True)

# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'hot_monitor_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(5e-1) # 500 msec.
pub.publish(msg)

time.sleep(monitor_time)

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# cp plot_tool
data_path = '/home/amigos/data/experiments/logger/hot_monitor/'
all_file = glob.glob(data_path + '*')
path = max(all_file, key=os.path.getctime)
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools/hot_monitor_2beam.ipynb'
shutil.copy(plot_tool_path, path + '/hot_monitor.ipynb')

# Unset LO.
#ctrl.unset_1st_lo()
print(path)
print('fin.')
