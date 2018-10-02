# export ROS_IP = 172.20.0.24
# export ROS_MASTER_URI=http://172.20.0.20:11311
source /opt/ros/melodic/setup.bash
source /home/necst/ros/devel/setup.bash
roslaunch nasco_system nasco.launch
