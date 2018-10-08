import rospy
from std_msgs.msg import Float64
import time


#sis_vol                                                                    

def callback_voltage(req, ch):
    time.sleep(1)
    print(ch,":",req)
    return


rospy.init_node('Monitor')

sis_ch_list = ['2l','2r','3l','3r','4l','4r','5l','5r','1lu','1ll','1ru','1rl']


for ch in sis_ch_list:
    sis_vol_mon = rospy.Subscriber('sis_vol_{}'.format(ch), Float64, callback_voltage,
                                   callback_args  = ch, queue_size = 1)


rospy.spin()
    

#sis_current                                                                

def callback_current(req,ch):
    print(ch,":",req)
    return

for ch in sis_ch_list:
    sis_cur_mon = rospy.Subscriber('sis_cur_{}'.format(ch), Float64, callback_current,
                                   callback_args =ch,queue_size = 1)
rospy.spin()

#loatt_current                                                              

loatt_ch_list = ['2l','2r','3l','3r','4l','4r','5l','5r','1l','1r']



def callback_loatt(req,ch):
    print(cd,":",req)
    return

for _ch in loatt_ch_list:
    loatt_cur_mon = rospy.Subscriber('loatt_{}'.format(_ch), Float64, callback_loatt,
                                     callback_args = ch,queue_size = 1)

rospy.spin()

