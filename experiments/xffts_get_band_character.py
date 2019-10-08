#! /usr/bin/env python3

# Configurations
# ==============

name = 'xffts_get_band_character'


# import
# ======

import sys
import time
import argparse
import numpy
import rospy
import std_msgs.msg

sys.path.append('/home/amigos/ros/src/nasco_system/scripts/')
import sg_controller
import jpynb_controller

jpynb = jpynb_controller.jpynb()
date = time.strftime('%Y%m%d-%H%M%S')
dir_name_jpynb = name + '/' + date

# argparse
# ========

# configurations
# --------------
desc = 'Measure XFFTS band character.'
integ = 1.0

p = argparse.ArgumentParser(description=desc)
p.add_argument('--integ', type=float,
               help='integration time in sec. default is  %f'%(integ))
args = p.parse_args()

# load args
# ---------
if args.integ is not None: integ = args.integ

# main
# ====
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Mesure XFFTS band character')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# start logging
# -------------
db_path = name + '/' + date

logger = rospy.Publisher('/logger_path', std_msgs.msg.String, queue_size=1)
pub_integ = rospy.Publisher('/'+name+'/integ', std_msgs.msg.Float32, queue_size=1)
time.sleep(0.5)

logger.publish(db_path)
time.sleep(0.5)

pub_integ.publish(integ)

# get band character
# --------------
time.sleep(integ)

# stop logging
# ------------
logger.publish('')


# setup plot_tool
#-------------
jpynb.make(dir_name_jpynb)
time.sleep(1.)


print('')
print('FINISH!!')
print('')

