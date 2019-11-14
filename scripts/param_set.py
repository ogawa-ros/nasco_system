#!/usr/bin/env/ python3
import sys
import nasco_controller
ctrl = nasco_controller.controller()


#config_file = configparser.ConfigParser()
#config_file.read('/home/amigos/ros/src/nasco_system/configuration/')


# Set Param
ctrl.hemt.output_hemt_voltage_config('vd','vg1','vg2',config = None)
ctrl.loatt.output_loatt_current_config()
ctrl.sis.output_sis_voltage_config()
