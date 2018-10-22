#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import threading
import sqlite3

import rospy
import std_msgs.msg


# --
name = 'const_logger'
dbpath = '/home/amigos/data/const/nasco_system.db'
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
        self.cursor.execute("create table if not exists xffts (time float, pm float)")
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
        connection = sqlite3.connect(dbpath)
        self.cursor = connection.cursor()

        self.make_table()
        while not rospy.is_shutdown():
            """
            datatime = str(time.time()) + '\n'
            sis_vol = ' '.join(map(str, self.sis_vol)) + '\n'
            sis_cur = ' '.join(map(str, self.sis_cur)) + '\n'
            hemt_vd = ' '.join(map(str, self.hemt_vd)) + '\n'
            hemt_vg1 = ' '.join(map(str, self.hemt_vg1)) + '\n'
            hemt_vg2 = ' '.join(map(str, self.hemt_vg2)) + '\n'
            hemt_id = ' '.join(map(str, self.hemt_id)) + '\n'
            loatt = ' '.join(map(str, self.loatt)) + '\n'            
            power = ' '.join(map(str, self.power)) + '\n'
            xffts = ' '.join(map(str, self.xffts)) + '\n'
            """

            self.cursor.execute("INSERT into xffts (time, PM) values (?,?)",
                    (time.time(), self.xffts))
            connection.commit()
            
            time.sleep(1e-2) # 10 msec.
            continue
        else:
            connection.close()

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

    rospy.spin()
