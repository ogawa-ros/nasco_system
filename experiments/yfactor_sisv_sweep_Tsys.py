#!/usr/bin/env python3


name = 'yfactor_sisv_sweep_Tsys'


import sys
import rospy
import time
import std_msgs.msg
import datetime

sys.path.append('/home/amigos/ros/src/nasco_system/scripts/')
import nasco_controller
import jpynb_controller

rospy.init_node(name)

con = nasco_controller.controller(node=False)
jpynb = jpynb_controller.jpynb()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name = name + '/' + date + '.necstdb'

# pub initialize
# --------------
logger = rospy.Publisher('/logger_path', std_msgs.msg.String, queue_size=1)
status = rospy.Publisher('/'+name+'/status', std_msgs.msg.String, queue_size=1)
time.sleep(0.5)

# set params.
beam_list = con.beam_list

initial_voltage = 0 # mV
final_voltage   = 10 # mV
step            = 0.1 # mV
roop = int((final_voltage - initial_voltage) / step)

#initialize
for beam in beam_list:
    con.sis.output_sis_voltage(beam, initial_voltage)
    time.sleep(0.01) # 10 msec.


#logger start
logger.publish(dir_name)
# move hot
print('[INFO] : Movo chopper to HOT ...')
con.slider0.set_step('u', 0)
status.publish('{0:4s}'.format('hot'))
time.sleep(1.)

#sweep voltage(hot)
print('[INFO] : Start to measure hot with sisv sweep.')

for vol in range(roop + 1):
    for beam in beam_list:
        con.sis.output_sis_voltage(beam=beam, voltage=vol*step+initial_voltage)
        time.sleep(0.01) # 10 msec.
    time.sleep(1.)

print('[INFO] : Finish measure hot with sisv sweep')

#initilize voltage
for beam in beam_list:
    con.sis.output_sis_voltage(beam, initial_voltage)
    time.sleep(0.01) # 10 msec.


#move cold
print('[INFO] : Movo chopper from HOT to COLD...')
con.slider0.set_step('u', 250)
status.publish('{0:4s}'.format('cold'))
time.sleep(1.)

#sweep voltage(cold)
print('[INFO] : Start to measure cold with sisv sweep.')

for vol in range(roop + 1):
    for beam in beam_list:
        con.sis.output_sis_voltage(beam=beam, voltage=vol*step+initial_voltage)
        time.sleep(0.01) # 10 msec.
    time.sleep(1.)

print('[INFO] : Finish measure cold with sisv sweep')
time.sleep(1.)

# setup plot_tool
#-------------
jpynb.make(dir_name.replace('.necstdb', ''))
time.sleep(1.)

#finalize
con.slider0.set_step('u', 0)
status.publish('{0:4s}'.format('hot'))
time.sleep(1.)

for beam in beam_list:
    con.sis.output_sis_voltage(beam, 0.)
    time.sleep(0.01) # 10 msec.

time.sleep(2.)
logger.publish('')

print('')
print('FINISH!!')
print('')
