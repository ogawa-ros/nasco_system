#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller


ctrl = slider_controller.slider(rsw_id = "0")

# set parameter
x_start = 90
x_last = 160
y_start = 100
y_last = 30
strk = 1
speed = 1000
tool = 'nothing'
sleep_measure = 5
dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test'
beam_num = 'nothing'


# command
ctrl.initialize(x_start, y_start, speed, dir)
ctrl.measure(x_start = x_start, x_last = xlast, y_start = y_start, y_last = y_last,
            axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
ctrl.finalize()


