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

    sleep_long = 1
    sleep_short = 0.5

    def __init__(self, rsw_id):
        rospy.init_node(name)
        self.rsw_id = rsw_id
        
        self.axis = ['x', 'y', 'z']
        self.pub_position = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_position_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        self.pub_speed = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_speed_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        
        self.sub_position = [rospy.Subscriber('/cpz7415v_rsw{0}_{1}_position'.format(self.rsw_id, i), Int64, self.callback_position, callback_args= i) for i in self.axis]

        self.sub_XFFTS = rospy.Subscriber('/XFFTS_PM1', Float64, self.callback_XFFTS)
        
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
    def set_position(self, axis = 0, position = 0):
        self.pub_position[axis].publish(position)
        return    

    def set_speed(self, axis = 0, speed = 1000):
        self.pub_speed[axis].publish(speed)
        return    

    def callback_position(self, req, args):
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

    def initialize(self, x_start, y_start, speed, dir):
        axis = [0,1]
        start_pos = [x_start, y_start]
        for axis in axis:
            self.set_speed(axis = axis, speed = speed) #速度設定
            #time.sleep(self.sleep_long)
            self.set_position(axis = axis, position = start_pos[i])


        self.now = datetime.datetime.now()
        
        os.mkdir('{0}/data_at_{1:%Y%m%d-%H%M%S}_test_1'.format(dir, self.now), exist_ok = True)
        os.chdir('{0}/data_at_{1:%Y%m%d-%H%M%S}_test_1'.format(dir, self.now))

        print(pycolor.RED + '\n\n' +
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   Start : Knifeedge Measurement  \n'
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n' +
              '\n\n' + pycolor.ENDC)
        return

    def measure(self, x_start, x_last, y_start, y_last, axis, strk, direction, tool, sleep_measure, beam_num):
        data = []
        if axis == 'x':
            axis_num = 0
            x = x_start
            last = x_last
        elif axis == 'y':
            axis_num =1
            x = y_start
            last = y_last
        elif axis == 'z':
            axis_num = 2
            x = z_start
            last = z_last
        else:
            print('axis error')

        for i in range(x_last - x_start):
            if tool == 'nothing':
                time.sleep(sleep_measure)
                ret_2 = time.time()
                ret_3 = sleep_measure
            elif tool == 'XFFTS':
                ret_2 = self.PM
                ret_3 = beam_num
            else:
                print('tool error')
            
            data.append([x, ret_1,ret_2, ret_3])
            
            numpy.savetxt('{0:%Y%m%d-%H%M%S}_{1}_{2}_{3}.csv'.format(self.now, axis, direction, tool), numpy.array(data), delimiter=',', fmt=['%.0f', '%f', '%f', '%f'])
            self.set_position(axis = axis_num, position = x + strk)
            time.sleep(0.1)

            msg = 'Axis : {0}\nStroke : {1} [mm]\nCoorValue : {0} = {2} [mm]\nDestinate : {0} = {3} [mm]\nRemaining : {0} = {4} [mm]'.format(axis, strk, x, last, last - x)
            print('============'+'Knifeedge Measurement'+'============')
            print(msg)
            print('=========================================\n\n')
            x = x + strk

        return
            
    def finalize(self):
        axis = [0,1]
        final_pos = [0, 190]
        for axis in axis:
            self.set_position(axis = axis, position = final_pos[axis])
        
        print(pycolor.RED + '{0}-axis Measurement finished!!!'format(axis) + pycolor.ENDC)
        return
        
