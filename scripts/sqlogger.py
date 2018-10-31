#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import threading
sys.path.append("/home/amigos/python/")
import n2lite

import rospy
import std_msgs.msg


# --
name = 'sqlogger'
t = datetime.datetime.fromtimestamp(time.time())
dbpath = '/home/amigos/data/nasco_{}.db'.format(t.strftime('%Y%m%d_%H%M%S'))
# --


beam_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

loatt_list = beam_list[:-4]
loatt_list.extend(['1l', '1r'])


class logger(object):

    def __init__(self):
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
        self.xffts = 0

        pass

    def make_table(self):
        self.n2.make_table("datatime", "(time float)")
        self.n2.make_table("sis_vol", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.n2.make_table("sis_cur", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.n2.make_table("hemt_vd", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.n2.make_table("hemt_vg1", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.n2.make_table("hemt_vg2", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.n2.make_table("hemt_id", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1lu' float, '1ll' float, '1ru' float, '1rl' float)")
        self.n2.make_table("loatt", "('2l' float, '2r' float, '3l' float, '3r' float, '4l' float, '4r' float, '5l' float, '5r' float, '1l' float, '1r' float)")
        self.n2.make_table("power", "(data1 float, data2 float)")
        self.n2.make_table("xffts", "(data float)")
        return

    def set_flag(self, req, param):
        trigger = req.data
        if trigger == '': self.flag = 0
        else: self.flag = 1
        return

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

    def log(self):
        while not rospy.is_shutdown():
            if self.flag == 0:
                time.sleep(0.1)
                continue

            t = datetime.datetime.fromtimestamp(time.time())
            dbpath = '/home/amigos/data/nasco_{}.db'.format(t.strftime('%Y%m%d_%H%M%S'))
            self.n2 = n2lite.N2lite(dbpath)
            self.make_table()
            while self.flag == 1:

                self.n2.write("datatime", "", (time.time(),))
                self.n2.write("sis_vol", "", tuple(self.sis_vol))
                self.n2.write("sis_cur", "", tuple(self.sis_cur))
                self.n2.write("hemt_vd", "", tuple(self.hemt_vd))
                self.n2.write("hemt_vg1", "", tuple(self.hemt_vg1))
                self.n2.write("hemt_vg2", "", tuple(self.hemt_vg2))
                self.n2.write("hemt_id", "", tuple(self.hemt_id))
                self.n2.write("loatt", "", tuple(self.loatt))
                self.n2.write("power", "", tuple(self.power))
                self.n2.write("xffts", "", (self.xffts,))

                time.sleep(1e-2) # 10 msec.
            else: self.n2.close()
            continue
        
        return

    def start_thread(self):
        th = threading.Thread(target=self.log)
        th.setDaemon(True)
        th.start()


if __name__ == '__main__':

    st = logger()
    st.start_thread()
    rospy.init_node(name)
    sis_vol_sub_list = [rospy.Subscriber('sis_vol_{}'.format(sis),
                                         std_msgs.msg.Float64,
                                         st.callback_voltage,
                                         callback_args = idx)
                        for idx, sis in enumerate(beam_list)]
    sis_cur_sub_list = [rospy.Subscriber('sis_cur_{}'.format(sis),
                                         std_msgs.msg.Float64,
                                         st.callback_current,
                                         callback_args = idx)
                        for idx, sis in enumerate(beam_list)]
    power_sub_list = [rospy.Subscriber('power_{}'.format(ch),
                                       std_msgs.msg.Float64,
                                       st.callback_power,
                                       callback_args = idx)
                        for ch, idx in enumerate(range(2), start=1)]

    xffts_sub_list = rospy.Subscriber('/XFFTS_PM1',
                                       std_msgs.msg.Float64,
                                       st.callback_xffts)

    hemt_vd_sub_list = [rospy.Subscriber('/hemt_{}_vd'.format(beam),
                                         std_msgs.msg.Float64,
                                         st.callback_hemt_vd,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    hemt_vg1_sub_list = [rospy.Subscriber('/hemt_{}_vg1'.format(beam),
                                         std_msgs.msg.Float64,
                                         st.callback_hemt_vg1,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    hemt_vg2_sub_list = [rospy.Subscriber('/hemt_{}_vg2'.format(beam),
                                         std_msgs.msg.Float64,
                                         st.callback_hemt_vg2,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    hemt_id_sub_list = [rospy.Subscriber('/hemt_{}_id'.format(beam),
                                         std_msgs.msg.Float64,
                                         st.callback_hemt_id,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    loatt_sub_list = [rospy.Subscriber('/loatt_{}'.format(loatt),
                                         std_msgs.msg.Float64,
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
