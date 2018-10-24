#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller


ctrl = slider_controller.slider(rsw_id = "0")

# set parameter
x = 90
y = 30
length = 70
strk = 1
speed = 1000
tool = 'nothing'
sleep_measure = 5
dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test'
beam_num = 'nothing'


# command
ctrl.initialize(x, y, length, strk, speed, dir)
ctrl.on_ptp(axis = 1, len = 190 - last_y)# need change
ctrl.measure(x = x, y = y, length = length, axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
ctrl.finalize()


