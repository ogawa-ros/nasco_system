#!/usr/bin/env python3

name = "slider_controller"

import os, sys, numpy, time, datetime, threading

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Float64
from std_msgs.msg import Bool

class pycolor(object):
    #表示の色
    RED = '\033[31m'
    ENDC = '\033[0m'


class slider(object):
    p = [1, 1, 0]

    PM=0
    PM1=0
    PM2=0

    #sleep_long = 3
    #sleep_short = 2

    def __init__(self, rsw_id):
        rospy.init_node(name)
        
        self.rsw_id = rsw_id
        
        self.axis = ['x', 'y', 'z']
        self.pub_step = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_step_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        self.pub_speed = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_speed_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        self.pub_do = [rospy.Publisher('/cpz7415v_rsw{0}_do_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        
        self.sub_step = [rospy.Subscriber('/cpz7415v_rsw{0}_{1}_step'.format(self.rsw_id, i), Int64, self.callback_step, callback_args= i) for i in self.axis]

        self.sub_XFFTS = [rospy.Subscriber('/xffts_power_board{0}s'.format(i+1), Float64, self.callback_XFFTS, callback_args = i) for i in range(0,16,1)]
        
        self.sub_PM1 = rospy.Subscriber('/power_1', Float64, self.callback_PM1)
        self.sub_PM2 = rospy.Subscriber('/power_2', Float64, self.callback_PM2)
       
        
        sub_th = threading.Thread(
                target = self.sub_function,
                daemon = True
                )
        sub_th.start()
        pass

    def sub_function(self):
        rospy.spin()
        return

        '''
        axis
        x : 0
        y : 1
        z : 2
        '''
    def set_step(self, axis = 0, step = 0):
        self.pub_step[axis].publish(step * 100)
        return       

    def callback_step(self, req, args):
        if args == "x":
            self.p[0] = req.data/100
        if args == "y":
            self.p[1] = req.data/100
        if args == "z":
            self.p[2] = req.data/100
        return

    def callback_XFFTS(self, req, args):
        self.PM[args] = req.data
        return
        
    def callback_PM1(self, req):
        self.PM1 = req.data
        return
        
    def callback_PM2(self, req):
        self.PM2 = req.data
        return

    def initialize(self, dir):
        axis = [0,1]
        start_pos = [0,0]

        for axis, pos in zip(axis, start_pos):
            self.set_step(axis = axis, step = pos)
            while pos!= self.p[axis]:
                time.sleep(0.01)
                continue
        self.now = datetime.datetime.now()
        os.makedirs('{0}/data_at_{1:%Y%m%d-%H%M%S}'.format(dir, self.now), exist_ok = True)
        os.chdir('{0}/data_at_{1:%Y%m%d-%H%M%S}'.format(dir, self.now))

        print(pycolor.RED + '\n\n' +
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   Start : Knifeedge Measurement  \n'
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n' +
              '\n\n' + pycolor.ENDC)
        return

    def measure(self, start, last, axis, strk, direction, sleep_measure):
        data = []
        x = start
        if axis == 'x':
            axis_num = 0
        elif axis == 'y':
            axis_num = 1
        else:
            print('axis error')
        
        for i in range(int(abs((last - start)/strk + 1))):
            print(x, self.p)
            if rospy.is_shutdown(): return
            
            while x!=self.p[axis_num]:
                time.sleep(0.001)
                continue

            ret_1 = time.time()
            #time.sleep(sleep_measure):ROACH使用時に入れる
            ret_5 = self.PM
            ret_3 = self.PM1
            ret_4 = self.PM2
            ret_6 = 0 #sleep_measure
            ret_2 = time.time()
            
            data.append([x, ret_1,ret_2, ret_3, ret_4, ret_5, ret_6])
            
            numpy.savetxt('{0:%Y%m%d-%H%M%S}_{1}_{2}.csv'.format(self.now, axis, direction), numpy.array(data), delimiter=',', fmt=['%.0f', '%f', '%f', '%f', '%f', '%f','%f'])

            #msg = 'Axis : {0}\nStroke : {1} [mm]\nCoorValue : {0} = {2} [mm]\nDestinate : {0} = {3} [mm]\nRemaining : {0} = {4} [mm]\nx = {5}'.format(axis, strk, self.p[axis_num], last, last - x, x)
            #print('============'+'Knifeedge Measurement'+'============')
            #print(msg)
            #print('=========================================\n\n')
            x = x + strk
            self.set_step(axis = axis_num, step = int(x))
            time.sleep(sleep_measure)
            

        return
            
    def finalize(self):
        axis = [0,1]
        final_pos = [0, 0]
        for axis, pos in zip(axis, final_pos):
            self.set_step(axis = axis, step = pos)
            while pos!= self.p[axis]:
                time.sleep(0.001)
                continue
        print(pycolor.RED + 'Measurement finished!!!' + pycolor.ENDC)
        return

    def M4(self, mo = 'IN'):
        '''
        M4の駆動を行う
        M4が最も下の位置にある時を'OUT',
        M4が200 mm上にある時を'IN'とする。
        '''

        if mo == 'IN':
            self.set_step(axis = 2, step = 200) #z軸使用を想定

        else:
            self.set_step(axis = 2, step = 0) #z軸使用を想定

        return

    def M4_initalize(self):
        '''
        M4の位置をシリンダーの原点に戻す。
        M4の電源を入れ直した時、
        countの値が0の時のみ行ってください。
        '''

        self.pub_do[2].publish(1)
        time.sleep(5)
        self.pub_do[2].publish(0)
        return
