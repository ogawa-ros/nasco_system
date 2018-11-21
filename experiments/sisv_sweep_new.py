#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()

import nasco_controller_old
con = nasco_controller_old.controller()

import rospy
import datetime

from std_msgs.msg import String
from std_msgs.msg import Int64

import os
import shutil

beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = 6  # mV
final_voltage =  9     # mV
step = 0.5             # mV
interval = 5e-2        # 50 msec.
fixtime = 0.5           # 0.5 sec.
wait = 1.5
roop = int((final_voltage - initial_voltage) / step)

# Set Chopper
chopper_wait = 5.

# Set Param
ctrl.loatt.output_loatt_current_config()
#ctrl.set_1st_lo(config=True)
ctrl.hemt.output_hemt_voltage_config('vd','vg1','vg2',config = None)


# HOT set
con.slider.set_position('z',0)
time.sleep(chopper_wait)

# Start Log.
msg_hot = String()
msg_hot.data = str(time.time())
f_msg = String()
f_msg.data = ''
flag_name = 'sisv_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.

try:
    #HOT_initialize
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=initial_voltage)

    time.sleep(wait)

    pub.publish(msg_hot)
    time.sleep(1e-3)
    
    #HOT
    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.sis.output_sis_voltage(beam=_, voltage=vol*step+initial_voltage)
        time.sleep(fixtime)

    pub.publish(f_msg)
    time.sleep(1)

    con.slider.set_position('z',250)  #COLD_set
    time.sleep(chopper_wait)

    #COLD_initialize
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=initial_voltage)

    time.sleep(wait)
    
    #COLD
    msg_cold = String()
    msg_cold.data = str(time.time())
    pub = rospy.Publisher(flag_name, String, queue_size=1)
    time.sleep(1.5) # 1.5 sec.
    pub.publish(msg_cold)
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

# change data_name
exp_time_hot = datetime.datetime.fromtimestamp(float(msg_hot.data))
ymd = exp_time_hot.strftime('%Y%m%d_')
hms = exp_time_hot.strftime('%H%M%S')
hot_time = os.path.join(ymd +hms)

exp_time_cold = datetime.datetime.fromtimestamp(float(msg_cold.data))
ymd = exp_time_cold.strftime('%Y%m%d_')
hms = exp_time_cold.strftime('%H%M%S')
cold_time = os.path.join(ymd +hms)


hot_data = '~/data/sql/sisv_sweep/{}/param.db'.format(hot_time)
cold_data = '~/data/sql/sisv_sweep/{}/param.db'.format(cold_time)

os.rename(hot_data,'~/data/sql/sisv_sweep/{}/hot_param.db'.format(hot_time))
os.rename(cold_data,'~/data/sql/sisv_sweep/{}/cold_param.db'.format(cold_time))

# move data
shutil.move('~/data/sql/sisv_sweep/{}/cold_param.db'.format(cold_time),'~/data/sql/sisv_sweep/{}'.format(hot_time))

# remove cold_directory
shutl.rmtree('~/data/sql/sisv_sweep/{}'.format(cold_time))
time.sleep(0.1)

# cp data_tool
data_path = '/home/amigos/data/sql/sisv_sweep/'
all_file = glob.glob(data_path + '*')
path = max(all_file, key=os.path.getctime)
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools/sisv_sweep_3beam.ipynb'
shutil.copy(plot_tool_path, path + '/sisv_plot.ipynb')
