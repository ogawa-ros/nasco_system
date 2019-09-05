import time

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64

name = 'controller'
rospy.init_node(name)

class controller(object):

    def __init__(self, model='e8257d'):
        self.freq = 0.
        self.power = 0.
        self.onoff = 0

        self.pub_freq = rospy.Publisher(
            name = '/{}_freq_cmd'.format(model),
            data_class = Float64,
            queue_size = 1
            )

        self.pub_power = rospy.Publisher(
            name = '/{}_power_cmd'.format(model),
            data_class = Float64,
            queue_size = 1
            )

        self.pub_onoff = rospy.Publisher(
            name = '/{}_onoff_cmd'.format(model),
            data_class = Int32,
            queue_size = 1
            )


        self.sub_freq = rospy.Subscriber(
            name = '/{}_freq'.format(model),
            data_class = Float64,
            callback = self.callback_freq
            )

        self.sub_power = rospy.Subscriber(
            name = '/{}_power'.format(model),
            data_class = Float64,
            callback = self.callback_power
            )

        self.sub_onoff = rospy.Subscriber(
            name = '/{}_onoff'.format(model),
            data_class = Int32,
            callback = self.callback_onoff
            )

    def set_freq(self, freq=0.):
        self.pub_freq.publish(freq)
        return

    def set_power(self, power=0.):
        self.pub_power.publish(power)
        return

    def set_onoff(self, onoff=0):
        self.pub_onoff.publish(onoff)
        return

    def get_freq(self):

        return self.freq

    def get_power(self):

        return self.power

    def get_onoff(self):

        return self.onoff

    def callback_freq(self, q):
        self.freq = q.data
        return

    def callback_power(self, q):
        self.power = q.data
        return

    def callback_onoff(self, q):
        self.onoff = q.data
        return

if __name__ == '__main__':
    rospy.init_node(name)
    controller()
    rospy.spin()
