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
data_dir = '/home/amigos/data/experiments/'
save_dir = os.path.join(data_dir, name)

exp_time = datetime.datetime.fromtimestamp(time.time())
ymd = exp_time.strftime("%Y%m%d_")
hms = exp_time.strftime("%H%M%S")
filename =  ymd + hms + ".txt"
saveto = os.path.join(save_dir, filename)
# --


interval = int(sys.argv[1])


class status_monitor(object):

    def __init__(self):
        self.timestamp = 0.
        self.l218_temp = [0.] * 8
        self.tpg261_pressure = 0.
        self.ondo = 0.
        self.hum = 0.

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
        while not rospy.is_shutdown():
            f = open(saveto, 'a')
            _ctime = time.time()
            ctime = datetime.datetime.fromtimestamp(_ctime)
            date1 = [ctime.strftime('%Y-%m-%d %H:%M:%S')]
            date2 = [time.time()]
            l218_temp = [temp for temp in self.l218_temp]
            pre = [self.tpg261_pressure]
            ondo = [self.ondo, self.hum]
            msg1 = date1 + l218_temp + pre + ondo
            msg2 = date2 + l218_temp + pre + ondo
            msg1 = '{0} {1:.2f}K {2:.2f}K {3:.2f}K {4:.2f}K {5:.2f}K {6:.2f}K {7:.2f}K {8:.2f}K {9:.1}torr {10:.2f}deg {11:.2f}%'.format(*msg1)
            msg2 = '{0} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f} {6:.2f} {7:.2f} {8:.2f} {9:.1} {10:.2f} {11:.2f}\n'.format(*msg2)
            print(msg1)
            f.write(msg2)
            f.close()

            time.sleep(interval)
            continue
        return


if __name__ == '__main__':
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        pass

    st = status_monitor()
    rospy.init_node(name)
    temp_sub_list = [rospy.Subscriber('/lakeshore_ch{}'.format(ch),
                                      Float64,
                                      st.callback_temp,
                                      callback_args = ch-1) \
                     for ch in range(1, 8 + 1)]
    pressure_sub = rospy.Subscriber('/tpg261_torr', Float64, st.callback_pressure)
    ondo_sub = rospy.Subscriber('/ondotori_temp', Float64, st.callback_ondo)
    hum_sub = rospy.Subscriber('/ondotori_hum', Float64, st.callback_hum)
    st.log()


