import numpy as np
import matplotlib.pyplot as plt
import glob
import matplotlib.dates as mdates
from pylab import *
from matplotlib import dates, ticker
from scipy import stats
import xarray as xr
import matplotlib.path as mpath
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import scipy.signal as signal
# import cmaps
from mpl_toolkits.basemap import Basemap, shiftgrid
from scipy.stats import t



waveh = xr.open_dataset('G:\SYS\data\CRYOSAT-2\IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_065N-180E-DM00.nc')['SWH_KU_CAL']

waveh[waveh>30] = np.nan
wave_1d = waveh.resample(TIME="1D",skipna=True).interpolate("linear")

#drop nan data
wave_1d_new = wave_1d.dropna(dim='TIME')
wave_1d_new.plot(color='r',linestyle='--',marker='o')
plt.show()
