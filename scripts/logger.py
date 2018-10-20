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
name = 'logger'
sisiv_flag = 'sisiv_trigger'
sisv_sweep_flag = 'sisv_sweep_trigger'
loatt_sweep_flag = 'loatt_sweep_trigger'
hemt_sweep_flag = 'hemt_sweep_trigger'
hot_monitor_flag = 'hot_monitor_trigger'
data_dir = '/home/amigos/data/experiments/'
save_dir = os.path.join(data_dir, name)
# --


beam_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

loatt_list = beam_list[:-4]
loatt_list.extend(['1l', '1r'])


class logger(object):

    def __init__(self):
        self.flag = 0
        self.sisv_sweep_flag = 0
        self.loatt_sweep_flag = 0
        self.hemt_sweep_flag = 0
        self.hot_monitor_flag = 0
        self.saveto = ''
        self.timestamp = 0
        self.datatime = 0
        self.sis_vol = [0.] * 12
        self.sis_cur = [0.] * 12
        self.hemt_vd = [0.] * 12
        self.hemt_vg1 = [0.] * 12
        self.hemt_vg2 = [0.] * 12
        self.hemt_id = [0.] * 12
        self.loatt = [0.] * 10
        self.power = [0.] * 2
        self.filename_datatime = ''
        self.filename_vol = ''
        self.filename_cur = ''
        self.filename_vd = ''
        self.filename_vg1 = ''
        self.filename_vg2 = ''
        self.filename_id = ''
        self.filename_loatt = ''
        self.filename_power = ''

    def set_flag(self, req, param):
        trigger = req.data
        if trigger == '': self.flag = 0
        else:
            if 'lo' in trigger:
                self.timestamp = trigger.replace('-lo', '')
                lo = '-lo'
            else: self.timestamp, lo = trigger, ''            
            self.param = param
            exp_time = datetime.datetime.fromtimestamp(float(self.timestamp))
            self.ymd = exp_time.strftime('%Y%m%d_')
            self.hms = exp_time.strftime('%H%M%S')
            self.saveto = os.path.join(save_dir, self.param, self.ymd + self.hms)
            os.makedirs(self.saveto)
            self.filename_datatime = self.saveto + '/datatime.txt'
            self.filename_vol = self.saveto + '/sis_vol.txt'
            self.filename_cur = self.saveto + '/sis_cur.txt'
            self.filename_vd = self.saveto + '/hemt_vd.txt'
            self.filename_vg1 = self.saveto + '/hemt_vg1.txt'
            self.filename_vg2 = self.saveto + '/hemt_vg2.txt'
            self.filename_id = self.saveto + '/hemt_id.txt'
            self.filename_loatt = self.saveto + '/loatt.txt'
            self.filename_power = self.saveto + '/power.txt'
            print("FILE OPEN")
            f_datetime = open(self.filename_datatime, 'a')
            f_vol = open(self.filename_vol, 'a')
            f_cur = open(self.filename_cur, 'a')
            f_vd = open(self.filename_vd, 'a')
            f_vg1 = open(self.filename_vg1, 'a')
            f_vg2 = open(self.filename_vg2, 'a')
            f_id = open(self.filename_id, 'a')
            f_loatt = open(self.filename_loatt, 'a')
            f_power = open(self.filename_power, 'a')
            f_datetime.close()
            f_vol.close()
            f_cur.close()
            f_vd.close()
            f_vg1.close()
            f_vg2.close()
            f_id.close()
            f_loatt.close()
            f_power.close()
            self.flag = 1

    def callback_voltage(self, req, idx):

        self.sis_vol[idx] = req.data
        return

    def callback_current(self, req, idx):

        self.sis_cur[idx] = req.data
        return

    def callback_hemt_vd(self, req, idx):

        self.hemt_vd[idx] = req.data
        return

    def callback_hemt_vg1(self, req, idx):

        self.hemt_vg1[idx] = req.data
        return

    def callback_hemt_vg2(self, req, idx):

        self.hemt_vg2[idx] = req.data
        return

    def callback_hemt_id(self, req, idx):

        self.hemt_id[idx] = req.data
        return

    def callback_loatt(self, req, idx):

        self.loatt[idx] = req.data
        return    

    def callback_power(self, req, idx):

        self.power[idx] = req.data
        return

    def log(self):
        while not rospy.is_shutdown():
            if self.flag == 0:
                continue

            datatime = str(time.time()) + '\n'
            sis_vol = ' '.join(map(str, self.sis_vol)) + '\n'
            sis_cur = ' '.join(map(str, self.sis_cur)) + '\n'
            hemt_vd = ' '.join(map(str, self.hemt_vd)) + '\n'
            hemt_vg1 = ' '.join(map(str, self.hemt_vg1)) + '\n'
            hemt_vg2 = ' '.join(map(str, self.hemt_vg2)) + '\n'
            hemt_id = ' '.join(map(str, self.hemt_id)) + '\n'
            loatt = ' '.join(map(str, self.loatt)) + '\n'            
            power = ' '.join(map(str, self.power)) + '\n'

            f_datatime = open(self.filename_datatime, 'a')
            f_vol = open(self.filename_vol, 'a')
            f_cur = open(self.filename_cur, 'a')
            f_vd = open(self.filename_vd, 'a')
            f_vg1 = open(self.filename_vg1, 'a')
            f_vg2 = open(self.filename_vg2, 'a')
            f_id = open(self.filename_id, 'a')
            f_loatt = open(self.filename_loatt, 'a')
            f_power = open(self.filename_power, 'a')
            f_datatime.write(datatime)
            f_vol.write(sis_vol)
            f_cur.write(sis_cur)
            f_vd.write(hemt_vd)
            f_vg1.write(hemt_vg1)
            f_vg2.write(hemt_vg2)
            f_id.write(hemt_id)
            f_vd.write(hemt_vd)
            f_loatt.write(loatt)
            f_power.write(power)
            f_datatime.close()
            f_vol.close()
            f_cur.close()
            f_vd.close()
            f_vg1.close()
            f_vg2.close()
            f_id.close()
            f_loatt.close()
            f_power.close()
            
            #time.sleep(4.0) # for gpib
            time.sleep(1e-2) # 10 msec.

    def start_thread(self):
        th = threading.Thread(target=self.log)
        th.setDaemon(True)
        th.start()


if __name__ == '__main__':
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        pass

    st = logger()
    st.start_thread()
    rospy.init_node(name)
    sis_vol_sub_list = [rospy.Subscriber('sis_vol_{}'.format(sis),
                                         Float64,
                                         st.callback_voltage,
                                         callback_args = idx)
                        for idx, sis in enumerate(beam_list)]
    sis_cur_sub_list = [rospy.Subscriber('sis_cur_{}'.format(sis),
                                         Float64,
                                         st.callback_current,
                                         callback_args = idx)
                        for idx, sis in enumerate(beam_list)]
    power_sub_list = [rospy.Subscriber('power_{}'.format(ch),
                                       Float64,
                                       st.callback_power,
                                       callback_args = idx)
                        for ch, idx in enumerate(range(2), start=1)]

    hemt_vd_sub_list = [rospy.Subscriber('/hemt_{}_vd'.format(beam),
                                         Float64,
                                         st.callback_hemt_vd,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    hemt_vg1_sub_list = [rospy.Subscriber('/hemt_{}_vg1'.format(beam),
                                         Float64,
                                         st.callback_hemt_vg1,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    hemt_vg2_sub_list = [rospy.Subscriber('/hemt_{}_vg2'.format(beam),
                                         Float64,
                                         st.callback_hemt_vg2,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    hemt_id_sub_list = [rospy.Subscriber('/hemt_{}_id'.format(beam),
                                         Float64,
                                         st.callback_hemt_id,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    loatt_sub_list = [rospy.Subscriber('/loatt_{}'.format(loatt),
                                         Float64,
                                         st.callback_loatt,
                                         callback_args = idx)
                        for idx, loatt in enumerate(loatt_list)]
    sisiv_flag_sub = rospy.Subscriber(sisiv_flag,
                                      String,
                                      st.set_flag,
                                      callback_args = 'sisiv')
    sisv_sweep_flag_sub = rospy.Subscriber(sisv_sweep_flag,
                                      String,
                                      st.set_flag,
                                      callback_args = 'sisv_sweep')
    loatt_sweep_flag_sub = rospy.Subscriber(loatt_sweep_flag,
                                      String,
                                      st.set_flag,
                                      callback_args = 'loatt_sweep')
    hemt_sweep_flag_sub = rospy.Subscriber(hemt_sweep_flag,
                                      String,
                                      st.set_flag,
                                      callback_args = 'hemt_sweep')

    hot_monitor_flag_sub = rospy.Subscriber(hot_monitor_flag,
                                      String,
                                      st.set_flag,
                                      callback_args = 'hot_monitor')

    rospy.spin()
