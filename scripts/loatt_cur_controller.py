import time
import rospy
from std_msgs.msg import Float64


name = 'loatt_cur_controller'
rospy.init_node(name)

loatt_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1l', '1r']

loatt_list_out = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ru']

topic_list = ['/loatt_{}_cmd'.format(_) for _ in loatt_list] 
pub_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list]


def output_current(loatt='', current=0.):
    msg = Float64()
    msg.data = current
    pub = pub_list[loatt_list_out.index(loatt)]
    pub.publish(msg)
    time.sleep(1e-3) # 1 msec.
