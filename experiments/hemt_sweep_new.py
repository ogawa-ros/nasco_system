import sys
import time
sys.path.append('/home/necst/ros/src/nasco_system/scripts')
import controller as ctrl
import pyinterface
import rospy
from std_msgs.msg import Float64

mc_board_name = 7415
mc = pyinterface.open(mc_board_name ,1)

beam_list = ['2l','2r','3l','3r',
             '4l','4r','5l','5r']

interval = 5e-3
fixtime = 1
chopper_wait = 10


# Set Param

ctrl.output_sis_voltage(config = True)
ctrl.output_loatt_current(config = True)


# Set chopper                                                                                                                                                                     
mc.initializer()
mc.set_mode(mode=['PTP'],axis='z')
mc.set_length(length=[90/36],axis = 'z')


# hemt_param

inital_voltege = -2
final_voltage = 2

#set_log                                                                                                                                                                          
msg = String()
msg.data = str(time.time())
f_msg = String()
f_msg.data = ''
fleg_name = 'hemt_sweep_trigger'
pub = rospy.Publisher(flag_name, String , queue_size = 1)
time.sleep(1.5)

try:
    for i in range(0,3,2):
        pub.publish(msg)
        time.sleep(1)

        #HOT
        for vol1 in range(initial_voltage + i ,initial_voltage + i+2):
            for vol2 in range(initial_voltage + i , initial_voltage + i+1):
                for _ in beam_list:
                    ctrl.output_hemt_voltage(beam = _, vd = 1.2 , vg1 = vol1*step+intial_volatge, vg2 = vol2*step+intial_volatge)

                time.sleep(interval)
            time.sleep(fixtime)
        time.sleep(fixtime)

        pub.publish(f_msg)

        mc.move(axis = 'z')
        time.sleep(chopper_wait)

        pub.publish(f_msg)
        time.sleep(1)

        #COLD                                             
        for vol1 in range(initial_voltage + i ,initial_voltage + i+2):
            for vol2 in range(initial_voltage + i , initial_voltage + i+1):
                for _ in beam_list:
                    ctrl.output_hemt_voltage(beam = _, vd = 1.2 , vg1 = vol1*step+intial_volatge, vg2 = vol2*step+intial_volatge)

                time.sleep(interval)
            time.sleep(fixtime)
        time.sleep(fixtime)


        pub.publish(f_msg)


        mc.move(axis = 'z')
        time.sleep(chopper_wait)

except KeyboardInterrupt:
    pub.publish(f_msg)

    for _ in beam_list:
        ctrl.output_hemt_voltage(beam = _, vd = 0, vg1 = 0, vg2 = 0)
        time.sleep(interval)

for _ in beam_list:
    ctrl.output_hemt_voltage()ctrl.output_hemt_voltage(beam = _, vd = 0, vg1 = 0, vg2 = 0)
    time.sleep(interval)




    
