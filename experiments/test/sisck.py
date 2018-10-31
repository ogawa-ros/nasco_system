#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()

import rospy
from std_msgs.msg import String

beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']

beam_num = 12

initial_voltage = -10. # mV
final_voltage = 10     # mV
step = 0.1             # mV
interval = 5e-3        # 5 msec.
roop = int((final_voltage - initial_voltage) / step)

for beam in beam_list:
    ctrl.sis.output_sis_voltage(beam=beam, voltage=initial_voltage)
    time.sleep(1e-2) # 10 msec.

# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'sisv_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(3e-2) # 30 msec.
pub.publish(msg)

try:
    for vol in range(roop + 1):
        for beam in beam_list:
            ctrl.sis.output_sis_voltage(beam=beam, voltage=vol*step+initial_voltage)
            time.sleep(1e-2) # 10 msec.
except KeyboardInterrupt:
    for beam in beam_list:
        ctrl.sis.output_sis_voltage(beam=beam, voltage=0.)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for beam in beam_list:
    ctrl.sis.output_sis_voltage(beam=beam, voltage=0)
    time.sleep(5e-2) # 50 msec.

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)
