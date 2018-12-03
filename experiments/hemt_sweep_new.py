import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()

import rospy
import datetime
import configparser

from std_msgs.msg import Int64
from std_msgs.msg import String

import os
import shutil
import glob

beam_list = ['2l','2r','3l','3r',
             '4l','4r','5l','5r']

interval = 5e-3
fixtime = 0.5
trigger_wait = 1.5
chopper_wait = 3.
vg1_wait = 1e-1 # 100 msec
wait = 1

# hemt_initial_param
#config_file = configparser.ConfigParser()
#config_file.read('/home/amigos/ros/src/nasco_system/configuration/')
#ini_vg1 = [float(config_file.get(beam,'vg1')) for beam in beam_list]
#ini_vg2 = [float(config_file.get(beam,'vg2')) for beam in beam_list]


# hemt_param
step = 0.1
#roop_vg1 = int() #
#roop_vg2 = int() #
[ctrl.hemt.output_hemt_voltage(beam=beam, vd=1.2) for beam in beam_list] # vd_initialize

# set_log
msg_hot = String()
f_msg = String()
f_msg.data = ''
flag_name = 'hemt_sweep_trigger'
pub = rospy.Publisher(flag_name, String , queue_size = 1)

# home position
con.slider.set_step('z', 250)
print('[INFO] cold position.')
time.sleep(chopper_wait)

# Set Param
ctrl.loatt.output_loatt_current_config()
ctrl.sis.output_sis_voltage_config()

try:
    
    # initialize
   # [ctrl.hemt.output_hemt_voltage(beam=beam, vg1=ini) for beam, ini in zip(beam_list, ini_vg1)] # vg1
    #[ctrl.hemt.output_hemt_voltage(beam=beam, vg2=ini) for beam, ini in zip(beam_list, ini_vg2)] # vg2
    #time.sleep(wait)
    

    # start logger
    msg_hot.data = str(time.time())
    pub.publish(msg_hot)
    time.sleep(trigger_wait)

    # HOT
    for vg1 in range(roop_vg1+1):
        [ctrl.hemt.output_hemt_voltage(beam=beam, vg1=vg1*step+ini) for beam, ini in zip(beam_list, ini_vg1)]
        time.sleep(vg1_wait)
        for vg2 in range(roop_vg2+1):
            [ctrl.hemt.output_hemt_voltage(beam=beam, vg2=vg2*step+ini) for beam, ini in zip(beam_list, ini_vg2)]
            time.sleep(fixtime)
    time.sleep(wait)

    # end logger
    pub.publish(f_msg)
    time.sleep(trigger_wait)

    # ---

    # initialize
    [ctrl.hemt.output_hemt_voltage(beam=beam, vg1=ini) for beam, ini in zip(beam_list, ini_vg1)] # vg1
    [ctrl.hemt.output_hemt_voltage(beam=beam, vg2=ini) for beam, ini in zip(beam_list, ini_vg2)] # vg2
    time.sleep(wait)
    
    # set cold
    con.slider.set_position('z', 250)
    print('[INFO] cold position.')    
    time.sleep(chopper_wait)

    # start logger
    msg_cold.data = str(time.time())
    pub.publish(msg_cold)
    time.sleep(trigger_wait)

    # COLD
    for vg1 in range(roop_vg1+1):
        [ctrl.hemt.output_hemt_voltage(beam=beam, vg1=vg1*step+ini) for beam, ini in zip(beam_list, ini_vg1)]
        time.sleep(vg1_wait)
        for vg2 in range(roop_vg2+1):
            [ctrl.hemt.output_hemt_voltage(beam=beam, vg2=vg2*step+ini) for beam, ini in zip(beam_list, ini_vg2)]
            time.sleep(fixtime)
    
    # end logger
    pub.publish(f_msg)
    time.sleep(trigger_wait)
        
except KeyboardInterrupt:
    pub.publish(f_msg)
    [ctrl.hemt.output_hemt_voltage(beam=beam, vd=0, vg1=0, vg2=0) for beam in beam_list]
    
# finalize
[ctrl.hemt.output_hemt_voltage(beam=beam, vd=0, vg1=0, vg2=0) for beam in beam_list]

# change data_name
exp_time_hot = datetime.datetime.fromtimestamp(float(msg_hot.data))
ymd = exp_time_hot.strftime('%Y%m%d_')
hms = exp_time_hot.strftime('%H%M%S')
hot_time = os.path.join(ymd +hms)

exp_time_cold = datetime.datetime.fromtimestamp(float(msg_cold.data))
ymd = exp_time_cold.strftime('%Y%m%d_')
hms = exp_time_cold.strftime('%H%M%S')
cold_time = os.path.join(ymd +hms)


hot_data = '/home/amigos/data/sql/hemt_sweep/{}/param.db'.format(hot_time)
cold_data = '/home/amigos/data/sql/hemt_sweep/{}/param.db'.format(cold_time)

os.rename(hot_data,'/home/amigos/data/sql/hemt_sweep/{}/hot_param.db'.format(hot_time))
os.rename(cold_data,'/home/amigos/data/sql/hemt_sweep/{}/cold_param.db'.format(cold_time))

# move data
shutil.move('/home/amigos/data/sql/hemt_sweep/{}/cold_param.db'.format(cold_time),'/home/amigos/data/sql/hemt_sweep/{}'.format(hot_time))

# remove cold_directory
shutl.rmtree('/home/amigos/data/sql/hemt_sweep/{}'.format(cold_time))
time.sleep(0.1)

# cp data_tool
data_path = '/home/amigos/data/sql/hemt_sweep/'
all_file = glob.glob(data_path + '*')
path = max(all_file, key=os.path.getctime)
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools/hemt_sweep_3beam.ipynb'
shutil.copy(plot_tool_path, path + '/hemt_plot.ipynb')
