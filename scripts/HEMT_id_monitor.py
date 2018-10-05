import rospy
from std_msgs.msg import Float64
import time

def callback(req, ch):
    time.sleep(1)
    print(ch, ":  ", req)
    return

rospy.init_node('id_monitor')
ch_list = ['2l','2r','3l','3r','4l','4r','5l','5r']
list = []

for ch in ch_list:
    sub = rospy.Subscriber('hemt_{}_id'.format(ch),Float64,callback,callback_args = ch,queue_size =1)

    list.append(sub)

rospy.spin()


