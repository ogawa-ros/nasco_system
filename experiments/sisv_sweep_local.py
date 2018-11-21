#!/usr/bin/env python3
import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
ctrl = nasco_controller.controller()
import rospy
from std_msgs.msg import String


beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']
beam_num = 12

initial_voltage = 6  # mV
final_voltage =  9     # mV
#step = 0.1             # mV
step = 0.05            # for gpib
interval = 5e-3        # 5 msec.
fixtime = 3.           # 1 sec.
#fixtime = 5.           # for gpib
roop = int((final_voltage - initial_voltage) / step)

# Start Chopper


# Set Param
ctrl.loatt.output_loatt_current_config()
#ctrl.set_1st_lo(config=True)
ctrl.hemt.output_hemt_voltage_config()

time.sleep(3)


# Start Log.
msg = String()
msg.data = str(time.time())
flag_name = 'sisv_sweep_trigger'
pub = rospy.Publisher(flag_name, String, queue_size=1)
time.sleep(1.5) # 1.5 sec.
#pub.publish('')
time.sleep(3.0)
pub.publish(msg)
time.sleep(1.5)

# initialize
for _ in beam_list:
    ctrl.sis.output_sis_voltage(beam=_, voltage=initial_voltage)

try:
    for vol in range(roop+1):
        for _ in beam_list:
            ctrl.sis.output_sis_voltage(beam=_, voltage=vol*step+initial_voltage)
            time.sleep(interval)
        time.sleep(fixtime)
except KeyboardInterrupt:
    for _ in beam_list:
        ctrl.sis.output_sis_voltage(beam=_, voltage=0)
    msg = String
    msg.data = ''
    pub.publish(msg)
    rospy.signal_shutdown('')

for _ in beam_list:
    ctrl.sis.output_sis_voltage(beam=_, voltage=0)
    time.sleep(interval)

# Finish Log.
msg = String()
msg.data = ''
pub.publish(msg)

# Stop Chopper


# Unset LO.
#ctrl.unset_1st_lo()
