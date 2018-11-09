#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64

beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1l', '1r']

initial_current = 0  # mA
final_current = 10     # mA
step = 0.1             # mV
interval = 5e-2        # 50 msec.
fixtime = 0.5           # 0.5 sec.
roop = int((final_current - initial_current) / step)

# Set Chopper
chopper_wait = 5
ctrl.slider.set_position('x',100)

# Set Param
#ctrl.set_1st_lo(config=True)
ctrl.hemt.output_hemt_voltage_config()
ctrl.sis.output_sis_voltage_config()

# Start Log.
msg = String()
msg.data = str(time.time())
f_msg = String()
f_msg.data = ''
flag_name = 'loatt_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.

try:
    #HOT_initialize
    for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=0)

    time.sleep(fixtime)

    #HOT
    pub.publish(msg)
    time.sleep(1e-3) # 1 msec
    
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=cur*step)
        time.sleep(fixtime)

    pub.publish(f_msg)   # HOT finsh
    time.sleep(1)

    # COLD set
    ctrl.slider.set_position('x',0)
    time.sleep(chopper_wait)

    for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=0)
    time.sleep(fixtime)


    #COLD
    msg = String()
    msg.data = str(time.time())
    pub = rospy.Publisher(flag_name, String, queue_size=1)
    pub.publish(msg)
    time.sleep(1)
    
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=cur*step)
        time.sleep(fixtime)

    pub.publish(f_msg)   #COLD finish
    time.sleep(1) 
    
except KeyboardInterrupt:
    pub.publish(f_msg)
    for _ in beam_list:
        ctrl.loatt.output_loatt_current(beam=_, current=0)

for _ in beam_list:
    ctrl.loatt.output_loatt_current(beam=_, current=0)
    time.sleep(interval)

# Finish Log.

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
