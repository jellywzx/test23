import netCDF4
from netCDF4 import Dataset
from pandas import Series
import tkinter as tk
from tkinter import filedialog
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import netCDF4 as nc


# fig, ax = plt.subplots()
cryosat2 = xr.open_dataset('C:/Users/fzjxw/Desktop/test/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')

# era5 = xr.open_dataset('download.nc')
# ers1 = xr.open_dataset('D:/wzx/data/ERS-1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_000N-000E-DM00.nc')
#jason1 = xr.open_dataset('D:/wzx/data/JASON-1/IMOS_SRS-Surface-Waves_MW_JASON-1_FV02_000N-000E-DM00.nc')
# saral = xr.open_dataset('D:/wzx/data/SARAL/IMOS_SRS-Surface-Waves_MW_SARAL_FV02_000N-000E-DM00.nc')
lon = cryosat2['LONGITUDE']
lat = cryosat2['LATITUDE']
time = cryosat2['TIME']
swh_KU = cryosat2['SWH_KU']
# swh_KU.plot()
# plt.title('lat=0N, lon=75E')
# plt.xlabel('TIME', fontsize=10)
# plt.xticks(fontsize=10)
# plt.show()


# uwnd = cryosat2['UWND']
# uwnd.plot(color= 'b')

# jasonswhC = jason1['SWH_C']
# jasonswhC.plot(color ='k')
#
# twin1=ax.twinx()
# jasonswhKU = jason1['SWH_KU']
# jasonswhKU.plot(color ='b')


era5 = xr.open_dataset('G:/SYS/data/adaptor.mars.internal-1633085155.6619427-4694-4-5eb53e1c-d956-4729-b7c4-c6549011d060.nc')
# a =xr.open_mfdataset('G:/SYS/data/test/*.nc')

# ers=nc.MFDataset('G:/SYS/data/test1/*.nc')
# ers1=nc.Dataset('G:/SYS/data/test1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_000N-000E-DM00.nc')
# ers2=nc.Dataset('G:/SYS/data/test1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_000N-001E-DM00.nc')
#
# xrers= xr.open_mfdataset('G:/SYS/data/test/*.nc')
# xrers1=xr.open_dataset('G:/SYS/data/test/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')
# xrers2=xr.open_dataset('G:/SYS/data/test/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-001E-DM00.nc')

times=[]
latitudes=[]
longitudes=[]


times_after=[]
latitudes_after=[]
longitudes_after=[]

netCDF4.num2date(time,)

da = xr.DataArray(
   ...:     np.sin(0.3 * np.arange(12).reshape(4, 3)),
   ...:     [("time", np.arange(4)), ("space", [0.1, 0.2, 0.3])],
   ...: )

