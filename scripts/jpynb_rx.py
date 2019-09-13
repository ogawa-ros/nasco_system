#!/usr/bin/env python3


name = 'jpynb_rx'


import os
import time
import shutil
import subprocess

import rospy
import std_msgs.msg


analy_path = '/home/amigos/analysis/rx'
plot_tool_path = '/home/amigos/ros/src/nasco_system/plot_tools'


def callback(req):
    temp_jpynb = req.data.split('/')[0] + '_temp.ipynb' # need yfactor_necstdb_temp.ipynb
    temp_jpynb_path = os.path.join(plot_tool_path, temp_jpynb)

    jpynb_path = os.path.join(analy_path, req.data)
    if not os.path.exists(jpynb_path):
        os.makedirs(jpynb_path)

    path = os.path.join(jpynb_path, temp_jpynb)
    if not os.path.exists(path):
        shutil.copyfile(temp_jpynb_path, path)

    print('[INFO] Copy : {0}\n' \
          '       --> {1}'.format(temp_jpynb, jpynb_path))

    subprocess.run(['jupyter', 'nbconvert', "--output-dir={0}".format(jpynb_path), '--to', 'script', path])
    os.chdir(jpynb_path)
    py = os.path.join(jpynb_path, temp_jpynb.replace('ipynb', 'py'))

    while not(os.path.exists(py)):
        continue
    subprocess.run(['ipython', '{0}'.format(py), 'xxx'])
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
    print('[INFO] Waiting trigger...')
    rospy.spin()
