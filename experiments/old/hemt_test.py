#!/usr/bin/env python3


import sys
import time
import qlook
#plotter = qlook.hemt_test_plot
import argparse
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import nasco_controller
ctrl = nasco_controller.controller()

import glob
import shutil
import os

import rospy
from std_msgs.msg import String


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r']

beam_num = 8

initial_voltage = -2.  # mV
final_voltage = 2.     # mV
step = 0.1              # mV
interval = 0.1          # sec.
roop = int((final_voltage - initial_voltage) / step)

# Initialize
for beam in beam_list:
    ctrl.hemt.output_hemt_voltage(beam, vd = 1.2)
    ctrl.hemt.output_hemt_voltage(beam, vg1 = initial_voltage)
    ctrl.hemt.output_hemt_voltage(beam, vg2 = initial_voltage)
    
    
time.sleep(3.0)

# Start Log.
msg = String()
msg.data = str(time.time()) # + lo
flag_name = 'hemt_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
pub1 = rospy.Publisher('logger_flag', String, queue_size=1)
time.sleep(1.5) # 1.5 sec.
pub.publish(msg)
pub1.publish(msg)
time.sleep(0.5)

try:
    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.hemt.output_hemt_voltage(beam=_, vd=1.2, vg1=vol*step+initial_voltage, vg2=vol*step+initial_voltage)
            
            time.sleep(1e-2) # 10 msec.
        time.sleep(5e-1)

except KeyboardInterrupt:
    for _ in beam_list:
        ctrl.hemt.output_hemt_voltage(beam=_, vd=0)
        ctrl.hemt.output_hemt_voltage(beam=_, vg1=0)
        ctrl.hemt.output_hemt_voltage(beam=_, vg2=0)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in beam_list:
    ctrl.hemt.output_hemt_voltage(beam=_, vd=0)
    ctrl.hemt.output_hemt_voltage(beam=_, vg1=0)
    ctrl.hemt.output_hemt_voltage(beam=_, vg2=0)
    time.sleep(5e-2) # 50 msec.

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)
pub1.publish(msg)

# cp data_tool
data_path = '/home/amigos/data/sql/hemt_sweep/'
all_file = glob.glob(data_path + '*')
path = max(all_file, key=os.path.getctime)
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools/hemt_test_plot.ipynb'
shutil.copy(plot_tool_path, path + '/hemt_test_plot.ipynb')

# qlook

#plotter.plot()
