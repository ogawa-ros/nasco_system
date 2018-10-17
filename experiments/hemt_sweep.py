#!/usr/bin/env python3


import sys
import time
sys.path.append('/home/necst/ros/src/nasco_system/scripts')
import controller as ctrl

import rospy
from std_msgs.msg import String


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r']

initial_voltage = -2  # mV
final_voltage = 2     # mV
step = 0.1             # mV
interval = 5e-3        # 5 msec.
fixtime = 1.           # 1 sec.
roop_vg1 = int((final_voltage - initial_voltage) / step)
roop_vg2 = int((final_voltage - initial_voltage) / step)

# Start Chopper


# Set Param
ctrl.output_loatt_current(config=True)
#ctrl.set_1st_lo(config=True)
ctrl.output_sis_voltage(config=True)

# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'hemt_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5)
pub.publish(msg)

try:
    for vol1 in range(roop_vg1 + 1):
        for vol2 in range(roop_vg2 + 1):
            for _ in beam_list:
                ctrl.output_hemt_voltage(beam = _, vd = 1.2, vg1 = vol1*step+initial_voltage, vg2 = vol2*step+initial_voltage)
            time.sleep(interval)
        time.sleep(fixtime)

except KeyboardInterrupt:
    for _ in beam_list:
        ctrl.output_hemt_voltage(beam = _, vd =0, vg1 = 0, vg2 = 0)
        time.sleep(interval)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in beam_list:
    ctrl.output_hemt_voltage(beam = _, vd =0, vg1 = 0, vg2 = 0)
    time.sleep(interval)

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# Stop Chopper

# Unset LO.
#ctrl.unset_1st_lo()
