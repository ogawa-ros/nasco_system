import sis_vol_controller as con
import configparser


sis_list = ["2l", "2r", "3l", "3r", "4l", "4r", "5l", "5r", "1lu", "1ll", "1ru", "1rl"]o1

config = configparser.ConfigParser()
config.read("../configuration/tuning.conf")


voltage = []
for sis in sis_list:
	voltage.append(float(config.get(sis, "sisv")))

for i in range(len(voltage)):
	con.output_voltage(sis_list[i], voltage[i])
