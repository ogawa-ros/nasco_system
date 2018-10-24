#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter
y_start = - 170
y_last = - 80
strk = 1
tool = 'nothing'
sleep_measure = 1
dir = '/home/amigos/beam_pattern/data/2018_10_24_script_test'
beam_num = 'nothing'

# command
ctrl.initialize(dir = dir)
ctrl.set_position(axis = 0, position = y_start)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
ctrl.finalize()