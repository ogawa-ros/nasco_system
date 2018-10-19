#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import controller as ctrl

import rospy
from std_msgs.msg import String


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = 7  # mV
final_voltage =  9     # mV
step = 0.1             # mV
interval = 5e-3        # 5 msec.
fixtime = 1.           # 1 sec.
#fixtime = 3.           # for gpib
roop = int((final_voltage - initial_voltage) / step)

# Start Chopper


# Set Param
ctrl.output_loatt_current(config=True)
#ctrl.set_1st_lo(config=True)
ctrl.output_hemt_voltage(config=True)

time.sleep(3)


# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'sisv_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.
pub.publish('')
time.sleep(3.0)
pub.publish(msg)
time.sleep(1.5)

try:
    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.output_sis_voltage(sis=_, voltage=vol*step+initial_voltage)
            time.sleep(interval)
        time.sleep(fixtime)
except KeyboardInterrupt:
    for _ in beam_list:
        ctrl.outpu_sis_voltage(sis=_, voltage=0)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in beam_list:
    ctrl.output_sis_voltage(sis=_, voltage=0)
    time.sleep(interval)

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
