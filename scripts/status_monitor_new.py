#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import n2lite
import threading
import rospy
from std_msgs.msg import Float64


# --
name = 'status_monitor'
data_dir = '/home/amigos/data/sql/'
save_dir = '/home/amigos/data/sql/status/'

# --


class status_monitor(object):

    def __init__(self):
        self.timestamp = 0.
        self.l218_temp = [0.] * 8
        self.tpg261_pressure = 0.
        self.ondo = 0.
        self.hum = 0.
        self.datatime = 0.
        self.interval = int(sys.argv[1])
        pass
    
    def make_table(self):
        self.n2.make_table('datatime','(time float)')
        self.n2.make_table('l218_temp','(CH1 float, CH2 float, CH3 float, CH4 float, CH5 float, CH6 float, CH7 float, CH8 float)')
        self.n2.make_table('tpg261_pressure','(pressure float)')
        self.n2.make_table('temperture','(ondo float)')
        self.n2.make_table('humidity','(hum float)')
        return

    def callback_temp(self, req, idx):
        self.l218_temp[idx] = float(req.data)
        return

    def callback_pressure(self, req):
        self.tpg261_pressure = float(req.data)
        return

    def callback_ondo(self, req):
        self.ondo = float(req.data)
        return

    def callback_hum(self, req):
        self.hum = float(req.data)
        return

    def log(self):

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            pass

        self.timestamp = time.time()
        exp_time = datetime.datetime.fromtimestamp(self.timestamp)
        self.ymd = exp_time.strftime('%Y%m%d_')
        self.hms = exp_time.strftime('%H%M%S')
        self.saveto = os.path.join(save_dir, self.ymd + self.hms)
        os.makedirs(self.saveto)
        
        dbpath = self.saveto + '/nasco_status.db'
        self.n2 = n2lite.N2lite(dbpath)
        print("OPEN DATABASE")
        self.make_table()
        
        while not rospy.is_shutdown():
                    time.sleep(self.interval)
                    
                    self.n2.write('datatime','','({})'.format(time.time()), auto_commit=True)
                    self.n2.write('l218_temp','',tuple(self.l218_temp), auto_commit=True)
                    self.n2.write('tpg261_pressure','','({})'.format(self.tpg261_pressure), auto_commit=True)
                    self.n2.write('temperture','','({})'.format(self.ondo), auto_commit=True)
                    self.n2.write('humidity','','({})'.format(self.hum), auto_commit=True)

                    time.sleep(1e-2)

                    self.n2.commit_data()

        else:
            self.n2.close()
            print('COMMIT DATA')
                
        return


    def start_thread(self):
        th = threading.Thread(target=self.log)
        th.setDaemon(True)
        th.start()
        
if __name__ == '__main__': 
    st = status_monitor()
    st.start_thread()
    rospy.init_node(name)
    temp_sub_list = [rospy.Subscriber('/lakeshore_ch{}'.format(ch),
                                      Float64,
                                      st.callback_temp,
                                      callback_args = ch-1) \
                     for ch in range(1, 8 + 1)]
    pressure_sub = rospy.Subscriber('/tpg261_torr', Float64, st.callback_pressure)
    ondo_sub = rospy.Subscriber('/ondotori_temp', Float64, st.callback_ondo)
    hum_sub = rospy.Subscriber('/ondotori_hum', Float64, st.callback_hum)

    rospy.spin()


