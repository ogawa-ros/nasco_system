import time

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64

name = 'controller'
rospy.init_node(name)

class sg(object):

    def __init__(self):
        self.freq = 0.
        self.power = 0.
        self.onoff = 0

        self.pub_freq = rospy.Publisher(
            name = '/e8257d_freq_cmd',
            data_class = Float64,
            queue_size = 1
            )

        self.pub_power = rospy.Publisher(
            name = '/e8257d_power_cmd',
            data_class = Float64,
            queue_size = 1
            )

        self.pub_onoff = rospy.Publisher(
            name = '/e8257d_onoff_cmd',
            data_class = Int32,
            queue_size = 1
            )

        self.sub_freq = rospy.Subscriber(
            name = '/e8257d_freq',
            data_class = Float64,
            callback = callback_freq
            )

        self.sub_power = rospy.Subscriber(
            name = '/e8257d_power',
            data_class = Float64,
            callback = callback_power
            )

        self.sub_onoff = rospy.Subscriber(
            name = '/e8257d_onoff',
            data_class = Float64,
            callback = callback_onoff
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
    rospy.init(name)
    sg()
    rospy.spin()
