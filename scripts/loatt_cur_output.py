import sys
sys.path.append("/home/ros/src/nasco_system/configuration/")
import loatt_cur_controller as con
import configparser


loatt_list = ["2l", "2r", "3l", "3r", "4l", "4r", "5l", "5r", "1lu", "1ru"]

config = configparser.ConfigParser()
config.read("tuning.conf")

current = []
current.append(config.get("{}".format(loatt) for loatt in loatt_list, "lo_att"))
for i in range(len(current)):
    con.output_current(loatt_list[i], current[i])
