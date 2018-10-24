import sys_vol_controller as con
import configparser


sis_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r',
            '1lu', '1ll', '1ru', '1rl']

config = configparser.ConfigParser()
config.read("setting.ini")

voltage = []
voltage.append(config.get("sis_vol_{}".format(sis) for sys in sys_list, "vol"))
for i in range(len(voltage)):
    con.output_voltage(sis_list[i], voltage[i])

