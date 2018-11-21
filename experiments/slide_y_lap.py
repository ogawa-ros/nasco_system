###slide_y_lap.py

#!/usr/bin/env python3                                                                                                                                                                                      

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter                                                                                                                                                                                             
y_start = - 30 #0 #- 60                                                                                                                                        
y_last = -170 #- 190 #-150 
strk = 1
sleep_measure = 1
dir = '/home/amigos/beam_pattern/data/2018_10_24_script_test'
sleep = 3

# command                                                                                                                                                    
ctrl.initialize(dir = dir)
ctrl.set_position(axis = 0, position = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = strk, direction = 'cw', sleep_measure = sleep_measure)
ctrl.set_position(axis = 0, position = y_last)
time.sleep(sleep)
ctrl.measure(start = y_last, last = y_start, axis = 'y', strk = - strk, direction = 'ccw', sleep_measure = sleep_measure)
ctrl.finalize()