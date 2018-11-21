import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import controller
ctrl = controller
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String


beam_list = ['2l','2r','3l','3r',
             '4l','4r','5l','5r']

interval = 5e-3
fixtime = 1.
trigger_wait = 1.5
vg1_wait = 1. # 1. sec
wait = 1.

# hemt_param
initial_voltage = -2.0
final_voltage = 2.0
step = 0.1
roop = int((final_voltage - initial_voltage) / step)
[ctrl.output_hemt_voltage(beam=beam, vd=1.2) for beam in beam_list] # vd

# set_log
msg = String()
f_msg = String()
f_msg.data = ''
flag_name = 'hemt_sweep_trigger'
pub = rospy.Publisher(flag_name, String , queue_size = 1)

# home position
#ctrl.slider.set_position('x', 0)
#print('[INFO] cold position.')
#time.sleep(chopper_wait)

# initialize
# ctrl.output_sis_voltage(config=True)
# ctrl.output_loatt_current(config=True)

try:
    #---
    
    # initialize
    [ctrl.output_hemt_voltage(beam=beam, vg1=initial_voltage) for beam in beam_list] # vg1
    [ctrl.output_hemt_voltage(beam=beam, vg2=initial_voltage) for beam in beam_list] # vg2
    time.sleep(wait)
        
    # set hot
#    ctrl.slider.set_position('x', 100)
 #   print('[INFO] hot position.')    
  #  time.sleep(chopper_wait)

    # start logger
    msg.data = str(time.time())
    pub.publish(msg)
    time.sleep(trigger_wait)

    # HOT
    for vg1 in range(roop+1):
        [ctrl.output_hemt_voltage(beam=beam, vg1=vg1*step+initial_voltage) for beam in beam_list]
        time.sleep(vg1_wait)
        for vg2 in range(roop+1):
            [ctrl.output_hemt_voltage(beam=beam, vg2=vg2*step+initial_voltage) for beam in beam_list]
            time.sleep(fixtime)
    time.sleep(wait)

    # end logger
    pub.publish(f_msg)
    time.sleep(trigger_wait)

except KeyboardInterrupt:
    pub.publish(f_msg)
    [ctrl.output_hemt_voltage(beam=beam, vd=0, vg1=0, vg2=0) for beam in beam_list]
    
# finalize
[ctrl.output_hemt_voltage(beam=beam, vd=0, vg1=0, vg2=0) for beam in beam_list]
