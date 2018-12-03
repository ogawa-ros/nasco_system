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
    p = [0, 0, 0]

    sleep_long = 3
    sleep_short = 2

    def __init__(self, rsw_id):
        rospy.init_node(name)
        
        self.rsw_id = rsw_id
        
        self.axis = ['x', 'y', 'z']
        self.pub_step = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_step_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        self.pub_speed = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_speed_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        
        self.sub_step = [rospy.Subscriber('/cpz7415v_rsw{0}_{1}_step'.format(self.rsw_id, i), Int64, self.callback_step, callback_args= i) for i in self.axis]

        self.sub_XFFTS = rospy.Subscriber('/XFFTS_PM1', Float64, self.callback_XFFTS)
        
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
            self.p[0] = req.data
        if args == "y":
            self.p[1] = req.data
        if args == "z":
            self.p[2] = req.data
        return

    def callback_XFFTS(self, req):
        self.PM = req.data
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
            time.sleep(self.sleep_long)

        self.now = datetime.datetime.now()
        os.makedirs('{0}/data_at_{1:%Y%m%d-%H%M%S}'.format(dir, self.now), exist_ok = True)
        os.chdir('{0}/data_at_{1:%Y%m%d-%H%M%S}'.format(dir, self.now))

        print(pycolor.RED + '\n\n' +
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   Start : Knifeedge Measurement  \n'
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n' +
              '\n\n' + pycolor.ENDC)
        time.sleep(self.sleep_long)
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
            if rospy.is_shutdown(): return
            ret_1 = time.time()
            time.sleep(sleep_measure)
            ret_5 = self.PM
            ret_3 = self.PM1
            ret_4 = self.PM2
            ret_6 = sleep_measure
            ret_2 = time.time()
            
            data.append([x, ret_1,ret_2, ret_3, ret_4, ret_5, ret_6])
            
            numpy.savetxt('{0:%Y%m%d-%H%M%S}_{1}_{2}.csv'.format(self.now, axis, direction), numpy.array(data), delimiter=',', fmt=['%.0f', '%f', '%f', '%f', '%f', '%f','%f'])

            msg = 'Axis : {0}\nStroke : {1} [mm]\nCoorValue : {0} = {2} [mm]\nDestinate : {0} = {3} [mm]\nRemaining : {0} = {4} [mm]\nx = {5}'.format(axis, strk, self.p[axis_num], last, last - x, x)
            print('============'+'Knifeedge Measurement'+'============')
            print(msg)
            print('=========================================\n\n')
            x = x + strk
            self.set_step(axis = axis_num, step = int(x))
            time.sleep(self.sleep_short)

        return
            
    def finalize(self):
        axis = [0,1]
        final_pos = [0, 0]
        for axis, pos in zip(axis, final_pos):
            self.set_step(axis = axis, step = pos)
            time.sleep(self.sleep_long)
        print(pycolor.RED + 'Measurement finished!!!' + pycolor.ENDC)
        return
