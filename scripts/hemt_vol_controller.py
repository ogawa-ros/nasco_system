import time
import rospy
from std_msgs.msg import Float64


name = 'hemt_vol_controller'
rospy.init_node(name)

hemt_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

topic_list_vd = ['/hemt_{}_vd_cmd'.format(_) for _ in hemt_list]
topic_list_vg1 = ['/hemt_{}_vg1_cmd'.format(_) for _ in hemt_list]
topic_list_vg2 = ['/hemt_{}_vg2_cmd'.format(_) for _ in hemt_list]
pub_list_vd = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list_vd]
pub_list_vg1 = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list_vg1]
pub_list_vg2 = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list_vg2]


def output_voltage(hemt='', vd = 0.0, vg1 = 0.0, vg2 = 0.0):
    msg = Float64()
    msg.data = vd
    pub = pub_list_vd[hemt_list.index(hemt)]
    pub.publish(msg)
    
    msg = Float64()
    msg.data = vg1
    pub = pub_list_vg1[hemt_list.index(hemt)]
    pub.publish(msg)
    
    msg = Float64()
    msg.data = vg2
    pub = pub_list_vg2[hemt_list.index(hemt)]
    pub.publish(msg)
    time.sleep(1e-3) # 1 msec.
