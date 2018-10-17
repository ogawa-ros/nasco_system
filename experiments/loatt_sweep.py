#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/necst/ros/src/nasco_system/scripts')
import controller as ctrl

import rospy
from std_msgs.msg import String


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1l', '1r']

initial_current = 0  # mA
final_current = 10     # mA
step = 0.1             # mV
interval = 5e-3        # 5 msec.
fixtime = 3           # 1 sec.
roop = int((final_current - initial_current) / step)

# Start Chopper


# Set Param
#ctrl.set_1st_lo(config=True)
ctrl.output_hemt_voltage(config=True)
ctrl.output_sis_voltage(config = True)

# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'loatt_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.
pub.publish(msg)

try:
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.output_loatt_current(beam=_, current=cur*step)
            time.sleep(interval)
        time.sleep(fixtime)
except KeyboardInterrupt:
    for _ in beam_list:
        ctrl.output_loatt_current(beam=_, current=0)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in beam_list:
    ctrl.output_loatt_current(beam=_, current=0)
    time.sleep(interval)

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
