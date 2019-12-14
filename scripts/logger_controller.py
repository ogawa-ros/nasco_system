#!/usr/bin/env python3

node_name = 'logger_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.logger = logger()


class make_pub(object):

    def __init__(self):
        self.pub = {}
        pass

    def publish(self, topic_name, data_class, msg):
        if topic_name not in self.pub:
            self.set_publisher(topic_name = topic_name, data_class = data_class)
            pass

        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class):
        self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = True)
        time.sleep(0.1)
        return


class logger(object):

    def __init__(self):
        self.make_pub = make_pub()

    def start(self, db_path):
        topic_name = '/logger_path'
        data_class = std_msgs.msg.String
        self.make_pub.publish(topic_name, data_class, msg = db_path)
        msg = '[INFO] : Data Saved to\n' \
              '         amigos@172.20.0.11 ( 記録 PC ) :\n' \
              '         /media/usbdisk/data/rx/{}'.format(db_path)
   #     print(msg)
        return msg

    def stop(self):
        topic_name = '/logger_path'
        data_class = std_msgs.msg.String

        self.make_pub.publish(topic_name, data_class, msg = '')
        return
