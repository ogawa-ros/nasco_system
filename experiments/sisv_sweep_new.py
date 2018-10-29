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
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = 7  # mV
final_voltage =  9     # mV
step = 0.1             # mV
#step = 0.3            # for gpib
interval = 5e-2        # 50 msec.
fixtime = 3.           # 3 sec.
#fixtime = 5.           # for gpib
roop = int((final_voltage - initial_voltage) / step)

# Set Chopper

#cf = (90/36)*100   #degree conversion
#mc_msg = Int64
#mc_msg.data = cf
pub_mc = rospy.Publisher('/cpz7415v_rsw0_z_position_cmd', Int64 , queue_size = 1)
chopper_wait = 10.

# Set Param
#ctrl.output_loatt_current(config=True)
#ctrl.set_1st_lo(config=True)
ctrl.output_hemt_voltage(config=True)

time.sleep(3)


# Start Log.
msg = String()
msg.data = str(time.time())
f_msg = String()
f_msg.data = ''
flag_name = 'sisv_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.
#pub.publish('')
time.sleep(3.0)

try:
    #HOT
    for _ in beam_list:
        ctrl.output_sis_voltage(sis=_, voltage=initial_voltage)

    time.sleep(1)

    pub.publish(msg)
    time.sleep(1e-3)

    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.output_sis_voltage(sis=_, voltage=vol*step+initial_voltage)
        time.sleep(fixtime)

    pub.publish(f_msg)
    time.sleep(10)

    pub_mc.publish(250)
    time.sleep(chopper_wait)

    for _ in beam_list:
        ctrl.output_sis_voltage(sis=_, voltage=initial_voltage)

    time.sleep(1)
    
    #COLD
    msg = String()
    msg.data = str(time.time())
    pub = rospy.Publisher(flag_name, String, queue_size=1)
    time.sleep(1.5) # 1.5 sec.
    pub.publish(msg)
    time.sleep(1)

    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.output_sis_voltage(sis=_, voltage=vol*step+initial_voltage)
        time.sleep(fixtime)
    time.sleep(fixtime)

    pub.publish(f_msg)
    
except KeyboardInterrupt:
    pub.publish(f_msg)
    for _ in beam_list:
        ctrl.outpu_sis_voltage(sis=_, voltage=0)



    
for _ in beam_list:
    ctrl.output_sis_voltage(sis=_, voltage=0)
    time.sleep(interval)

pub_mc.publish(250)

# Finish Log.

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
