#!/usr/bin/env python3

name = 'nasco_controller'

# ---
import time
import numpy
import threading
import configparser

import rospy
import std_msgs.msg


class controller(object):

    def __init__(self):
        rospy.init_node(name)
        self.ps = PS()

        # ----
        self.slider0 = SLIDER(rsw_id="0")
        self.slider1 = SLIDER(rsw_id="1")
        self.sis = SIS()
        self.hemt = HEMT()
        self.loatt = LOATT()
        self.switch = SWITCH()
        self.sg_8257d = SG(model='e8257d')
        self.sg_mg3692c = SG(model='mg3692c')
        self.sg_fsw0020 = SG(model='fsw0020')
        self.patt = PATT()
        pass

    def display_publisher(self):
        print(self.ps.pub.keys())
        return

    def delete_publisher(self):
        self.ps.pub.clear()
        return


class PS(object):
    pub = {
            #"topic_name":rospy.Publisher(name, data_class, queue_size, latch)
            }

    """
    sub = {
            #"topic_name":[rospy.Subscriber(name, data_class, callback, callback_args), 0]
            }
    """

    def __init__(self):
        """
        sub_th = threading.Thread(
                target = self.sub_function,
                daemon = True
                )
        sub_th.start()
        """
        pass

    def publish(self, topic_name, msg):
        self.pub[topic_name].publish(msg)
        return

    """
    def subscribe(self, topic_name):
        return self.sub[topic_name][1]

    def callback(self, req, topic_name):
        self.sub[topic_name][1] = req.data
        return
    """

    def set_publisher(self, topic_name, data_class, queue_size):
        self.pub[topic_name] = rospy.Publisher(
                                            name = topic_name,
                                            data_class = data_class,
                                            queue_size = queue_size,
                                            latch = True,
                                        )
        time.sleep(0.01)
        return

    """
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
    """


class SIS(object):

    beam_list = ['2l', '2r', '3l', '3r',
                 '4l', '4r', '5l', '5r',
                 '1lu', '1ll', '1ru', '1rl']

    config_file = configparser.ConfigParser()
    config_file.read('/home/amigos/ros/src/nasco_system/configuration/tuning.conf')

    def __init__(self):
        self.ps = PS()
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
    config_file0 = configparser.ConfigParser()
    config_file0.read('/home/amigos/ros/src/nasco_system/configuration/hemt0.conf')
    config_file1 = configparser.ConfigParser()
    config_file1.read('/home/amigos/ros/src/nasco_system/configuration/hemt1.conf')

    def __init__(self):
        self.ps = PS()
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

    def output_hemt_voltage_config(self, *args, config=None):# changed
        for beam in self.beam_list:
            for target in args:
                name = "/hemt_{0}_{1}_cmd".format(beam, target)

                if name not in self.ps.pub:
                    self.ps.set_publisher(
                            topic_name = name,
                            data_class = std_msgs.msg.Float64,
                            queue_size = 1
                        )

                if config == None:
                    voltage = float(self.config_file.get(beam, target))
                elif config == 0:
                    voltage = float(self.config_file0.get(beam, target))
                elif config == 1:
                    voltage = float(self.config_file1.get(beam, target))

                self.ps.publish(topic_name=name, msg=voltage)
                time.sleep(0.005)

        return


class LOATT(object):

    loatt_list = ['2l', '2r', '3l', '3r',
                 '4l', '4r', '5l', '5r',
                 '1l', '1r']

    config_file = configparser.ConfigParser()
    config_file.read('/home/amigos/ros/src/nasco_system/configuration/tuning.conf')

    def __init__(self):
        self.ps = PS()
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

            if beam == "1l" or beam == "1r":
                current = float(self.config_file.get(beam+'u', 'lo_att'))
            else:
                current = float(self.config_file.get(beam, 'lo_att'))

            self.ps.publish(topic_name=name, msg=current)
            time.sleep(0.005)

        return


class SLIDER(object):
    axis = {
              #'ex':[initial position, current position, final position]
                'x':[0, 0, 0],
                'y':[0, 0, 0],
                'z':[0, 0, 0],
                'u':[0, 0, 0],
            }

    def __init__(self, rsw_id):
        self.ps = PS()
        self.rsw_id = rsw_id
        pass

    def initialize(self):
        for key in self.axis:
            self.set_position(axis = key, position = self.axis[key][0])
        return

    def finalize(self):
        for key in self.axis:
            self.set_position(axis=key, position=self.axis[key][2])
        return

    def output_do(self, command):
        if not 0<= command <= 8:
            print("Invalid Command")
            return

        name = "/cpz7415v_rsw{0}_do_cmd".format(self.rsw_id)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Int64,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=command)
        return

    def set_step(self, axis, step):
        if axis not in self.axis:
            print("Invalid Axis")
            return

        name = "/cpz7415v_rsw{0}_{1}_step_cmd".format(self.rsw_id, axis)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.Int64,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=step)
        return


class SWITCH(object):
    ch_list = ["1X", "1Y", "2X", "2Y"]

    def __init__(self):
        self.ps = PS()
        pass

    def switch(self, ch, command):
        """
        command = ON / OFF
        """
        if ch not in self.ch_list:
            print("Invalid Channel")
            print("CH_LIST ['1X','1Y','2X','2Y']")
            return

        name = "/switch_{}_cmd".format(ch)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                    topic_name = name,
                    data_class = std_msgs.msg.String,
                    queue_size = 1
                )

        self.ps.publish(topic_name=name, msg=str(command).upper())
        return

    def switch_all(self, command):
        """
        command = ON / OFF
        """
        for ch in self.ch_list:
            name = "/switch_{}_cmd".format(ch)

            if name not in self.ps.pub:
                self.ps.set_publisher(
                        topic_name = name,
                        data_class = std_msgs.msg.String,
                        queue_size = 1
                    )

            self.ps.publish(topic_name=name, msg=str(command).upper())
        return

class SG(object):
    model_list = ['e8257d', 'mg3692c', 'fsw0020']

    def __init__(self, model):
        self.ps = PS()
        self.model = model
        pass

    def set_freq(self, freq): # GHz

        name = '/{}_freq_cmd'.format(model)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                topic_name = name,
                data_class = std_msgs.msg.Float64,
                queue_size = 1
                )

        if self.model == 'e8257d':
            if not(0.00025 <= freq <= 20.): print('InvalidRangeError')
        if self.model == 'mg3692c':
            if not(2. <= freq <= 20.): print('InvalidRangeError')
        if self.model == 'fsw0020':
            if not(0.5 <= freq <= 20.): print('InvalidRangeError')

        self.ps.publish(name, freq)
        time.sleep(1)
        return

    def set_power(self, power): # dBm

        name = '/{}_power_cmd'.format(model)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                topic_name = name,
                data_class = std_msgs.msg.Float64,
                queue_size = 1
                )

        if self.model == 'e8257d':
            if not(-20. <= power <= 30.): print('InvalidRangeError')
        if self.model == 'mg3692c':
            if not(-20. <= power <= 30.): print('InvalidRangeError')
        if self.model == 'fsw0020':
            if not(-10. <= power <= 13.): print('InvalidRangeError')

        self.ps.publish(name, power)
        time.sleep(1)
        return

    def set_onoff(self, onoff): # on : 1, off : 0

        name = '/{}_onoff_cmd'.format(model)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                topic_name = name,
                data_class = std_msgs.msg.Int32,
                queue_size = 1
                )

        if not(onoff in [0, 1]): print('InvalidOnoffError')

        self.ps.publish(name, onoff)
        time.sleep(1)
        return


class PATT(object):

    beam_list = [
        '2l', '2r', '3l', '3r',
        '4l', '4r', '5l', '5r',
        '1lu', '1ll', '1ru', '1rl'
        ]

    def __init__(self):
        self.ps = PS()
        pass

    def set_att(self, beam, att):

        name = '/patt_{}_cmd'.format(beam)

        if name not in self.ps.pub:
            self.ps.set_publisher(
                topic_name = name,
                data_class = std_msgs.msg.Int32,
                queue_size = 1
                )

        if 0 <= att <= 11:
            self.ps.publish(name, att)
            time.sleep(1)

        else:
            pritn('InvalidRangeError ( 0 <= att < 11 )')
        return

    def set_att_all(self, att_list):

        _ = numpy.array(att_list)
        if 0 in numpy.array((0 <= _) * (_ <=11)).astype(int):
            print('InvalidRangeError ( 0 <= att <= 11 )')

        for beam, att in zip(self.beam_list, att_list):

            name = '/patt_{}_cmd'.format(beam)

            if name not in self.ps.pub:
                self.ps.set_publisher(
                        topic_name = name,
                        data_class = std_msgs.msg.Int32,
                        queue_size = 1
                    )

            self.ps.publish(name, att)
            time.sleep(1.)
        return
