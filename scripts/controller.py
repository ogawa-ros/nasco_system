
import time

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64

name = 'controller'
rospy.init_node(name)

beam_list = ['2l', '2r', '3l', '3r',
             '4l', '4r', '5l', '5r',
             '1lu', '1ll', '1ru', '1rl']

config = configparser.ConfigParser()
config.read('../configuration/tuning.conf')


#--- lo
pub_lo_1st_freq = rospy.Publisher('/lo_1st_freq_cmd', Float64, queue_size=1)
pub_lo_1st_power = rospy.Publisher('/lo_1st_power_cmd', Float64, queue_size=1)
pub_lo_1st_onoff = rospy.Publisher('/lo_1st_onoff_cmd', Int32, queue_size=1)


class InvalidRangeError(Exception):
    pass


def set_1st_lo(frequency=0., signal_power=0., config=False):
    step = 1e-1
    interval = 5e-1
    freq, power, onoff = Float64(), Float64(), Int32()
    power.data = 0.
    onoff.data = 1
    pub_lo_1st_power.pub(power)
    time.sleep(interval)

    if config == True:
        freq.data = float(config.get(freq, 'lo_1st'))
        target_power = float(config.get(power, 'lo_1st'))

        pub_lo_1st_freq.pub(freq)
        time.sleep(interval)
        pub_lo_1st_onoff.pub(onoff)
        time.sleep(interval)

        for _ in range(1, int(target_power / step)):
            power.data = float(_ * step)
            pub_lo_1st_power.publish(power)
            time.sleep(interval)

    else:
        if -20. < signal_power < 30.:
            freq.data = frequency
            target_power = signal_power

            pub_lo_1st_freq.pub(freq)
            time.sleep(interval)
            pub_lo_1st_onoff.pub(onoff)
            time.sleep(interval)

            for _ in range(1, int(target_power / step)):
                power.data = float(_ * step)
                pub_lo_1st_power.publish(power)
                time.sleep(interval)
        else:
            msg = 'Output power range is -20 -- 30V,'
            msg += ' while {}dBm is given.'.format(signal_power)
            raise InvalidRangeError(msg)
    return

def unset_1st_lo():
    interval = 5e-1
    freq, power, onoff = Float64(), Float64(), Int32()
    freq.data, power.data, onoff.data = 0., 0., 0

    pub_freq.publish(freq)
    time.sleep(interval)
    pub_power.publish(power)
    time.sleep(interval)
    pub_onoff.publish(onoff)
    return

def output_sis_voltage(sis='', voltage=0., config=False):
    interval = 1e-3
    msg = Float64()
    topic_list = ['/sis_vol_{}_cmd'.format(_) for _ in beam_list]
    pub_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list]
    if config == True:
        vol_list = [float(config.get(sis, 'sisv')) for sis in beam_list]
        for pub, vol in zip(pub_list, vol_list):
            msg.data = vol
            pub.publish(msg)
            time.sleep(interval)

    else:
        msg.data = voltage
        pub = pub_list[beam_list.index(sis)]
        pub.publish(msg)
        time.sleep(interval)
    return

def output_hemt_voltage(beam='', **kargs, config=False):
    interval = 1e-3
    msg = Flaot64()
    topic_vd_list = ['/hemt_{}_vd_cmd'.format(_) for _ in beam_list]
    topic_vg1_list = ['/hemt_{}_vg1_cmd'.format(_) for _ in beam_list]
    topic_vg2_list = ['/hemt_{}_vg2_cmd'.format(_) for _ in beam_list]
    pub_vd_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list_vd]
    pub_vg1_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list_vg1]
    pub_vg2_list = [rospy.Publisher(topic, Float64, queue_size=1) for topic in topic_list_vg2]

    if config == True:
        vd_list = [float(config.get(beam, 'vd')) for beam in beam_list]
        vg1_list = [float(config.get(beam, 'vg1')) for beam in beam_list]
        vg2_list = [float(config.get(beam, 'vg2')) for beam in beam_list]
        for pub_vd, pub_vg1, pub_vg2, vd, vg1, vg2 in zip(pub_vd_list, pub_vg1_list, pub_vg2_list,
                                                          vd_list, vg1_list, vg2_list):
            msg.data = vd
            pub_vd.publish(vd)
            time.sleep(interval)
            msg.data = vg1
            pub_vg1.publish(vg1)
            time.sleep(interval)
            msg.data = vg2
            pub_vg2.publish(vg2)
            time.sleep(interval)
        return

    else:
        idx = beam_list.index(beam)
        if 'vd' in kargs:
            msg.data = kargs['vd']
            pub_vd_list[idx].publish(msg)
        if 'vg1' in kargs:
            msg.data = kargs['vg1']
            pub_vd_list[idx].publish(msg)
        if 'vg2' in kargs:
            msg.data = kargs['vg2']
            pub_vd_list[idx].publish(msg)
    return

def output_loatt_current(beam='', current=0., config=False):
    interval = 5e-3
    msg = Float64()
    loatt_list = beam_list[:-4]
    loatt.list.extend(['1l', '1r'])
    topic_loatt_list = ['/loatt_{}_cmd'.format(_) for _ in topic_loatt_list]
    pub_loatt_list = [rospy.Publisher(topi, Float64, queue_size=1)
                          for topic in topic_loatt_list]

    if config == True:
        loatt_list = [float(config.get(beam, 'loatt')) for beam in beam_list[:-2]]
        for pub, current zip(pub_loatt_list, loatt_list):
            msg.data = current
            pub.publish(msg)
            time.sleep(interval)

    else:
        idx = loatt_list.index(beam)
        msg.data = current
        pub_loatt_list[idx].publish(msg)
