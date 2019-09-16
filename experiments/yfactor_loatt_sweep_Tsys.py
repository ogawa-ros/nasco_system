#!/usr/bin/env python3


name = 'yfactor_loatt_sweep_Tsys'


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

# pub intialize
# ------------
logger = rospy.Publisher('/logger_path', std_msgs.msg.String, queue_size=1)
status = rospy.Publisher('/'+name+'/status', std_msgs.msg.String, queue_size=1)
time.sleep(0.5)

# set params.
beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r']
con.sis.output_sis_voltage_config()
con.hemt.output_hemt_voltage_config()


initial_current = 0.0 # mA
final_current   = 1.0 # mA
step            = 0.1 # mA
interval        = 0.1 # sec.
fixtime         = 1 # sec.
roop = int((final_current - initial_current) / step)


# initialize ( hot ).
print('[INFO] : Initializing for hot... ')
for beam in beam_list:
    con.loatt.output_loatt_current(beam, initial_current)
    time.sleep(1e-2) # 10 msec.


#logger start
logger.publish(dir_name)

# move hot
print('[INFO] : Movo chopper to HOT ...')
#con.slider0.set_step('u',0)
status.publish('{0:4s}'.format('hot'))
time.sleep(1.)


# measure hot.
print('[INFO] : Start to measure hot with loatt sweep.')

time.sleep(1e-2)

for cur in range(roop + 1):
    for beam in beam_list:
        con.loatt.output_loatt_current(beam=beam, current=cur*step+initial_current)
        time.sleep(1e-2) # 10 msec.
    time.sleep(fixtime)

print('[INFO] : Finish measure hot with loatt sweep')
time.sleep(1.)

#initilize current
for beam in beam_list:
    con.loatt.output_loatt_current(beam, initial_current)
    time.sleep(0.01) # 10 msec.


# move cold
print('[INFO] : Movo chopper from HOT to COLD...')
#con.slider0.set_step('u',250)
status.publish('{0:4s}'.format('cold'))
time.sleep(1.)

# measure cold.
print('[INFO] : Start to measure cold with loatt sweep.')


for cur in range(roop + 1):
    for beam in beam_list:
        con.loatt.output_loatt_current(beam=beam, current=cur*step+initial_current)
        time.sleep(1e-2) # 10 msec.
    time.sleep(fixtime)

print('[INFO] : Finish measure cold with loatt sweep')
time.sleep(1.)

# setup plot_tool.
jpynb.make(dir_name.replace('.necstdb', ''))
time.sleep(1.)

# finalize.
#con.slider0.set_step('u', 0)
status.publish('{0:4s}'.format('hot'))
time.sleep(1.)

print('[INFO] : Finalizing... ')
for beam in beam_list:
    con.loatt.output_loatt_current(beam, 0.)
    time.sleep(1e-2) # 10 msec.

time.sleep(2.)
logger.publish('')

print('')
print('FINISH!')
print('')
