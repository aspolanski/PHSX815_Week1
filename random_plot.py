#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u

#Other Modules:

from datetime import datetime, timezone

##### Author: Alex Polanski #####
#####  #####


date = str(datetime.now().astimezone())[0:19]

random_data = pd.read_csv('./random_vals.csv')

fig, ax = plt.subplots(figsize=(11,8.5))

ax.hist(random_data['vals'],histtype='step',hatch='/',edgecolor='black') #Plot Histogram 
ax.set_xlabel("Value", fontsize=22)
ax.set_ylabel("Frequency", fontsize=22)
ax.set_title(f"Uniform Distribution for {len(random_data['vals'])} Samples",fontsize=22)


ax.minorticks_on()
ax.tick_params(axis='both',which='both',direction='in',labelsize='large')

plt.tight_layout()

fig_name = 'uniform_plot_' + date + '.pdf'

plt.savefig(fig_name, orientation='landscape', format='pdf')
