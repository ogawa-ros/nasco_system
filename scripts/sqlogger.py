#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import threading
from n2lite import n2lite

import rospy
import std_msgs.msg


# --
name = 'logger'
sisiv_flag = 'sisiv_trigger'
sisv_sweep_flag = 'sisv_sweep_trigger'
loatt_sweep_flag = 'loatt_sweep_trigger'
hemt_sweep_flag = 'hemt_sweep_trigger'
hot_monitor_flag = 'hot_monitor_trigger'
save_dir = '/home/amigos/data/sql/'
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
        
        self.flag = 0
        pass

    def make_table(self):
        self.n2.make_table("datatime", "(time float)")
        self.n2.make_table("sis_vol", "(sis_vol_2l float, sis_vol_2r float, sis_vol_3l float, sis_vol_3r float, sis_vol_4l float, sis_vol_4r float, sis_vol_5l float, sis_vol_5r float, sis_vol_1lu float, sis_vol_1ll float, sis_vol_1ru float, sis_vol_1rl float)")
        self.n2.make_table("sis_cur", "(sis_cur_2l float, sis_cur_2r float, sis_cur_3l float, sis_cur_3r float, sis_cur_4l float, sis_cur_4r float, sis_cur_5l float, sis_cur_5r float, sis_cur_1lu float, sis_cur_1ll float, sis_cur_1ru float, sis_cur_1rl float)")
        self.n2.make_table("hemt_vd", "(hemt_vd_2l float, hemt_vd_2r float, hemt_vd_3l float, hemt_vd_3r float, hemt_vd_4l float, hemt_vd_4r float, hemt_vd_5l float, hemt_vd_5r float, hemt_vd_1lu float, hemt_vd_1ll float, hemt_vd_1ru float, hemt_vd_1rl float)")
        self.n2.make_table("hemt_vg1", "(hemt_vg1_2l float, hemt_vg1_2r float, hemt_vg1_3l float, hemt_vg1_3r float, hemt_vg1_4l float, hemt_vg1_4r float, hemt_vg1_5l float, hemt_vg1_5r float, hemt_vg1_1lu float, hemt_vg1_1ll float, hemt_vg1_1ru float, hemt_vg1_1rl float)")
        self.n2.make_table("hemt_vg2", "(hemt_vg2_2l float, hemt_vg2_2r float, hemt_vg2_3l float, hemt_vg2_3r float, hemt_vg2_4l float, hemt_vg2_4r float, hemt_vg2_5l float, hemt_vg2_5r float, hemt_vg2_1lu float, hemt_vg2_1ll float, hemt_vg2_1ru float, hemt_vg2_1rl float)")
        self.n2.make_table("hemt_id", "(hemt_id_2l float, hemt_id_2r float, hemt_id_3l float, hemt_id_3r float, hemt_id_4l float, hemt_id_4r float, hemt_id_5l float, hemt_id_5r float, hemt_id_1lu float, hemt_id_1ll float, hemt_id_1ru float, hemt_id_1rl float)")
        self.n2.make_table("loatt", "(loatt_2l float, loatt_2r float, loatt_3l float, loatt_3r float, loatt_4l float, loatt_4r float, loatt_5l float, loatt_5r float, loatt_1l float, loatt_1r float)")
        self.n2.make_table("power", "(power_1 float, power_2 float)")
        self.n2.make_table("xffts", "(xffts_1 float)")
        return

    def set_flag(self, req, param):
        trigger = req.data
        if trigger == '': self.flag = 0
        else:
            self.timestamp = trigger
            self.param = param
            exp_time = datetime.datetime.fromtimestamp(float(self.timestamp))
            self.ymd = exp_time.strftime('%Y%m%d_')
            self.hms = exp_time.strftime('%H%M%S')

            self.saveto = os.path.join(save_dir, self.param, self.ymd + self.hms)
            os.makedirs(self.saveto)
            self.flag = 1
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

            else:
                t = datetime.datetime.fromtimestamp(time.time())
                dbpath = os.path.join(self.saveto, 'param.db')
                self.n2 = n2lite.N2lite(dbpath)
                self.make_table()
                print("DATABASE OPEN")

                while self.flag == 1:

                    self.n2.write("datatime", "", "({})".format(time.time()), auto_commit=False)
                    self.n2.write("sis_vol", "", tuple(self.sis_vol), auto_commit=False)
                    self.n2.write("sis_cur", "", tuple(self.sis_cur), auto_commit=False)
                    self.n2.write("hemt_vd", "", tuple(self.hemt_vd), auto_commit=False)
                    self.n2.write("hemt_vg1", "", tuple(self.hemt_vg1), auto_commit=False)
                    self.n2.write("hemt_vg2", "", tuple(self.hemt_vg2), auto_commit=False)
                    self.n2.write("hemt_id", "", tuple(self.hemt_id), auto_commit=False)
                    self.n2.write("loatt", "", tuple(self.loatt), auto_commit=False)
                    self.n2.write("power", "", tuple(self.power), auto_commit=False)
                    self.n2.write("xffts", "", "({})".format(self.xffts), auto_commit=False)
                    
                    time.sleep(1e-2) # 10 msec.
                else: 
                    self.n2.commit_data()
                    self.n2.close()
                    print("COMMIT DATA")
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
                                      std_msgs.msg.String,
                                      st.set_flag,
                                      callback_args = 'sisiv')
    sisv_sweep_flag_sub = rospy.Subscriber(sisv_sweep_flag,
                                      std_msgs.msg.String,
                                      st.set_flag,
                                      callback_args = 'sisv_sweep')
    loatt_sweep_flag_sub = rospy.Subscriber(loatt_sweep_flag,
                                      std_msgs.msg.String,
                                      st.set_flag,
                                      callback_args = 'loatt_sweep')
    hemt_sweep_flag_sub = rospy.Subscriber(hemt_sweep_flag,
                                      std_msgs.msg.String,
                                      st.set_flag,
                                      callback_args = 'hemt_sweep')

    hot_monitor_flag_sub = rospy.Subscriber(hot_monitor_flag,
                                      std_msgs.msg.String,
                                      st.set_flag,
                                      callback_args = 'hot_monitor')

    rospy.spin()
