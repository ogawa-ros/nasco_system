export ROS_IP=172.20.0.160
export ROS_MASTER_URI=http://172.20.0.21:11311
source /opt/ros/melodic/setup.bash
source /home/necst/ros/devel/setup.bash
roslaunch nasco_system nasco_fac.launch
