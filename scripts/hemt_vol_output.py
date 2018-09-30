import sys
sys.path.append("/home/ros/src/nasco_system/configuration/")
import hemt_vol_controller as con
import configparser


hemt_list = ["2l", "2r", "3l", "3r", "4l", "4r", "5l", "5r", "1lu", "1ll", "1ru", "1rl"]

config = configparser.ConfigParser()
config.read("tuning.conf")

vd = []
vg1 = []
vg2 = []
vd.append(config.get("{}".format(hemt) for hemt in hemt_list, "vd"))
vg1.append(config.get("{}".format(hemt) for hemt in hemt_list, "vg1"))
vg2.append(config.get("{}".format(hemt) for hemt in hemt_list, "vg2"))
for i in range(len(vd)):
    con.output_voltage(hemt_list[i], vd[i], vg1[i], vg2[i])
