export ROS_IP = 192.168.100.150
export ROS_MASTER_URI=http://192.168.100.183:11311
source /opt/ros/melodic/setup.bash
source /home/amigos/ros/devel/setup.bash
roslaunch nasco_system nasco_fac.launch
