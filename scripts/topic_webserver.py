#!/usr/bin/env python3

import rospy, os, ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

def kill():
    os.system('kill -KILL ' + str(os.getpid()))

os.chdir('/home/amigos/ros/src/nasco_system/web_monitor')

rospy.init_node('webserver')
host = rospy.get_param('~host')
port = rospy.get_param('~port')

httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
print('serving at port', port)
httpd.serve_forever()

rospy.on_shutdown(kill)
