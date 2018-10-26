#!/usr/bin/env python3

import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')

import slider_controller


ctrl = slider_controller.slider(rsw_id = "0")

# set parameter
x_start = 0
x_last = 190
y_start = - 0
y_last = - 190
strk = 1
tool = 'nothing'
sleep_measure = 1
dir = '/home/amigos/beam_pattern/data/2018_10_26_script_test/test4/'
beam_num = 'nothing'
sleep = 3

# command
ctrl.initialize(dir = dir)
ctrl.set_position(axis = 0, position = x_start)
time.sleep(sleep)
ctrl.measure(start = x_start, last = x_last, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
ctrl.set_position(axis = 0, position = x_last)
time.sleep(sleep)
ctrl.measure(start = x_last, last = x_start, axis = 'x', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
ctrl.set_position(axis = 0, position = 0)
time.sleep(sleep)
ctrl.set_position(axis = 1, position = y_start)
time.sleep(sleep)
ctrl.measure(start = y_start, last = y_last, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
time.sleep(sleep)
ctrl.set_position(axis = 1, position = y_last)
time.sleep(sleep)
ctrl.measure(start = y_last, last = y_start, axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
ctrl.finalize()
