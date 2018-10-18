export ROS_IP=192.168.100.183
export ROS_MASTER_URI=http://localhost:11311
source /opt/ros/melodic/setup.bash
source /home/amigos/ros/devel/setup.bash
roslaunch nasco_system nasco.launch
