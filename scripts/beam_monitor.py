#!/usr/bin/env python3


import os
import sys
import time
import numpy
import datetime
import threading

import rospy
from std_msgs.msg import Float64


# --
name = 'beam_monitor'
data_dir = '/home/amigos/data/experiments/'
save_dir = os.path.join(data_dir, name)

exp_time = datetime.datetime.utcnow()
ymd = exp_time.strftime("%Y%m%d_")
hms = exp_time.strftime("%H%M%S")
filename =  ymd + hms + ".txt"
saveto = os.path.join(save_dir + filename)
# --

interval = float(sys.argv[1])

beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']

loatt_list = beam_list[:-4]
loatt_list.extend(['1l', '1r'])


class beam_monitor(object):

    def __init__(self):
        self.timestamp = 0.
        self.sis_vol = [0.] * 12
        self.sis_cur = [0.] * 12
        self.hemt_vd = [0.] * 12
        self.hemt_vg1 = [0.] * 12
        self.hemt_vg2 = [0.] * 12
        self.hemt_id = [0.] * 12
        self.loatt = [0.] * 10

    def callback_sis_vol(self, req, idx):

        self.sis_vol[idx] = req.data
        return

    def callback_sis_cur(self, req, idx):

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

    def start_thread(self):
        th = threading.Thread(target=self.log)
        th.setDaemon(True)
        th.start()

    def log(self):
        print('\n\n/------- nasco beam monitor \n')
        print('[BEAM / SISV / SISI / VD / VG1 / VG2 / ID / LOATT]')
        
        print('\n\n\n\n\n\n\n\n\n\n\n\n')
        while not rospy.is_shutdown():
            sis_vol = self.sis_vol
            sis_cur = self.sis_cur
            hemt_vd = self.hemt_vd
            hemt_vg1 = self.hemt_vg1
            hemt_vg2 = self.hemt_vg2
            hemt_id = self.hemt_id            
            loatt = self.loatt
            [exec('globals()["v_{0}"] = {1}'.format(beam, vol)) for beam, vol in zip(beam_list, sis_vol)]
            [exec('globals()["c_{0}"] = {1}'.format(beam, cur)) for beam, cur in zip(beam_list, sis_cur)]
            [exec('globals()["vd_{0}"] = {1}'.format(beam, vd)) for beam, vd in zip(beam_list, hemt_vd)]
            [exec('globals()["vg1_{0}"] = {1}'.format(beam, vg1)) for beam, vg1 in zip(beam_list, hemt_vg1)]
            [exec('globals()["vg2_{0}"] = {1}'.format(beam, vg2)) for beam, vg2 in zip(beam_list, hemt_vg2)]
            [exec('globals()["id_{0}"] = {1}'.format(beam, _id)) for beam, _id in zip(beam_list, hemt_id)]            
            [exec('globals()["lo_{0}"] = {1}'.format(beam, lo)) for beam, lo in zip(loatt_list, loatt)]
            print('\u001B[12A', end='')
            print('Beam-2l   :  {v_2l:.1f}mV  {c_2l:.1f}uA  {vd_2l:.1f}V  {vg1_2l:.1f}V  {vg2_2l:.1f}V  {id_2l:.1f}mA  {lo_2l:.1f}mA     \n'\
                  'Beam-2r   :  {v_2r:.1f}mV  {c_2r:.1f}uA  {vd_2r:.1f}V  {vg1_2r:.1f}V  {vg2_2r:.1f}V  {id_2r:.1f}mA  {lo_2r:.1f}mA     \n'\
                  'Beam-3l   :  {v_3l:.1f}mV  {c_3l:.1f}uA  {vd_3l:.1f}V  {vg1_3l:.1f}V  {vg2_3l:.1f}V  {id_3l:.1f}mA  {lo_3l:.1f}mA     \n'\
                  'Beam-3r   :  {v_3r:.1f}mV  {c_3r:.1f}uA  {vd_3r:.1f}V  {vg1_3r:.1f}V  {vg2_3r:.1f}V  {id_3r:.1f}mA  {lo_3r:.1f}mA     \n'\
                  'Beam-4l   :  {v_4l:.1f}mV  {c_4l:.1f}uA  {vd_4l:.1f}V  {vg1_4l:.1f}V  {vg2_4l:.1f}V  {id_4l:.1f}mA  {lo_4l:.1f}mA     \n'\
                  'Beam-4r   :  {v_4r:.1f}mV  {c_4r:.1f}uA  {vd_4r:.1f}V  {vg1_4r:.1f}V  {vg2_4r:.1f}V  {id_4r:.1f}mA  {lo_4r:.1f}mA     \n'\
                  'Beam-5l   :  {v_5l:.1f}mV  {c_5l:.1f}uA  {vd_5l:.1f}V  {vg1_5l:.1f}V  {vg2_5l:.1f}V  {id_5l:.1f}mA  {lo_5l:.1f}mA     \n'\
                  'Beam-5r   :  {v_5r:.1f}mV  {c_5r:.1f}uA  {vd_5r:.1f}V  {vg1_5r:.1f}V  {vg2_5r:.1f}V  {id_5r:.1f}mA  {lo_5r:.1f}mA     \n'\
                  'Beam-1lu  :  {v_1lu:.1f}mV  {c_1lu:.1f}uA  {vd_1lu:.1f}V  {vg1_1lu:.1f}V  {vg2_1lu:.1f}V  {id_1lu:.1f}mA  {lo_1l:.1f}mA     \n'\
                  'Beam-1ll  :  {v_1ll:.1f}mV  {c_1ll:.1f}uA  {vd_1ll:.1f}V  {vg1_1ll:.1f}V  {vg2_1ll:.1f}V  {id_1ll:.1f}mA  {lo_1l:.1f}mA     \n'\
                  'Beam-1ru  :  {v_1ru:.1f}mV  {c_1ru:.1f}uA  {vd_1ru:.1f}V  {vg1_1ru:.1f}V  {vg2_1ru:.1f}V  {id_1ru:.1f}mA  {lo_1r:.1f}mA     \n'\
                  'Beam-1rl  :  {v_1rl:.1f}mV  {c_1rl:.1f}uA  {vd_1rl:.1f}V  {vg1_1rl:.1f}V  {vg2_1rl:.1f}V  {id_1rl:.1f}mA  {lo_1r:.1f}mA  '
                  .format(**globals()))
            
            time.sleep(interval)

        
if __name__ == '__main__':
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        pass

    st = beam_monitor()
    st.start_thread()
    rospy.init_node(name)
    sis_vol_sub_list = [rospy.Subscriber('/sis_vol_{}'.format(beam),
                                         Float64,
                                         st.callback_sis_vol,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
    sis_cur_sub_list = [rospy.Subscriber('/sis_cur_{}'.format(beam),
                                         Float64,
                                         st.callback_sis_cur,
                                         callback_args = idx)
                        for idx, beam in enumerate(beam_list)]
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
    rospy.spin()    
