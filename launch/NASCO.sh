#export ROS_IP=192.168.101.170
#export ROS_MASTER_URI=http://192.168.101.170:11311
export ROS_IP=172.20.0.233
export ROS_MASTER_URI=http://172.20.0.233:11311

source /opt/ros/melodic/setup.bash
source /home/amigos/ros/devel/setup.bash
roslaunch nasco_system nasco.launch
