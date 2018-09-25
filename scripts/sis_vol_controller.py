import time
import rospy
from std_msgs.msg import Float64


name = 'sis_vol_controller'
rospy.init_node(name)

sis_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

topic_list = ['/sis_vol_{}_cmd'.format(_) for _ in sis_list]
pub_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list]


def output_voltage(sis='', voltage=0.):
    msg = Float64()
    msg.data = voltage
    pub = pub_list[sis_list.index(sis)]
    pub.publish(msg)
    time.sleep(1 * 10 ** (-3))
