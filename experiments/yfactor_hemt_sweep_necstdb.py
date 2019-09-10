#!/usr/bin/env python3


name = 'yfactor_hemt_sweep_necstdb'


import sys
import rospy
import time
import std_msgs.msg
import datetime

sys.path.append('/home/amigos/ros/src/nasco_system/scripts/')
import nasco_controller
import logger_controller
import jpynb_controller


rospy.init_node(name)

con = nasco_controller.controller(node=False)
logger = logger_controller.logger()
jpynb = jpynb_controller.jpynb()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name_hot = name + '/hot/' + date + '.necstdb'
dir_name_cold = name + '/cold/' + date + '.necstdb'
dir_name_jpynb = name + '/' + date


# set params.
hemt_list = con.beam_list[:8]

initial_voltage = -0.2 # mV
final_voltage   = 0.2  # mV
step            = 0.1  # mV
interval        = 0.1  # sec.
fixtime         = 0.1  # sec.
roop = int((final_voltage - initial_voltage) / step)


# initialize ( hot ).
print('[INFO] : Initializing for HOT... ')
# move hot
print('[INFO] : Movo chopper to HOT ...')
# con.??
time.sleep(1.)
for hemt in hemt_list:
    con.hemt.output_hemt_voltage(hemt, vd=1.2)
    con.hemt.output_hemt_voltage(hemt, vg1=initial_voltage)
    con.hemt.output_hemt_voltage(hemt, vg2=initial_voltage)
    time.sleep(1e-1) # 100 msec.

# measure hot.
print('[INFO] : Start to measure HOT with hemt ( vg1, vg2 ) sweep.')
logger.start(dir_name_hot)

for vg1 in range(roop + 1):
    [con.hemt.output_hemt_voltage(beam=hemt, vg1=vg1*step+initial_voltage) for hemt in hemt_list]
    time.sleep(0.1)
    for vg2 in range(roop + 1):
        [con.hemt.output_hemt_voltage(beam=hemt, vg2=vg2*step+initial_voltage) for hemt in hemt_list]
        time.sleep(fixtime)
time.sleep(1.)

print('[INFO] : Finish measure HOT with hemt ( vg1, vg2 ) sweep.')
logger.stop()

# move.
print('[INFO] : Move chopper from HOT to COLD...')
# con.??
time.sleep(1.)

# measure cold.
print('[INFO] : Start to measure COLD with hemt ( vg1, vg2 ) sweep.')
logger.start(dir_name_cold)
time.sleep(1.)

for vg1 in range(roop + 1):
    [con.hemt.output_hemt_voltage(beam=hemt, vg1=vg1*step+initial_voltage) for hemt in hemt_list]
    time.sleep(0.1)
    for vg2 in range(roop + 1):
        [con.hemt.output_hemt_voltage(beam=hemt, vg2=vg2*step+initial_voltage) for hemt in hemt_list]
        time.sleep(fixtime)
time.sleep(1.)

print('[INFO] : Finish measure COLD with hemt ( vg1, vg2 ) sweep.')
logger.stop()
time.sleep(1.)

# setup plot_tool.
jpynb.make(dir_name_jpynb)
time.sleep(1.)

# finalize.
print('[INFO] : Finalizing... ')
for hemt in hemt_list:
    con.hemt.output_hemt_voltage(hemt, vd=0.)
    con.hemt.output_hemt_voltage(hemt, vg1=0.)
    con.hemt.output_hemt_voltage(hemt, vg2=0.)
    time.sleep(1e-2) # 10 msec.
