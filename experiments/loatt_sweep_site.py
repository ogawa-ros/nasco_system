#!/usr/bin/env python3

name = 'loatt_sweep_test'

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()
import logger_controller
import jpynb_controller
import datetime


import rospy
import datetime

from std_msgs.msg import String
from std_msgs.msg import Int64

import os
import shutil
import glob

logger = logger_controller.logger()
jpynb = jpynb_controller.jpynb()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name_hot = name + '/' + date + '.necstdb'
dir_name_jpynb = name + '/' + date + '.necstdb'


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r']


initial_current = 0  # mA
final_current = 5     # mA
step = 0.1             # mV
interval = 5e-2        # 50 msec.
fixtime = 3           # 0.5 sec.
roop = int((final_current - initial_current) / step)

# Set Chopper
#chopper_wait = 5
#ctrl.slider.set_step('z',0)

# Set Param
#ctrl.set_1st_lo(config=True)
ctrl.hemt.output_hemt_voltage_config('vd','vg1','vg2',config = None)
ctrl.sis.output_sis_voltage_config()

# Start Log.
#msg_hot = String()
#msg_hot.data = str(time.time())
#f_msg = String()
#f_msg.data = ''
#flag_name = 'loatt_sweep_trigger'
#pub = rospy.Publisher(flag_name, String, queue_size=1)
#time.sleep(1.5) # 1.5 sec.

try:
    #HOT_initialize
    for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=0)

    time.sleep(fixtime)

    #HOT
    #pub.publish(msg_hot)
    logger.start(dir_name_hot)
    time.sleep(1e-3) # 1 msec
    
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=cur*step)
        time.sleep(fixtime)

    #pub.publish(f_msg)   # HOT finsh
    logger.stop()
    time.sleep(1)

    # setup plot_tool.
    jpynb.make(dir_name_jpynb)
    time.sleep(1.)

              
    
except KeyboardInterrupt:
    pub.publish(f_msg)
    for _ in beam_list:
        ctrl.loatt.output_loatt_current(beam=_, current=0)

for _ in beam_list:
    ctrl.loatt.output_loatt_current(beam=_, current=0)
    time.sleep(interval)






