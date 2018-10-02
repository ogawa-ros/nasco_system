#!/usr/bin/env python3


import sys
import time
sys.path.append('/home/necst/ros/src/nasco_system/scripts')
import sis_vol_controller as ctrl

import rospy
from std_msgs.msg import String


sis_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

beam_num = 12
initial_voltage = -7  # mV
final_voltage = 7     # mV
step = 0.1            # mV
interval = 0.1        # sec.
roop = int((final_voltage - initial_voltage) / step)

msg = String()
msg.data = str(time.time())
pub = rospy.Publisher('log_triger', String, queue_size=1)
time.sleep(3e-1) # 300 msec.
pub.publish(msg)


try:
    for vol in range(roop+1):
        for _ in sis_list:
            ctrl.output_voltage(sis=_, voltage=vol*step-final_voltage)
            time.sleep(1e-2) # 10 msec.
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

msg = String()
msg.data = ''
pub.publish(msg)
