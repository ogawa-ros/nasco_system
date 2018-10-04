#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime

import rospy
from std_msgs.msg import Float64


# --
name = 'status_monitor'
data_dir = '/home/necst/data/experiments/'
save_dir = os.path.join(data_dir, name)

exp_time = datetime.datetime.utcnow()
ymd = exp_time.strftime("%Y%m%d_")
hms = exp_time.strftime("%H%M%S")
filename =  ymd + hms + ".txt"
saveto = os.path.join(save_dir + filename)
# --


interval = int(sys.argv[1])


class logger_low(object):

    def __init__(self):
        self.timestamp = 0
        self.l218_temp = [0.] * 8
        self.tpg261_pressure = 0.

    def callback_temp(self, req, idx):
        self.l218_temp[idx] = req.data
        return

    def callback_pressure(self, req):
        self.tpg261_pressure = req
        return

    def log(self):
        while not rospy.is_shutdown():
            ctime = time.time()
            f = open(saveto, 'a')
            temp = self_vol
    
            
