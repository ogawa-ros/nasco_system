###slide_x_go.py

#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter
x_start = 90 #0 #50 #0 #80
x_last = 100 #190 #190 #170
strk = 1
sleep_measure = 0.1
dir = '/home/amigos/beam_pattern/data/2018_11_22/test01/'
sleep = 1

# command
ctrl.initialize(dir = dir)
time.sleep(0.1)
ctrl.set_step(axis = 0, step = x_start)
time.sleep(sleep)
ctrl.measure(start = x_start, last = x_last, axis = 'x', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.finalize()
