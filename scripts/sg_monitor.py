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
        self.mode_list = ['1st', '2nd_upper', '2nd_lower']
        self.rate = 1.
        self.rate_pub = 1e-1
        self.sg_100ghz_freq = [0., 0., 0.]
        self.sg_100ghz_power = [0., 0., 0.]
        self.sg_100ghz_onoff = [0, 0, 0]
        self.sg_200ghz_freq = [0., 0., 0.]
        self.sg_200ghz_power = [0., 0., 0.]
        self.sg_200ghz_onoff = [0, 0, 0]

        self.pub_sg_100ghz_freq = [
            rospy.Publisher('/sg_100ghz_{}_freq_web'.format(_mode), Float64, queue_size=1)
            for _mode in self.mode_list]
        self.pub_sg_100ghz_power = [
            rospy.Publisher('/sg_100ghz_{}_power_web'.format(_mode), Float64, queue_size=1)
            for _mode in self.mode_list]
        self.pub_sg_100ghz_onoff = [
            rospy.Publisher('/sg_100ghz_{}_onoff_web'.format(_mode), String, queue_size=1)
            for _mode in self.mode_list]

        self.sub_sg_100ghz_freq = [
            rospy.Subscriber('/sg_100ghz_{}_freq'.format(_mode), Float64, self.set_100ghz_freq, callback_args=_mode)
            for _mode in self.mode_list]
        self.sub_sg_100ghz_power = [
            rospy.Subscriber('/sg_100ghz_{}_power'.format(_mode), Float64, self.set_100ghz_power, callback_args=_mode)
            for _mode in self.mode_list]
        self.sub_sg_100ghz_onoff = [
            rospy.Subscriber('/sg_100ghz_{}_onoff'.format(_mode), Int32, self.set_100ghz_onoff, callback_args=_mode)
            for _mode in self.mode_list]

        self.pub_sg_200ghz_freq = [
            rospy.Publisher('/sg_200ghz_{}_freq_web'.format(_mode), Float64, queue_size=1)
            for _mode in self.mode_list]
        self.pub_sg_200ghz_power = [
            rospy.Publisher('/sg_200ghz_{}_power_web'.format(_mode), Float64, queue_size=1)
            for _mode in self.mode_list]
        self.pub_sg_200ghz_onoff = [
            rospy.Publisher('/sg_200ghz_{}_onoff_web'.format(_mode), String, queue_size=1)
            for _mode in self.mode_list]

        self.sub_sg_200ghz_freq = [
            rospy.Subscriber('/sg_200ghz_{}_freq'.format(_mode), Float64, self.set_200ghz_freq, callback_args=_mode)
            for _mode in self.mode_list]
        self.sub_sg_200ghz_power = [
            rospy.Subscriber('/sg_200ghz_{}_power'.format(_mode), Float64, self.set_200ghz_power, callback_args=_mode)
            for _mode in self.mode_list]
        self.sub_sg_200ghz_onoff = [
            rospy.Subscriber('/sg_200ghz_{}_onoff'.format(_mode), Int32, self.set_200ghz_onoff, callback_args=_mode)
            for _mode in self.mode_list]

    def set_100ghz_freq(self, freq, mode):
        idx = self.mode_list.index(mode)
        self.sg_100ghz_freq[idx] = freq

    def set_100ghz_power(self, power, mode):
        idx = self.mode_list.index(mode)
        self.sg_100ghz_power[idx] = power

    def set_100ghz_onoff(self, onoff, mode):
        idx = self.mode_list.index(mode)
        self.sg_100ghz_onoff[idx] = int(onoff.data)

    def set_200ghz_freq(self, freq, mode):
        idx = self.mode_list.index(mode)
        self.sg_200ghz_freq[idx] = freq

    def set_200ghz_power(self, power, mode):
        idx = self.mode_list.index(mode)
        self.sg_200ghz_power[idx] = power

    def set_200ghz_onoff(self, onoff, mode):
        idx = self.mode_list.index(mode)
        self.sg_200ghz_onoff[idx] = int(onoff.data)

    def web_100ghz_freq(self):
        while True:
            for i, pub in enumerate(self.pub_sg_100ghz_freq):
                pub.publish(self.sg_100ghz_freq[i])
                time.sleep(self.rate_pub)
            time.sleep(self.rate)

    def web_100ghz_power(self):
        while True:
            for i, pub in enumerate(self.pub_sg_100ghz_power):
                pub.publish(self.sg_100ghz_power[i])
                time.sleep(self.rate_pub)
            time.sleep(self.rate)

    def web_100ghz_onoff(self):
        while True:
            for i, pub in enumerate(self.pub_sg_100ghz_onoff):
                if self.sg_100ghz_onoff[i] == 0: onoff = 'OFF'
                elif self.sg_100ghz_onoff[i] == 1: onoff = 'ON'
                pub.publish(onoff)
                time.sleep(self.rate_pub)
            time.sleep(self.rate)

    def web_200ghz_freq(self):
        while True:
            for i, pub in enumerate(self.pub_sg_200ghz_freq):
                pub.publish(self.sg_200ghz_freq[i])
                time.sleep(self.rate_pub)
            time.sleep(self.rate)

    def web_200ghz_power(self):
        while True:
            for i, pub in enumerate(self.pub_sg_200ghz_power):
                pub.publish(self.sg_200ghz_power[i])
                time.sleep(self.rate_pub)
            time.sleep(self.rate)

    def web_200ghz_onoff(self):
        while True:
            for i, pub in enumerate(self.pub_sg_200ghz_onoff):
                if self.sg_200ghz_onoff[i] == 0: onoff = 'OFF'
                elif self.sg_200ghz_onoff[i] == 1: onoff = 'ON'
                pub.publish(onoff)
                time.sleep(self.rate_pub)
            time.sleep(self.rate)

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
    rospy.init_node(name)
    sg = sg_monitor()
    sg.start_thread()
    rospy.spin()
