import os
import sys
import time
import numpy

import rospy
sys.path.append('/home/amigos/ros/src/roach/scripts')
import get_roach_spec

class roach_contorller(object):

    def __init__(self):
        self.roach_id = rospy.get_param('~roach_id')
        self.if_number = rospy.get_param('~if_number')
        





roach_id = 'ROACH_03'
if_num = 1

con = get_roach_spec.spectrometer(roach_id, if_num)

while True:
    try:
         d = con.get_spec()
        time = d['timestamp']
        spec = d['spec']

    except:
        print('finish...')
