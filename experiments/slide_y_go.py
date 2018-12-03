###slide_y_go.py

#!/usr/bin/env python3

import sys
import time
sys.path.append('/root/ros/src/nasco_system/scripts')#('/home/amigos/ros/src/nasco_system/scripts')
import slider_controller

ctrl = slider_controller.slider(rsw_id = "0")

# set parameter         
y_start = -100 #-135 #-170 #- 190 #-150             
y_last = -90 #0 #- 30 #0 #- 60
strk = 1
sleep_measure = 1
dir = '/root/beam_pattern/data/2018_11_22/test01/'#'/home/amigos/beam_pattern/data/2018_11_22/test01/'
sleep = 3

# command
ctrl.initialize(dir = dir)
ctrl.set_step(axis = 1, step= y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = strk, direction = 'ccw', sleep_measure = sleep_measure)
ctrl.finalize()
