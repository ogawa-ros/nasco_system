#!/usr/bin/env python3


import sys
import time
sys.path.append('/home/necst/ros/src/nasco_system/scripts')
import controller as ctrl
# import sis_vol_controller as ctrl

import rospy
from std_msgs.msg import String


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = -10  # mV
final_voltage = 10     # mV
step = 0.1             # mV
interval = 1           # sec.
roop = int((final_voltage - initial_voltage) / step)

# Start Chopper
# 

# Set Param
ctrl.output_loatt_current(config=True)
ctrl.set_1st_lo(config=True)
ctrl.output_hemt_voltage(config=True)

# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'yfac_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1) # 1 sec.
pub.publish(msg)

try:
    for vol in range(roop+1):
        for _ in sis_list:
            ctrl.output_voltage(sis=_, voltage=vol*step-final_voltage)
            time.sleep(interval)
except KeyboardInterrupt:
    for _ in sis_list:
        ctrl.output_voltage(sis=_, voltage=0)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in sis_list:
    ctrl.output_voltage(sis=_, voltage=0)
    time.sleep(5e-2) # 50 msec.

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# Unset LO.
ctrl.unset_1st_lo()
