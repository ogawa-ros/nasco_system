export ROS_IP=172.20.0.151
export ROS_MASTER_URI=http://172.20.0.21:11311
source /opt/ros/melodic/setup.bash
source /home/amigos/ros/devel/setup.bash
roslaunch nasco_system nasco.launch
