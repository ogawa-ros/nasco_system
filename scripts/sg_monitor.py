#!/usr/bin/env python3

import time
import threading

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from std_msgs.msg import String


name = 'sg_monitor'


class sg_monitor(object):
    def __init__(self):
        mode_list = ['1st', '2nd_upper', '2nd_lower']

        reta = 1.
        rate_pub = 5e-2
        self.sg_100ghz_freq = [0., 0., 0.]
        self.sg_100ghz_power = [0., 0., 0.]
        self.sg_100ghz_onoff = [0, 0, 0]
        self.sg_200ghz_freq = [0., 0., 0.]
        self.sg_200ghz_power = [0., 0., 0.]
        self.sg_200ghz_onoff = [0, 0, 0]

        self.pub_sg_100ghz_freq = [
            rospy.Publisher('sg_100ghz_{}_freq_web'.format(_mode), Float64, queue_size=1)
            for _mode in mode_list]
        self.pub_sg_100ghz_power = [
            rospy.Publisher('sg_100ghz_{}_power_web'.format(_mode), Float64, queue_size=1)
            for _mode in mode_list]
        self.pub_sg_100ghz_onoff = [
            rospy.Publisher('sg_100ghz_{}_onoff_web'.format(_mode), String, queue_size=1)
            for _mode in mode_list]

        self.sub_sg_100ghz_freq = [
            rospy.Subscriber('sg_100ghz_{}_freq'.format(_mode), Float64, self.set_100ghz_freq, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_100ghz_power = [
            rospy.Subscriber('sg_100ghz_{}_power'.format(_mode), Float64, self.set_100ghz_power, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_100ghz_onoff = [
            rospy.Subscriber('sg_100ghz_{}_onoff'.format(_mode), Int32, self.set_100ghz_onoff, callback_args=_mode)
            for _mode in mode_list]

        self.pub_sg_200ghz_freq = [
            rospy.Publisher('sg_200ghz_{}_freq_web'.format(_mode), Float64, queue_size=1)
            for _mode in mode_list]
        self.pub_sg_200ghz_power = [
            rospy.Publisher('sg_200ghz_{}_power_web'.format(_mode), Float64, queue_size=1)
            for _mode in mode_list]
        self.pub_sg_200ghz_onoff = [
            rospy.Publisher('sg_200ghz_{}_onoff_web'.format(_mode), String, queue_size=1)
            for _mode in mode_list]

        self.sub_sg_200ghz_freq = [
            rospy.Subscriber('sg_200ghz_{}_freq'.format(_mode), Float64, self.set_200ghz_freq, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_200ghz_power = [
            rospy.Subscriber('sg_200ghz_{}_power'.format(_mode), Float64, self.set_200ghz_power, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_200ghz_onoff = [
            rospy.Subscriber('sg_200ghz_{}_onoff'.format(_mode), Int32, self.set_200ghz_onoff, callback_args=_mode)
            for _mode in mode_list]

    def set_100ghz_freq(self, freq=0., mode=''):
        idx = mode_list.index(mode)
        self.sg_100ghz_freq[idx] = freq

    def set_100ghz_power(self, power=0., mode=''):
        idx = mode_list.index(mode)
        self.sg_100ghz_power[idx] = power

    def set_100ghz_onoff(self, onoff=0., mode=''):
        idx = mode_list.index(mode)
        self.sg_100ghz_onoff[idx] = onoff

    def set_200ghz_freq(self, freq=0., mode=''):
        idx = mode_list.index(mode)
        self.sg_200ghz_freq[idx] = freq

    def set_200ghz_power(self, power=0., mode=''):
        idx = mode_list.index(mode)
        self.sg_200ghz_power[idx] = power

    def set_200ghz_onoff(self, onoff=0., mode=''):
        idx = mode_list.index(mode)
        self.sg_200ghz_onoff[idx] = onoff

    def web_100ghz_freq(self):
        while True:
            for i, pub in enumerate(self.pub_sg_100ghz_freq):
                pub.publish(self.sg_100ghz_freq[i])
                time.sleep(rate_pub)
            time.sleep(rate)

    def web_100ghz_power(self):
        while True:
            for i, pub in enumerate(self.pub_sg_100ghz_power):
                pub.publish(self.sg_100ghz_power[i])
                time.sleep(rate_pub)
            time.sleep(rate)

    def web_100ghz_onoff(self):
        while True:
            for i, pub in enumerate(self.pub_sg_100ghz_onoff):
                if self.sg_100ghz_onoff[i] == 0: onoff = 'ON'
                else: onoff = 'OFF'
                pub.publish(onoff)
                time.sleep(rate_pub)
            time.sleep(rate)

    def web_200ghz_freq(self):
        while True
            for i, pub in enumerate(self.pub_sg_200ghz_freq):
                pub.publish(self.sg_200ghz_freq[i])
                time.sleep(rate_pub)
            time.sleep(rate)

    def web_200ghz_power(self):
        while True:
            for i, pub in enumerate(self.pub_sg_200ghz_power):
                pub.publish(self.sg_200ghz_power[i])
                time.sleep(rate_pub)
            time.sleep(rate)

    def web_200ghz_onoff(self):
        while True:
            for i, pub in enumerate(self.pub_sg_200ghz_onoff):
                if self.sg_200ghz_onoff[i] == 0: onoff = 'ON'
                else: onoff = 'OFF'
                pub.publish(onoff)
                time.sleep(rate_pub)
            time.sleep(rate)

    def start_thread(self):
        th_100ghz_freq = threading.Thread(target=self.web_100ghz_freq)
        th_100ghz_freq.setDaemon(True)
        th_100ghz_freq.start()
        th_100ghz_power = threading.Thread(target=self.web_100ghz_power)
        th_100ghz_power.setDaemon(True)
        th_100ghz_power.start()
        th_100ghz_onoff = threading.Thread(target=self.web_100ghz_onoff)
        th_100ghz_onoff.setDaemon(True)
        th_100ghz_onoff.start()

        th_200ghz_freq = threading.Thread(target=self.web_200ghz_freq)
        th_200ghz_freq.setDaemon(True)
        th_200ghz_freq.start()
        th_200ghz_power = threading.Thread(target=self.web_200ghz_power)
        th_200ghz_power.setDaemon(True)
        th_200ghz_power.start()
        th_200ghz_onoff = threading.Thread(target=self.web_200ghz_onoff)
        th_200ghz_onoff.setDaemon(True)
        th_200ghz_onoff.start()


if __name__ == '__main__':
    sg = sg_monitor()
    sg.start_thread()
    rospy.init_node(name)
    rospy.spin()
