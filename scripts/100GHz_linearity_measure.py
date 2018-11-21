#this program is to measure linearity using roach board fo  100GHz 

#import module
import os, sys, time, datetime, numpy
#import rospy
import matplotlib.pyplot as plt
import NASCORX_System.device.A11713B as a11713b
import sys,os,time
sys.path.append('/home/amigos/ros/src/roach/scripts/')
import get_roach_spec as roach

'''
#prepare rospy 
rospy.init_node('nini')
'''

#input GPIB number for Beam 2
GPIB_No = input('type Beam2 GPIB IP adress!!!')


#set ATT driver
_att_beam2 = a11713b.a11713b(IP=GPIB_No,connection='GPIB')
_att_beam3 = a11713b.a11713b(IP='192.168.100.153',connection='LAN')
_att_beam4 = a11713b.a11713b(IP='192.168.100.154',connection='LAN')
_att_beam5 = a11713b.a11713b(IP='192.168.100.155',connection='LAN')

'''
#prepare roach board
spec_beam_2L = roach.spectrometer(2,1)
spec_beam_2R = roach.spectrometer(2,2)
spec_beam_3L = roach.spectrometer(3,1)
spec_beam_3R = roach.spectrometer(3,2)
spec_beam_4L = roach.spectrometer(4,1)
spec_beam_4R = roach.spectrometer(4,2)
spec_beam_5L = roach.spectrometer(5,1)
spec_beam_5R = roach.spectrometer(5,2)
'''

#prepare save array
beam_2L=[]
beam_2R=[]
beam_3L=[]
beam_3R=[]
beam_4L=[]
beam_4R=[]
beam_5L=[]
beam_5R=[]


#initialize BEAM2
_att_beam2.set_level(0,'1X')
_att_beam2.set_level(0,'1Y')
time.sleep(10)


#start measure
for rep in range(12): #rep = repeat number
    #set ATT 
    _att_beam2.set_level(rep,'1X')
    _att_beam2.set_level(rep,'1Y')
    _att_beam3.set_level(rep,'1X')
    _att_beam3.set_level(rep,'1Y')
    _att_beam4.set_level(rep,'1X')
    _att_beam4.set_level(rep,'1Y')
    _att_beam5.set_level(rep,'1X')
    _att_beam5.set_level(rep,'1Y')
    
    time.sleep(5)
    



