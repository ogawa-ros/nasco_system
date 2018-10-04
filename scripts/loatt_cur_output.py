import time
import loatt_cur_controller as con
import configparser


loatt_list = ["2l", "2r", "3l", "3r", "4l", "4r", "5l", "5r", "1lu", "1ru"]

config = configparser.ConfigParser()
config.read("../configuration/tuning.conf")

def main():
        current = []
        for loatt in loatt_list:
	        current.append(float(config.get("{}".format(loatt), "lo_att")))
        for i in range(len(current)):
                con.output_current(loatt_list[i], current[i])

if __name__ == '__main__':
        main()
