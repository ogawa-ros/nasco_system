###slide_y_back.py

#!/usr/bin/env python3                                                                                                                                                

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter         
y_start = 0 #- 30 #0 #- 60                                                                                                                                        
y_last = - 190 #-170 #- 190 #-150                                                                                                                                  
strk = 1
sleep_measure = 2.5
dir = '/home/amigos/beam_pattern/data/2018_11_20/test17/'
sleep = 3

# command                                                                                                                                                             
ctrl.initialize(dir = dir)
ctrl.set_position(axis = 1, position = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = - strk, direction = 'cw', sleep_measure = sleep_measure)
ctrl.finalize()
