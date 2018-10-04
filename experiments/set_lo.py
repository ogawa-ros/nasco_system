# LO

import time
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32

interval = 2

rospy.init_node('lo_set')

pub_freq = rospy.Publisher('/lo_1st_freq_cmd', Float64, queue_size=1)
pub_power = rospy.Publisher('/lo_1st_power_cmd', Float64, queue_size=1)
pub_onoff = rospy.Publisher('/lo_1st_onoff_cmd', Int32, queue_size=1)
time.sleep(2)

freq, power, onoff = Float64(), Float64(), Int32()
freq.data, power.data, onoff.data = 17.5, 0., 1
time.sleep(interval)
pub_freq.publish(freq)
time.sleep(interval)
pub_power.publish(power)
time.sleep(interval)
pub_onoff.publish(onoff)
time.sleep(interval)

for i in range(1, 17):
    power = Float64()
    power.data = float(i)
    pub_power.publish(power)
    time.sleep(1)

power = Float64()
power.data = 17.3
pub_power.publish(power)
