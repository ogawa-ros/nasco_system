###slide_x_lap.py
#!/usr/bin/env python3

import sys
import time
sys.path.append('/root/ros/src/nasco_system/scripts') #('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter

x_start = 90
x_last = 100
strk = 1
sleep_measure = 0.1
dir = '/root/beam_pattern/data/2018_10_22/test01'#'/home/amigos/beam_pattern/data/2018_10_22/test01'
sleep = 1

# command

ctrl.initialize(dir = dir)
time.sleep(0.1)
ctrl.set_step(axis = 0, step = x_start)
time.sleep(sleep)
ctrl.measure(start = x_start, last = x_last, axis = 'x', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.set_step(axis = 0, step = x_last)
time.sleep(sleep)
ctrl.measure(start = x_last, last = x_start, axis = 'x', strk = - strk, direction = 'cw', sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.finalize()
