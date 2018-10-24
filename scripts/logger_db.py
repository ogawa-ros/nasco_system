#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import threading
import sqlite3

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String


# --
name = 'logger_db'
sisiv_flag = 'sisiv_trigger'
sisv_sweep_flag = 'sisv_sweep_trigger'
loatt_sweep_flag = 'loatt_sweep_trigger'
hemt_sweep_flag = 'hemt_sweep_trigger'
hot_monitor_flag = 'hot_monitor_trigger'
data_dir = '/home/amigos/data/const/'
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
        self.xffts = [0.]

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

    def callback_xffts(self, req):
        self.xffts = req.data
        return

    def make_table(self):
        self.c.execute("create table if not exists datatime (time float)")
        self.c.execute("create table if not exists sis_vol ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.c.execute("create table if not exists sis_cur ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.c.execute("create table if not exists hemt_vd ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.c.execute("create table if not exists hemt_vg1 ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.c.execute("create table if not exists hemt_vg2 ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.c.execute("create table if not exists hemt_id ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.c.execute("create table if not exists loatt ('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1l' float, '1r' float)")
        self.c.execute("create table if not exists power (data1 float, data2 float)")
        self.c.execute("create table if not exists xffts (data float)")
        return

    def log(self):
        while not rospy.is_shutdown():
            if self.flag == 0:
                continue
            
            conn = sqlite3.connect(self.saveto + "nasco_system.db")
            self.c = connection.cursor()
            self.make_table()
            
            while self.flag == 1:

                self.c.execute("INSERT into datatime values (?)", (time.time(),))
                self.c.execute("INSERT into sis_vol values ( ?,?,?,?,?,?,?,?,?,?,?,?)", tuple(self.sis_vol))
                self.c.execute("INSERT into sis_cur values (?,?,?,?,?,?,?,?,?,?,?,?)", tuple(self.sis_cur))
                self.c.execute("INSERT into hemt_vd values (?,?,?,?,?,?,?,?,?,?,?,?)", tuple(self.hemt_vd))
                self.c.execute("INSERT into hemt_vg1 values (?,?,?,?,?,?,?,?,?,?,?,?)", tuple(self.hemt_vg1))
                self.c.execute("INSERT into hemt_vg2 values (?,?,?,?,?,?,?,?,?,?,?,?)", tuple(self.hemt_vg2))
                self.c.execute("INSERT into hemt_id values (?,?,?,?,?,?,?,?,?,?,?,?)", tuple(self.hemt_id))
                self.c.execute("INSERT into loatt values (?,?,?,?,?,?,?,?,?,?)", tuple(self.loatt))
                self.c.execute("INSERT into power values (?,?)", tuple(self.power))
                self.c.execute("INSERT into xffts values (?)", (self.xffts,))
                connection.commit()
                
                #time.sleep(4.0) # for gpib
                time.sleep(1e-2) # 10 msec.
                continue

            conn.close()
            

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

    xffts_sub_list = rospy.Subscriber('/XFFTS_PM1',
                                       Float64,
                                       st.callback_xffts)

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
