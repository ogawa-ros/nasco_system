#!/usr/bin/env python3


import sys
import time
import qlook
plotter = qlook.sisiv_plot
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
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = -15.  # mV
final_voltage = 15.     # mV
step = 0.01              # mV
interval = 0.1          # sec.
roop = int((final_voltage - initial_voltage) / step)

# Set LO.
parser = argparse.ArgumentParser(description='SISIV Measurement with LOCAL.')
parser.add_argument('--lo', default='', help='>>> python sisiv_measure.py --lo 1')
args = parser.parse_args()
lo = args.lo

if lo == '1':
    lo = '-lo'
    ctrl.set_1st_lo(config=True)
else: pass

# Initialize
for beam in beam_list:
    ctrl.sis.output_sis_voltage(beam, initial_voltage)

# Start Log.
msg = String()
msg.data = str(time.time()) # + lo
flag_name = 'sisiv_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
pub1 = rospy.Publisher('logger_flag', String, queue_size=1)
time.sleep(1.5) # 1.5 sec.
pub.publish(msg)
pub1.publish(msg)
time.sleep(3.0)

try:
    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.sis.output_sis_voltage(beam=_, voltage=vol*step+initial_voltage)
            time.sleep(1e-2) # 10 msec.
       
except KeyboardInterrupt:
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=0)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in beam_list:
    ctrl.sis.output_sis_voltage(beam=_, voltage=0)
    time.sleep(5e-2) # 50 msec.

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)
pub1.publish(msg)
# Unset LO.
if lo == '1': ctrl.unset_1st_lo()

# cp data_tool
data_path = '/home/amigos/data/sql/sisiv/'
all_file = glob.glob(data_path + '*')
path = max(all_file, key=os.path.getctime)
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools/sisiv_plot.ipynb'
shutil.copy(plot_tool_path, path + '/sisiv_plot.ipynb')

# qlook
plotter.plot()
