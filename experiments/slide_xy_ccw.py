###slide_xy_ccw.py
                                                                                                                
#!/usr/bin/env python3                                                                                                                                         

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter                                                                                                                                                
x_start = 50 #0 #80                                                                                                                                            
x_last = 190 #170                                                                                                                                         
y_start = -170 #- 190 #-150                                                                                                                                          
y_last = - 30 #0 #- 60                                                                                                               
strk = 1
sleep_measure = 2.5
dir = '/home/amigos/beam_pattern/data/2018_11_20/test14/'
sleep = 3

# command                                                                                                                                                      
ctrl.initialize(dir = dir)
ctrl.set_position(axis = 0, position = x_start)
time.sleep(sleep)
ctrl.measure(start = x_start, last = x_last, axis = 'x', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
ctrl.set_position(axis = 0, position = 0)
time.sleep(sleep)
ctrl.set_position(axis = 1, position = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
ctrl.finalize()
