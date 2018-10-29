#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import controller as ctrl
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
fixtime = 3           # 3 sec.
roop = int((final_current - initial_current) / step)

# Set Chopper

#cf = (90/36)*100  #degree conversion
#mc_msg = Int64
#mc_msg.data = cf
pub_mc = rospy.Publisher('/cpz7415v_rsw0_z_position_cmd' , Int64 , queue_size = 1)
chopper_wait = 10
# Set Param
#ctrl.set_1st_lo(config=True)
ctrl.output_hemt_voltage(config = True)
#ctrl.output_sis_voltage(config = True)

# Start Log.
msg = String()
msg.data = str(time.time())
f_msg = String()
f_msg.data = ''
flag_name = 'loatt_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.

try:
    #HOT
    pub.publish(msg)
    time.sleep(1e-3) # 1 msec
    
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.output_loatt_current(beam=_, current=cur*step)
        time.sleep(fixtime)

    pub.publish(f_msg)   # HOT finsh
    time.sleep(1)

    pub_mc.publish(250)   # COLD set
    time.sleep(chopper_wait)

    for _ in beam_list:
            ctrl.output_loatt_current(beam=_, current=0)
    time.sleep(fixtime)


    #COLD
    msg = String()
    msg.data = str(time.time())
    pub = rospy.Publisher(flag_name, String, queue_size=1)
    pub.publish(msg)
    time.sleep(1)
    
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.output_loatt_current(beam=_, current=cur*step)
        time.sleep(fixtime)

    pub.publish(f_msg)   #COLD finish
    time.sleep(1)
    
    pub_mc.publish(250) 
    
except KeyboardInterrupt:
    pub.publish(f_msg)
    for _ in beam_list:
        ctrl.output_loatt_current(beam=_, current=0)

for _ in beam_list:
    ctrl.output_loatt_current(beam=_, current=0)
    time.sleep(interval)

# Finish Log.

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
