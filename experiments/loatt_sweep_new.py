#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()


import rospy
import datetime

from std_msgs.msg import String
from std_msgs.msg import Int64

import os
import shutil
import glob

beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1l', '1r']

initial_current = 0  # mA
final_current = 5     # mA
step = 0.1             # mV
interval = 5e-2        # 50 msec.
fixtime = 3           # 0.5 sec.
roop = int((final_current - initial_current) / step)

# Set Chopper
chopper_wait = 5
ctrl.slider.set_step('z',0)

# Set Param
#ctrl.set_1st_lo(config=True)
ctrl.hemt.output_hemt_voltage_config('vd','vg1','vg2',config = None)
ctrl.sis.output_sis_voltage_config()

# Start Log.
msg_hot = String()
msg_hot.data = str(time.time())
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
    pub.publish(msg_hot)
    time.sleep(1e-3) # 1 msec
    
    for cur in range(roop+1):
        for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=cur*step)
        time.sleep(fixtime)

    pub.publish(f_msg)   # HOT finsh
    time.sleep(1)

    # COLD set
    ctrl.slider.set_step('z',250)
    time.sleep(chopper_wait)

    for _ in beam_list:
            ctrl.loatt.output_loatt_current(beam=_, current=0)
    time.sleep(fixtime)


    #COLD
    msg_cold = String()
    msg_cold.data = str(time.time())
    pub = rospy.Publisher(flag_name, String, queue_size=1)
    time.sleep(0.1)
    pub.publish(msg_cold)
    time.sleep(1e-3)
    
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

# chopper hot set
ctrl.slider.set_step('z',0)

# change data_name
exp_time_hot = datetime.datetime.fromtimestamp(float(msg_hot.data))
ymd = exp_time_hot.strftime('%Y%m%d_')
hms = exp_time_hot.strftime('%H%M%S')
hot_time = os.path.join(ymd +hms)

exp_time_cold = datetime.datetime.fromtimestamp(float(msg_cold.data))
ymd = exp_time_cold.strftime('%Y%m%d_')
hms = exp_time_cold.strftime('%H%M%S')
cold_time = os.path.join(ymd +hms)


hot_data = '/home/amigos/data/sql/loatt_sweep/{}/param.db'.format(hot_time)
cold_data = '/home/amigos/data/sql/loatt_sweep/{}/param.db'.format(cold_time)

os.rename(hot_data,'/home/amigos/data/sql/loatt_sweep/{}/hot_param.db'.format(hot_time))
os.rename(cold_data,'/home/amigos/data/sql/loatt_sweep/{}/cold_param.db'.format(cold_time))

# move data
shutil.move('/home/amigos/data/sql/loatt_sweep/{}/cold_param.db'.format(cold_time),'/home/amigos/data/sql/loatt_sweep/{}'.format(hot_time))

# remove cold_directory
shutil.rmtree('/home/amigos/data/sql/loatt_sweep/{}'.format(cold_time))
time.sleep(0.1)

# cp data_tool
data_path = '/home/amigos/data/sql/loatt_sweep/'
all_file = glob.glob(data_path + '*')
path = max(all_file, key=os.path.getctime)
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools/LoATT_plot_new.ipynb'
shutil.copy(plot_tool_path, path + '/loatt_plot.ipynb')




