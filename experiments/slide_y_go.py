###slide_y_go.py

#!/usr/bin/env python3                                                                                                                                                

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter         
y_start = -135 #-170 #- 190 #-150             
y_last = 0 #- 30 #0 #- 60                                                                                                            
strk = 1
sleep_measure = 2.5
dir = '/home/amigos/beam_pattern/data/2018_11_12/test18/'
sleep = 3

# command                                                                                                                                                             
ctrl.initialize(dir = dir)
ctrl.set_position(axis = 1, position = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
ctrl.finalize()
