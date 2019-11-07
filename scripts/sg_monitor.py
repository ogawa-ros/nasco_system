import time

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from std_msgs.msg import String


name = 'sg_monitor'


class sg_monitor(object):

    def __init__(self)
        mode_list = ['1st', '2nd_upper', '2nd_lower']

        reta = 1.
        rate_pub = 1e-2
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
            rospy.Publisher('sg_100ghz_{}_freq'.format(_mode), Float64, callback=self.set_100ghz_freq, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_100ghz_power = [
            rospy.Publisher('sg_100ghz_{}_power'.format(_mode), Float64, callback=self.set_100ghz_power, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_100ghz_onoff = [
            rospy.Publisher('sg_100ghz_{}_onoff'.format(_mode), String, callback=self.set_100ghz_onoff, callback_args=_mode)
            for _mode in mode_list]

        self.pub_sg_200ghz_freq = [
            rospy.Publisher('sg_200ghz_{}_freq_web'.format(_mode), Float64, queue_size=1)
            for _mode in mode_list]
        self.pub_sg_200ghz_power = [
            rospy.Publisher('sg_200ghz_{}_power_web'.format(_mode), Float64, queue_size=1)
            for _mode in mode_list]
        self.pub_sg_200ghz_onoff = [
            rospy.Publisher('sg_200ghz_{}_onoff_web'.format(_mode), Int32, queue_size=1)
            for _mode in mode_list]

        self.sub_sg_200ghz_freq = [
            rospy.Publisher('sg_200ghz_{}_freq'.format(_mode), Float64, callback=self.set_200ghz_freq, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_200ghz_power = [
            rospy.Publisher('sg_200ghz_{}_power'.format(_mode), Float64, callback=self.set_200ghz_power, callback_args=_mode)
            for _mode in mode_list]
        self.sub_sg_200ghz_onoff = [
            rospy.Publisher('sg_200ghz_{}_onoff'.format(_mode), Int32, callback=self.set_200ghz_onoff, callback_args=_mode)
            for _mode in mode_list]

    def set_100ghz_freq(self, freq=0., mode):
        idx = mode_list.index(mode)
        self.sg_100ghz_freq[idx] = freq

    def set_100ghz_power(self, power=0., mode):
        idx = mode_list.index(mode)
        self.sg_100ghz_power[idx] = power

    def set_100ghz_onoff(self, onoff=0., mode):
        idx = mode_list.index(mode)
        self.sg_100ghz_onoff[idx] = onoff

    def set_200ghz_freq(self, freq=0., mode):
        idx = mode_list.index(mode)
        self.sg_200ghz_freq[idx] = freq

    def set_200ghz_power(self, power=0., mode):
        idx = mode_list.index(mode)
        self.sg_200ghz_power[idx] = power

    def set_200ghz_onoff(self, onoff=0., mode):
        idx = mode_list.index(mode)
        self.sg_200ghz_onoff[idx] = ofoff

    def web_100ghz_freq(self):
        for i, pub in enumerate(self.pub_sg_100ghz_freq):
            pub.publish(self.sg_100ghz_freq[i])
            time.sleep(rate_pub)
        time.sleep(rate)

    def web_100ghz_power(self):
        for i, pub in enumerate(self.pub_sg_100ghz_power):
            pub.publish(self.sg_100ghz_power[i])
            time.sleep(rate_pub)
        time.sleep(rate)

    def web_100ghz_onoff(self):
        for i, pub in enumerate(self.pub_sg_100ghz_onoff):
            if self.sg_100ghz_onoff[i] == 0: onoff = 'ON'
            else: onoff = 'OFF'
            pub.publish(onoff)
            time.sleep(rate_pub)
        time.sleep(rate)

    def web_200ghz_freq(self):
        for i, pub in enumerate(self.pub_sg_200ghz_freq):
            pub.publish(self.sg_200ghz_freq[i])
            time.sleep(rate_pub)
        time.sleep(rate)

    def web_200ghz_power(self):
        for i, pub in enumerate(self.pub_sg_200ghz_power):
            pub.publish(self.sg_200ghz_power[i])
            time.sleep(rate_pub)
        time.sleep(rate)

    def web_200ghz_onoff(self):
        for i, pub in enumerate(self.pub_sg_200ghz_onoff):
            if self.sg_200ghz_onoff[i] == 0: onoff = 'ON'
            else: onoff = 'OFF'
            pub.publish(onoff)
            time.sleep(rate_pub)
        time.sleep(rate)


if __name__ == '__main__':
    rospy.init_node(name)
    sg_monitor()
    rospy.spin()
