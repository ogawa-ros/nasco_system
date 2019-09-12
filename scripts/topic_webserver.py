#!/usr/bin/env python3

import rospy, os, ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

def kill():
    os.system('kill -KILL ' + str(os.getpid()))

os.chdir('/home/amigos/ros/src/nasco_system/web_monitor')
 host = '172.20.0.237'
host = rospy.get_params('~host')
port = rospy.get_params('~port')
httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
print('serving at port', port)
httpd.serve_forever()

rospy.init_node('webserver')
rospy.on_shutdown(kill)
