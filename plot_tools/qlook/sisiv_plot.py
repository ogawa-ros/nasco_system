import os
import glob
import numpy
import matplotlib
import matplotlib.pyplot
from n2lite import n2lite

matplotlib.rcParams['figure.facecolor'] = 'white'
matplotlib.rcParams['savefig.dpi'] = 200

sis_list = ['2l', '2r', '3l', '3r',
            '4l', '4r', '5l', '5r', 
            '1lu', '1ll', '1ru', '1rl']

def plot():
    data_path = '/home/amigos/data/sql/sisiv/'
    all_file = glob.glob(data_path + '*' )
    path = max(all_file, key=os.path.getctime)
    file_name = path.split('/')[-1]

    d = n2lite.N2lite(path +'/param.db')
    D = d.read_pandas_all()
    
    ncol = 4
    nrow = 3
    nax = ncol * nrow

    figsize = (ncol * 2, nrow * 2)
    
    fig = matplotlib.pyplot.figure(figsize=figsize)
    ax = [fig.add_subplot(nrow, ncol, i+1) for i in range(nax)]
    
    for _ax, sis in zip(ax, sis_list):
        _ax.plot(D['sis_vol_'+sis], D['sis_cur_'+sis], '.')
        _ax.grid()
        _ax.set_xlabel('voltage [mV]')
        _ax.set_ylabel('current [uA]')
        _ax.set_title('{}'.format(sis))
        
    fig.subplots_adjust(wspace=0.6, hspace=0.6)
    fig.suptitle(path + '\nNASCO IV MEASUREMENT')
    
    # matplotlib.pyplot.savefig('{0}/{1}.png'.format(path, file_name))
        
    matplotlib.pyplot.show()

if __name__ == '__main__':
    plot_sisiv()
