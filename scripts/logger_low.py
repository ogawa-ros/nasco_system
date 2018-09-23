#!/usr/bin/env python3

import os
import sys
import time
import numpy
import datetime

import rospy
from std_msgs.msg import Float64


# --
name = 'logger_low'
data_dir = '/home/amigos/data/experiments/'
save_dir = os.path.join(data_dir, name)

exp_time = datetime.datetime.utcnow()
ymd = exp_time.strftime("%Y%m%d_")
hms = exp_time.strftime("%H%M%S")
filename =  ymd + hms + ".txt"
saveto = os.path.join(save_dir + filename)
# --

interval = int(sys.argv[1])

sis_list = ['1lu', '1ll', '1ru', '1rl',
            '2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r']


class logger_low(object):
    
    def __init__(self):
        self.timestamp = 0
        self.sis_vol = [0.] * 12
        self.sis_cur = [0.] * 12

    def callback_voltage(self, req, idx):
        self.sis_vol[idx] = req.data
        return

    def callback_current(self, req, idx):
        self.sis_cur[idx] = req.data
        return

    def log(self):
        while not rospy.is_shutdown():
            ctime = time.time()
            f = open(saveto, 'a')
            sis_vol = self.sis_vol
            sis_cur = self.sis_cur
            sis_status = []
            [sis_status.extend([round(v, 3), round(i, 3)]) for v, i in zip(sis_vol, sis_cur)]
            msg1 = '{0} {1} {2} {3} {4} {5} {6} {7} {8}' \
                   '{9} {10} {11} {12} {13} {14} {15} {16} {17} {18}'\
                   '{20} {21} {22} {23}'.format(*sis_status)
            msg2 = '{0}mV {1}uA {2}mV {3}uA {4}mV {5}uA {6}mV {7}uA {8}mV' \
                   '{9}uA {10}mV {11}uA {12}mV {13}uA {14}mV {15}uA {16}mV {17}uA {18}mV'\
                   '{19}uA {20}mV {21}uA {22}mV {23}uA'.format(*sis_status)
            print(msg2)
            f.write(msg1)
            f.close()

            time.sleep(interval)
            continue
        return
        

if __name__ == '__main__':
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        pass

    st = logger_low()
    rospy.init_node(name)
    print('[INFO] Start recording {}'.format(saveto))
    sis_vol_sub_list = [rospy.Subscriber('sis_vol_{}'.format(sis),
                                         Float64,
                                         st.callback_voltage,
                                         callback_args = idx)
                        for idx, sis in enumerate(sis_list)]
    sis_cur_sub_list = [rospy.Subscriber('sis_cur_{}'.format(sis),
                                         Float64,
                                         st.callback_current,
                                         callback_args = idx)
                        for idx, sis in enumerate(sis_list)]
    st.log()
