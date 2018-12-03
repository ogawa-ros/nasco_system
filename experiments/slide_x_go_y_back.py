###slide_x_go_y_back.py

#!/usr/bin/env python3

import sys
import time
sys.path.append('/root/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter

x_start = 90 #90
x_last = 100 #170
y_start = -90 #-30
y_last = -100 #-170
strk = 1
sleep_measure = 1
dir = '/root/beam_pattern/data/2018_10_22/test01'
sleep =	3

# command
ctrl.initialize(dir = dir)
ctrl.set_step(axis = 0, step = x_start)
time.sleep(sleep)
ctrl.measure(start = x_start, last = x_last, axis = 'x', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
ctrl.set_step(axis = 0, step = 0)
time.sleep(sleep)
ctrl.set_step(axis = 1, step = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = - strk, direction = 'cw', sleep_measure = sleep_measure)
ctrl.finalize()
