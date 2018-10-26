#!/usr/bin/env python3

name = 'nasco_controller'

# ----
import time
import threading
import configparser

import rospy
import std_msgs.msg


class controller(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = PS()

        # ----
        self.slider = SLIDER(self.ps, rsw_id="0")
        self.sis = SIS(self.ps)
        self.hemt = HEMT(self.ps)
        self.loatt = LOATT(self.ps)
        pass

    def display_publisher(self):
        print(self.ps.pub.keys())
        return

    def display_subscriber(self):
        print(self.ps.sub.keys())
        return

    def delete_publisher(self):
        self.ps.pub.clear()
        return

    def delete_subscriber(self):
        self.ps.sub.clear()
        return


class PS(object):
    pub = {
            #"topic_name":rospy.Publisher(name, data_class, queue_size)
            }
    
    sub = {
            #"topic_name":[rospy.Subscriber(name, data_class, callback, callback_args), 0]
            }

    def __init__(self):
        sub_th = threading.Thread(
                target = self.sub_function,
                daemon = True
                )
        sub_th.start()
        pass

    def publish(self, topic_name, msg):
        self.pub[topic_name].publish(msg)
        return

    def subscribe(self, topic_name):
        return self.sub[topic_name][1]

    def callback(self, req, topic_name):
        self.sub[topic_name][1] = req.data
        return

    def set_publisher(self, topic_name, data_class, queue_size):
        self.pub[topic_name] = rospy.Publisher(
                                            name = topic_name,
                                            data_class = data_class,
                                            queue_size = queue_size
                                        )
        return

    def set_subscriber(self, topic_name, data_class):
        self.sub[topic_name] = [rospy.Subscriber(
                                            name = topic_name,
                                            data_class = data_class,
                                            callback = self.callback,
                                            callback_args = topic_name
                                        ), None]
        return

    def sub_function(self):
        rospy.spin()
        return


class SIS(object):
    
    beam_list = ['2l', '2r', '3l', '3r',
                 '4l', '4r', '5l', '5r',
                 '1lu', '1ll', '1ru', '1rl']

    config_file = configparser.ConfigParser()
    config_file.read('/home/amigos/ros/src/nasco_system/configuration/tuning.conf')

    def __init__(self, ps):
        self.ps = ps
        pass

    def output_sis_voltage(self, beam, voltage):
        if beam not in self.beam_list:
            print("Invalid Beam Name")
            return

        name = "/sis_vol_{}_cmd".format(beam)
        
        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Float64,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=voltage)
        return

    def output_sis_voltage_config(self): # changed
        for beam in self.beam_list:
            name = "/sis_vol_{}_cmd".format(beam)

            if name not in self.ps.pub:
                self.ps.set_publisher(
                        topic_name = name,
                        data_class = std_msgs.msg.Float64,
                        queue_size = 1
                    )
            
            voltage = float(self.config_file.get(beam, 'sisv'))
            self.ps.publish(topic_name=name, msg=voltage)
            time.sleep(0.001)
        
        return


class HEMT(object):
    
    beam_list = ['2l', '2r', '3l', '3r',
                 '4l', '4r', '5l', '5r',
                 '1lu', '1ll', '1ru', '1rl']

    config_file = configparser.ConfigParser()
    config_file.read('/home/amigos/ros/src/nasco_system/configuration/tuning.conf')

    def __init__(self, ps):
        self.ps = ps
        pass

    def output_hemt_voltage(self, beam, **kargs):
        if beam not in self.beam_list:
            print("Invalid Beam Name")
            return

        for key in kargs:
            name = "/hemt_{0}_{1}_cmd".format(beam, key)
        
            if name not in self.ps.pub:
                self.ps.set_publisher(
                        topic_name = name,
                        data_class = std_msgs.msg.Float64,
                        queue_size = 1
                    )

            self.ps.publish(topic_name=name, msg=kargs[key])

        return

    def output_hemt_voltage_config(self, *args):# changed
        for beam in self.beam_list:
            for target in args:
                name = "/hemt_{0}_{1}_cmd".format(beam, target)

                if name not in self.ps.pub:
                    self.ps.set_publisher(
                            topic_name = name,
                            data_class = std_msgs.msg.Float64,
                            queue_size = 1
                        )
            
                voltage = float(self.config_file.get(beam, str(target)))
                self.ps.publish(topic_name=name, msg=voltage)
                time.sleep(0.001)
        
        return


class LOATT(object):
    
    loatt_list = ['2l', '2r', '3l', '3r',
                 '4l', '4r', '5l', '5r',
                 '1l', '1r']

    config_file = configparser.ConfigParser()
    config_file.read('/home/amigos/ros/src/nasco_system/configuration/tuning.conf')

    def __init__(self, ps):
        self.ps = ps
        pass

    def output_loatt_current(self, beam, current):
        if beam not in self.loatt_list:
            print("Invalid Beam Name")
            return

        name = "/loatt_{}_cmd".format(beam)
        
        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Float64,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=current)
        return

    def output_loatt_current_config(self): # changed
        for beam in self.loatt_list:
            name = "/loatt_{}_cmd".format(beam)

            if name not in self.ps.pub:
                self.ps.set_publisher(
                        topic_name = name,
                        data_class = std_msgs.msg.Float64,
                        queue_size = 1
                    )
            
            current = float(self.config_file.get(beam, 'lo_att'))
            self.ps.publish(topic_name=name, msg=current)
            time.sleep(0.005)
        
        return


class SLIDER(object):
    axis = {
              #'ex':[initial position, current position, final position, do_number]
                'x':[0, 0, 0, 1],
                'y':[0, 0, 0, 2],
                'z':[0, 0, 0, 3],
            }

    def __init__(self, ps, rsw_id):
        self.ps = ps
        self.rsw_id = rsw_id
        pass

    def initialize(self):
        for key in self.axis:
            self.set_position(axis = key, position = self.axis[key][0])
            time.sleep(5) # need?
        return

    def finalize(self):
        for key in self.axis:
            self.set_position(axis=key, position=self.axis[key][2])
            time.sleep(5) # need?
        return
    
    def set_origin_position(self, axis):
        if axis not in self.axis:
            print("Invalid Axis")
            return

        name = "/cpz7415v_rsw{0}_do{1}_cmd".format(self.rsw_id, self.axis[axis][3])
        
        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Bool,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=False)
        time.sleep(1)
        self.ps.publish(topic_name=name, msg=True)
        return

    def set_position(self, axis, position):
        if axis not in self.axis:
            print("Invalid Axis")
            return

        name = "/cpz7415v_rsw{0}_{1}_position_cmd".format(self.rsw_id, axis)
        
        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Int64,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=position*100)
        return

    def get_position(self, axis):
        if axis not in self.axis:
            print("Invalid Axis")
            return

        name = "/cpz7415v_rsw{0}_{1}_position".format(self.rsw_id, axis)

        if name not in self.ps.sub:
            self.ps.set_subscriber(
                    topic_name = name,
                    data_class = std_msgs.msg.Int64
                )
        
        ret = self.ps.subscribe(topic_name=name)
        return ret

    def error_reset(self):
        # False before True
        name = "/cpz7415v_rsw{0}_do4_cmd".format(self.rsw_id)
        
        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Bool,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=False)
        time.sleep(1)
        self.ps.publish(topic_name=name, msg=True)
        return
        
