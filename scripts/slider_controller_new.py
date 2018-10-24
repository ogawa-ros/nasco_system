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
    move_onoff = [False, False, False] # x y z
    
    sleep_long = 1
    sleep_short = 0.5

    def __init__(self):
        rospy.init_node(name)
        self.rsw_id = input("rsw_id(0 or 1): ")
        
        self.axis = ['x', 'y', 'z']
        self.pub_ptp_onoff = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_ptp_onoff_cmd'.format(self.rsw_id, i), Bool, queue_size=1) for i in self.axis]
        self.pub_length = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_pulse_num_cmd'.format(self.rsw_id, i), Int64, queue_size=1) for i in self.axis]
        self.pub_speed = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_fh_speed_cmd'.format(self.rsw_id, i),Int64, queue_size=1) for i in self.axis]
        self.pub_home = [rospy.Publisher('/cpz7415v_rsw{0}_{1}_move_to_home'.format(self.rsw_id, i), Bool, queue_size=1) for i in self.axis]
        
        self.sub = [rospy.Subscriber('/cpz7415v_rsw0_{}_onoff'.format(i), Bool, self.callback, callback_args = i) for i in self.axis]
        self.sub_XFFTS = rospy.Subscriber('/XFFTS_PM1', Float64, self.callback_XFFTS)
        sub_th = threading.Thread(
                target = self.sub_function,
                daemon = True,
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
    def ptp_onoff(self, axis = 0, onoff = 1):
        self.pub_ptp_onoff[axis].publish(onoff)
        return
        
    def set_length(self, axis = 0, len = 1):
        self.pub_length[axis].publish(len * 100)
        return

    def set_speed(self, axis = 0, speed = 1000):
        self.pub_speed[axis].publish(speed)
        return    

    def move_to_home(self, axis = 'x', cmd = True):
        self.pub_home[axis].publish(cmd)
        return

    def callback(self, req, axis):
        if axis == "x":
            self.move_onoff[0] = req.data # True/False
        if axis == "y":
            self.move_onoff[1] = req.data
        if axis == "z":
            self.move_onoff[2] = req.data
        return
        
    def callback_XFFTS(self, req):
        self.PM = req.data
        return

    def initialize(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test'):
        axis = [0,1]
        for i in axis:
            self.set_speed(axis = axis, speed = speed) #速度設定
            self.move_to_home(axis = axis, cmd = True) #原点復帰
            time.sleep(self.sleep_long)
            
            self.last_x = x + length * strk #xの座標の最大値
            self.last_y = y + length * strk #yの座標の最大値
            #last_z = z + length * strk #zの座標の最大値
            
            self.now = datetime.datetime.now()
        
        os.mkdir('{0}/data_at_{1:%Y%m%d-%H%M%S}_test_1'.format(dir, now), exist_ok = True)
        os.chdir('{0}/data_at_{1:%Y%m%d-%H%M%S}_test_1'.format(dir, now))

        print(pycolor.RED + '\n\n' +
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
              '   Start : Knifeedge Measurement  \n'
              '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'.format(x, last_x) +
              '\n\n' + pycolor.ENDC)
        return

	def on_ptp(self, axis = 0, len = 1):
    	self.set_length(axis = axis, len = len)
		self.ptp_onoff(axis_num = axis, onoff = 1)

        while self.move_onoff[axis] == True:
        	time.sleep(0.1)
            continue
        return

	def measure(self, x = 90, y = 30, length = 70, axis = 'x', strk = 1, direction = 'ccw', tool = 'nothing', sleep_measure = 5, beam_num = 'nothing'):
		data = []
		if axis == 'x':
			axis_num = 0
			x = x
			last = self.last_x
		elif axis == 'y':
			axis_num =1
			x = y
			last = self.last_y
		elif axis == 'z':
			axis_num = 2
			x = z
			last = self.last_z
		else:
			print('axis error')
			
		self.set_length(axis = axis_num, len = 1)
		
		for i in range(length+1):
           
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
            
            numpy.savetxt('{0:%Y%m%d-%H%M%S}_{1}_{2}_{3}.csv'.format(now, axis, direction, tool), numpy.array(data), delimiter=',', fmt=['%.0f', '%f', '%f', '%f'])
            self.ptp_onoff(axis_num = 0, onoff = 1)

            while self.move_onoff[axis_num] == True:
                time.sleep(0.1)
                continue

            msg = 'Axis : {0}\nStroke : {1} [mm]\nCoorValue : {0} = {2} [mm]\nDestinate : {0} = {3} [mm]\nRemaining : {0} = {4} [mm]'.format(axis, strk, x, last, last - x)
            print('============'+'Knifeedge Measurement'+'============')
            print(msg)
        print('=========================================\n\n')
            x = x + strk
            return
            
	def finalize(self):
        axis = [0,1]
        for i in axis:
			self.move_to_home(axis = axis, cmd = True) #原点復帰
        	
        print(pycolor.RED + '{0}-axis Measurement finished!!!'format(axis) + pycolor.ENDC)
        return
        
    
        
	def slide_x_go(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 0, len = x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	def slide_x_back(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 0, len = self.last_x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	
	def slide_y_back(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 1, len = -y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = -strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
	
	def slide_y_go(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing',sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 1, len = 190 - self.last_y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return	
		
	def slide_x_lap(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 0, len = self.last_x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.on_ptp(axis = 0, len = - strk)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	def slide_y_lap(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 1, len = -y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.on_ptp(axis = 1, len = strk)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	def slide_xy_lap(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 0, len = self.last_x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.on_ptp(axis = 0, len = - strk)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.move_to_home(axis = 'x', cmd = True)
		time.sleep(self.sleep_long)
		self.on_ptp(axis = 1, len = -y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.on_ptp(axis = 1, len = strk)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	def slide_yx_lap(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 1, len = -y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.on_ptp(axis = 1, len = strk)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.move_to_home(axis = 'y', cmd = True)
		time.sleep(self.sleep_long)
		self.on_ptp(axis = 0, len = self.last_x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.on_ptp(axis = 0, len = - strk)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	def slide_x_go_y_back(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 0, len = self.last_x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.move_to_home(axis = 'x', cmd = True)
		time.sleep(self.sleep_long)
		self.on_ptp(axis = 1, len = -y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
		
	def slide_y_back_x_go(self, x = 90, y = 30, length = 70, strk = 1 ,speed = 1000, tool = 'nothing', sleep_measure = 5, dir = '/home/amigos/beam_pattern/data/2018_10_20_script_test', beam_num = 'nothing'):
		self.initialize(x = x, y = y, length = length, strk = strk ,speed = speed, dir = dir)
		self.on_ptp(axis = 1, len = -y)
		self.measure(x = x, y = y, length = length, axis = 'y', strk = - strk, direction = 'cw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.move_to_home(axis = 'y', cmd = True)
		time.sleep(self.sleep_long)
		self.on_ptp(axis = 0, len = self.last_x)
		self.measure(x = x, y = y, length = length, axis = 'x', strk = strk, direction = 'ccw', tool = tool, sleep_measure = sleep_measure, beam_num = beam_num)
		self.finalize()
		return
    
