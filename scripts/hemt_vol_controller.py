import time
import rospy
from std_msgs.msg import Float64


name = 'hemt_vol_controller'
rospy.init_node(name)

hemt_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

topic_list = ['/hemt_vol_{}_cmd'.format(_) for _ in hemt_list]
pub_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list]


def output_voltage(hemt='', voltage=0.):
    msg = Float64()
    msg.data = voltage
    pub = pub_list[hemt_list.index(hemt)]
    pub.publish(msg)
    time.sleep(1e-3) # 1 msec.
