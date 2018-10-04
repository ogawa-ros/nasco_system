#!/usr/bin/env python3


import sys
import time
sys.path.append('/home/necst/ros/src/nasco_system/scripts')
import sis_vol_controller as ctrl

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Int32


sis_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

beam_num = 12
initial_voltage = -10  # mV
final_voltage = 10     # mV
step = 0.1            # mV
interval = 0.1        # sec.
roop = int((final_voltage - initial_voltage) / step)

msg = String()
msg.data = str(time.time())
pub = rospy.Publisher('log_triger', String, queue_size=1)
time.sleep(1) # 1 sec.
pub.publish(msg)


# LO
pub_lo = [rospy.Publisher('/lo_1st_freq_cmd', Float64, queue_size=1),
          rospy.Publisher('/lo_1st_power_cmd', Float64, queue_size=1),
          rospy.Publisher('/lo_1st_onoff_cmd', Int32, queue_size=1)]
time.sleep(5e-1)
freq, power, onoff = Float64(), Float64(), Int32()
freq.data, power.data, onoff.data = 17.5, 0., 1
pub_lo[0].publish(freq)
time.sleep(interval)
pub_lo[1].publish(power)
time.sleep(interval)
pub_lo[2].publish(onoff)
time.sleep(interval)
for i in range(1, 17):
    power = Float64()
    power.data = float(i)
    pub_lo[1].publish(power)
    time.sleep(1)
power = Float64()
power.data = 17.3
pub_lo[1].publish(power)

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

freq, power, onoff = Float64(), Float64(), Int32
freq.data, power.data, onoff.data = 0., 0., 0
pub_lo[0].publish(freq)
time.sleep(interval)
pub_lo[1].publish(power)
time.sleep(interval)
pub_lo[2].publish(onoff)
