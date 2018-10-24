import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import controller as ctrl
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String



beam_list = ['2l','2r','3l','3r',
             '4l','4r','5l','5r']

interval = 5e-3
fixtime = 1
chopper_wait = 10


# Set Param

ctrl.output_sis_voltage(config = True)
ctrl.output_loatt_current(config = True)


# Set chopper

#cf = 90/36*100 #degree conversion
#mc_msg = int   
#mc_msg.data = cf
#pub_mc = rospy.Pubilsher('7415_rsw0_z_position_cmd', int64 ,queue_size = 1)

# hemt_param

initial_voltage = -2
final_voltage = 2
step = 0.1
#set_log                                                                                                                                                                          
msg = String()
msg.data = str(time.time())
f_msg = String()
f_msg.data = ''
flag_name = 'hemt_sweep_trigger'
pub = rospy.Publisher(flag_name, String , queue_size = 1)
time.sleep(1.5)

try:

    for i in range(0,3,2):
        pub.publish(msg)
        time.sleep(1)
        #HOT
        for vol1 in range(int((initial_voltage + i)/step) ,int((initial_voltage + i+2)/step)):
            for vol2 in range(-20, 21):
                for _ in beam_list:
                    ctrl.output_hemt_voltage(beam = _, vd = 1.2 , vg1 = vol1*step, vg2 = vol2*step)

                time.sleep(interval)
            time.sleep(fixtime)
        time.sleep(fixtime)

        pub.publish(f_msg)  #HOT finish

        #pub_mc.publish(mc_msg)  #COLD Set
        time.sleep(chopper_wait)

        pub.publish(msg)
        time.sleep(1)

        #COLD                                             
        for vol1 in range(int((initial_voltage + i)/step) ,int((initial_voltage + i+2)/step)):
            for vol2 in range(-20, 21):
                for _ in beam_list:
                    ctrl.output_hemt_voltage(beam = _, vd = 1.2 , vg1 = vol1*step, vg2 = vol2*step)

                time.sleep(interval)
            time.sleep(fixtime)
        time.sleep(fixtime)


        pub.publish(f_msg)
        time.sleep(1)
        
        #pub_mc.publish(mc_msg)
        time.sleep(chopper_wait)

except KeyboardInterrupt:
    pub.publish(f_msg)

    for _ in beam_list:
        ctrl.output_hemt_voltage(beam = _, vd = 0, vg1 = 0, vg2 = 0)
        time.sleep(interval)

for _ in beam_list:
    ctrl.output_hemt_voltage(beam = _, vd = 0, vg1 = 0, vg2 = 0)
    time.sleep(interval)




    