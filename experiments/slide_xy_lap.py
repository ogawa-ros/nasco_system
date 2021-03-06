###slide_xy_lap.py

#!/usr/bin/env python3
print('1')
import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "1")
print('2')
# set parameter
x_start = 10 #50 #0 #80
x_last = 190 #190 #190 #170
y_start = - 10 #- 30 #0 #- 60
y_last = - 190 #-170 #- 190 #-150
strk = 1
sleep_measure = 0.1
dir = '/home/amigos/beam_pattern/data/2019_10_08/test03/'
sleep = 1
print('3')
# command
ctrl.initialize(dir = dir)
print('4')
time.sleep(0.1)
ctrl.set_step(axis = 0, step = x_start)
time.sleep(sleep)
ctrl.measure(start = x_start, last = x_last, axis = 'x', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.set_step(axis = 0, step = x_last)
time.sleep(sleep)
ctrl.measure(start = x_last, last = x_start, axis = 'x', strk = - strk, direction = 'cw', sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.set_step(axis = 0, step = 0)
time.sleep(sleep)
ctrl.set_step(axis = 1, step = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = - strk, direction = 'cw', sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.set_step(axis = 1, step = y_last)
time.sleep(sleep)
ctrl.measure(start = y_last, last = y_start, axis = 'y', strk = strk, direction = 'ccw',sleep_measure = sleep_measure)
time.sleep(0.1)
ctrl.finalize()
