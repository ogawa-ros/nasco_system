#!/usr/bin/env python3


name = 'yfactor_sisv_sweep_necstdb'


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
beam_list = con.beam_list

initial_voltage = 7.0 # mV
final_voltage   = 9.0 # mV
step            = 0.1 # mV
interval        = 0.1 # sec.
fixtime         = 0.1 # sec.
roop = int((final_voltage - initial_voltage) / step)


# initialize ( hot ).
print('[INFO] : Initializing for hot... ')
# move hot
print('[INFO] : Movo chopper to HOT ...')
# con.??
time.sleep(1.)
for beam in beam_list:
    con.sis.output_sis_voltage(beam, initial_voltage)
    time.sleep(1e-2) # 10 msec.

# measure hot.
print('[INFO] : Start to measure hot with sisv sweep.')
logger.start(dir_name_hot)

for vol in range(roop + 1):
    for beam in beam_list:
        con.sis.output_sis_voltage(beam=beam, voltage=vol*step+initial_voltage)
        time.sleep(1e-2) # 10 msec.
    time.sleep(fixtime)

print('[INFO] : Finish measure hot with sisv sweep')
logger.stop()

# move.
print('[INFO] : Movo chopper from HOT to COLD...')
# con.??
time.sleep(1.)

# measure cold.
print('[INFO] : Start to measure cold with sisv sweep.')
logger.start(dir_name_cold)
time.sleep(1.)

for vol in range(roop + 1):
    for beam in beam_list:
        con.sis.output_sis_voltage(beam=beam, voltage=vol*step+initial_voltage)
        time.sleep(1e-2) # 10 msec.
    time.sleep(fixtime)

print('[INFO] : Finish measure cold with sisv sweep')
logger.stop()
time.sleep(1.)

# setup plot_tool.
jpynb.make(dir_name_jpynb)
time.sleep(1.)

# finalize.
print('[INFO] : Finalizing... ')
for beam in beam_list:
    con.sis.output_sis_voltage(beam, 0.)
    time.sleep(1e-2) # 10 msec.
