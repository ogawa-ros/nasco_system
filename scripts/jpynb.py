#!/usr/bin/env python3


name = 'jpynb'


import os
import shutil
import time

import rospy
import std_msgs.msg


analy_path = '/home/amigos/analysis/rx'
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tool'


def callback(req):
    temp_jpynb = req.data.split('/')[0] + '_temp.ipynb' # yfactor 用の yfactor_necstdb_temp.ipynb が必要
    temp_jpynb_path = os.path.join(plot_tool_path, temp_jpynb)

    jpynb_path = os.path.join(analy_path, q.data)
    if not os.path.exists(jpynb_path):
        os.makedirs(jpynb_path)

    path = os.path.join(jpynb_path, temp_ipynb)
    if not os.path.exists(path):
        shutil.copyfile(temp_jpynb_path, jpynb_path)
    return


if __name__ == '__main__':
    if not os.path.exists(analy_path):
        os.makedirs(analy_path)
        pass

    rospy.init_node(name)
    rospy.Subscriber(
        name = 'jpynb_path',
        data_class = std_msgs.msg.String,
        callback = callback
        )
    rospy.spin()
