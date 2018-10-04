import time
import hemt_vol_controller as con
import configparser


hemt_list = ["2l", "2r", "3l", "3r", "4l", "4r", "5l", "5r", "1lu", "1ll", "1ru", "1rl"]

config = configparser.ConfigParser()
config.read("../configuration/tuning.conf")

vd = []
vg1 = []
vg2 = []
for hemt in hemt_list:
	vd.append(float(config.get(hemt, "vd")))
	vg1.append(float(config.get(hemt, "vg1")))
	vg2.append(float(config.get(hemt, "vg2")))
for i in range(len(vd)):
    con.output_voltage(hemt_list[i], vd[i], vg1[i], vg2[i])
    time.sleep(1e-2)
