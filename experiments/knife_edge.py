import sys
import time
sys.path.append('/home/amigos/ros/src/nasco_system/scripts')
import nasco_controller
con = nasco_controller.SLIDER()
import logger_controller
import jpynb_controller

name = 'knife_edge'
start = 0
step = 0
axis = 'x' #or 'y'
num = 0
time = 0

rospy.init_node(name)

logger = logger_controller.logger()
jpynb = jpynb_controller.jpynb()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
dir_name = name + date + '.necstdb'

con.slider1.set_step(axis,start * 100)

print('[INFO] : Start to knife edge')

logger.start(dir_name)

for i in range(num):
    con.slider1.set_step(axis, (start + step * (i + 1)) * 100)
    time.sleep(time)
    
logger.stop()

print('[INFO] : End to knife edge')

jpynb.make(dir_name)

con.slider1.set_step(axis,start * 100)
