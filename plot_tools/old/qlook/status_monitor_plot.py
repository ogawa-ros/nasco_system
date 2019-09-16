import os
import glob
import matplotlib
import matplotlib.pyplot as plt
from n2lite import n2lite
import pandas
import time
from datetime import datetime

matplotlib.rcParams['font.size'] = 20

def plot():

    data_path = '/home/amigos/data/experiments/status_monitor/'
    all_file = grob.grob(data_path + '*')
    path = max(all_file, key=os.path.getctime)
    file_name = path.split('/')[-1]

    status_list = pandas.read_csv(path, sep=' ', header=None,names=['time','CH1','CH2','CH3','CH4','CH5','CH6','CH7','CH8','vacuum','temperture','humidity'])

    #日付
    d = datetime.fromtimestamp(status_list['time'][0])
    D = str(d.year)+'/'+str(d.month)+'/'+str(d.day)+'  '+str(d.hour+9)+':'+str(d.minute)+':'+str(d.second)

    Time = (status_list['time']-status_list['time'][0])/3600
    s = status_list.drop(0,axis = 0)
    s = s.drop('time',axis = 1)
    t = Time.drop(0,axis = 0)
    status_list = pandas.concat([t,s],axis =1)

    ex = status_list[status_list['CH4']<70] #温度制限

    fig = plt.figure(figsize=(6*4, 4*4)) 

    matplotlib.rcParams['font.size'] = 20

    status = ['vacuum','temperture']
    unit = ['(Torr)','(K)']
    title = ['vacuum_gauge','room_temperture']
    CH_list = ['CH2','CH3','CH4','CH5','CH6','CH7','CH8']
    ax = [fig.add_subplot(2,2,i) for i in range(1,len(status)+3)]

    #70K 以下制限
    ex = status_list[status_list['CH4']<70]

    for status, _ax , _unit, _title in zip(status, ax , unit, title):
        _ax.plot(status_list['time'], status_list[status],'.', label = status)
        _ax.grid()
        _ax.set_xlabel('time(hour)',size = 15)
        _ax.set_ylabel(status+_unit,size = 15)
        _ax.set_title(_title,size = 20)
        _ax.legend()
        ax3 = fig.add_subplot(2,2,3)
        ax4 = fig.add_subplot(2,2,4)
        [ax3.plot(status_list['time'],status_list[i],label = i) for i in CH_list]
        ax3.grid()
        ax3.set_xlabel('time(hour)',size = 15)
        ax3.set_ylabel('temperture(K)', size = 15)
        ax3.set_title('all_CH',size = 20)
        ax3.legend()
        [ax4.plot(ex['time'],ex[i],label = i) for i in CH_list]
        ax4.grid(loc = 'upper right' )
        ax4.set_xlabel('time(hour)',size = 15)
        ax4.set_ylabel('temperture(K)', size = 15)
        ax4.set_ylim(0,20)
        ax4.set_title('4Kstage',size = 20)
        ax4.legend()
        
        fig.suptitle( 'START:  '+D, size=48)
        plt.show()

if __name__ == '__main__':
    plot_status_monitor()
