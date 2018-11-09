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
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = 7  # mV
final_voltage =  9     # mV
step = 0.05             # mV
#step = 0.3            # for gpib
interval = 5e-2        # 50 msec.
fixtime = 0.5           # 0.5 sec.
#fixtime = 5.           # for gpib
roop = int((final_voltage - initial_voltage) / step)

# Set Chopper
chopper_wait = 5.
ctrl.slider.set_position('x', 100)
time.sleep(chopper_wait)

# Set Param
ctrl.loatt.output_loatt_current_config()
#ctrl.set_1st_lo(config=True)
ctrl.hemt.output_hemt_voltage_config()

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

try:
    #HOT_initialize
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=initial_voltage)

    time.sleep(fixtime)

    pub.publish(msg)
    time.sleep(1e-3)
    
    #HOT
    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.sis.output_sis_voltage(beam=_, voltage=vol*step+initial_voltage)
        time.sleep(fixtime)

    pub.publish(f_msg)
    time.sleep(1)

    ctrl.slider.set_position('x',0)  #COLD_set
    time.sleep(chopper_wait)

    #COLD_initialize
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=initial_voltage)

    time.sleep(1)
    
    #COLD
    msg = String()
    msg.data = str(time.time())
    pub = rospy.Publisher(flag_name, String, queue_size=1)
    time.sleep(1.5) # 1.5 sec.
    pub.publish(msg)
    time.sleep(1e-3)

    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.sis.output_sis_voltage(beam=_, voltage=vol*step+initial_voltage)
        time.sleep(fixtime)
    time.sleep(fixtime)

    pub.publish(f_msg)
    
except KeyboardInterrupt:
    pub.publish(f_msg)
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=0)



    
for _ in beam_list:
    ctrl.sis.output_sis_voltage(beam=_, voltage=0)
    time.sleep(interval)

#pub_mc.publish(250)

# Finish Log.

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
