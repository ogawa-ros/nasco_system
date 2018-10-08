#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import threading

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String


# --
name = 'yfac_logger'
flag_name = 'yfac_trigger'
data_dir = '/home/necst/data/experiments/'
save_dir = os.path.join(data_dir, name)
# --


sis_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']


class yfac_logger(object):

    def __init__(self):
        self.flag = 0
        self.saveto = ''
        self.timestamp = 0
        self.sis_vol = [0.] * 12
        self.sis_cur = [0.] * 12
        self.power = [0.] * 2
        self.filename_vol = ''
        self.filename_cur = ''
        self.filename_power = ''

    def set_flag(self, req):
        trigger = req.data
        if trigger == '': self.flag = 0
        else:
            self.timestamp = trigger
            exp_time = datetime.datetime.fromtimestamp(float(self.timestamp))
            self.ymd = exp_time.strftime('%Y%m%d_')
            self.hms = exp_time.strftime('%H%M%S')
            self.saveto = os.path.join(save_dir, self.ymd + self.hms)
            os.makedirs(self.saveto)
            self.filename_vol = self.saveto + '/sis_vol.txt'
            self.filename_cur = self.saveto + '/sis_cur.txt'
            self.filename_power = self.saveto + '/power.txt'
            f_vol = open(self.filename_vol, 'a')
            f_cur = open(self.filename_cur, 'a')
            f_power = open(self.filename_power, 'a')
            f_vol.close()
            f_cur.close()
            f_power.close()
            self.flag = 1

    def callback_voltage(self, req, idx):
        if self.flag == 0:
            return

        self.sis_vol[idx] = req.data
        return

    def callback_current(self, req, idx):
        if self.flag == 0:
            return

        self.sis_cur[idx] = req.data
        return

    def callback_power(self, req, idx):
        if self.flag == 0:
            return

        self.power[idx] = req.data
        return

    def log(self):
        while not rospy.is_shutdown():
            if self.flag == 0:
                continue

            sis_vol = ' '.join(map(str, self.sis_vol)) + '\n'
            sis_cur = ' '.join(map(str, self.sis_cur)) + '\n'
            power = ' '.join(map(str, self.power)) + '\n'

            f_vol = open(self.filename_vol, 'a')
            f_cur = open(self.filename_cur, 'a')
            f_power = open(self.filename_power, 'a')
            f_vol.write(sis_vol)
            f_cur.write(sis_cur)
            f_power.write(power)
            f_vol.close()
            f_cur.close()
            f_power.close()

            time.sleep(1e-2) # 10 msec.

    def start_thread(self):
        th = threading.Thread(target=self.log)
        th.setDaemon(True)
        th.start()


if __name__ == '__main__':
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        pass

    st = yfac_logger()
    st.start_thread()
    rospy.init_node(name)
    # print('[yfac_logger] : START SUBSCRIBER ... ')
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
    power_sub_list = [rospy.Subscriber('power_{}'.format(ch),
                                       Float64,
                                       st.callback_power,
                                       callback_args = idx)
                        for ch, idx in enumerate(range(2), start=1)]
    flag_sub = rospy.Subscriber(flag_name, String, st.set_flag)
    rospy.spin()
