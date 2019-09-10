#!/usr/bin/env python3


name = 'sisiv_necstdb'


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
dir_name = name + date + '.necstdb'
dir_name_jpynb = name + '/' + date

# set params.
beam_list = con.beam_list

initial_voltage = -10.  # mV
final_voltage = 10.     # mV
step = 0.1              # mV
interval = 0.1          # sec.
roop = int((final_voltage - initial_voltage) / step)


# initialize.
print('[INFO] : Initializing... ')
for beam in beam_list:
    con.sis.output_sis_voltage(beam, initial_voltage)
    time.sleep(1e-2) # 10 msec.

# measure sisiv.
print('[INFO] : Start to measure sisiv.')
logger.start(dir_name)

for vol in range(roop + 1):
    for beam in beam_list:
        con.sis.output_sis_voltage(beam=beam, voltage=vol*step+initial_voltage)
        time.sleep(1e-2) # 10 msec.

print('[INFO] : Finish measure sisiv')
logger.stop()

# finalize.
print('[INFO] : Finalizing... ')
for beam in beam_list:
    con.sis.output_sis_voltage(beam, 0.)
    time.sleep(1e-2) # 10 msec.

# setup plot_tool.
jpynb.make(dir_name_jpynb)
time.sleep(1.)

