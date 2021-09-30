import numpy as np
import netCDF4 as nc
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import xarray as xr
import matplotlib.pyplot as plt
from metpy.cbook import get_test_data
from mpl_toolkits.basemap import Basemap

# read cryosat2 data
file_path = 'D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-075E-DM00.nc'
file_obj = nc.Dataset(file_path)
file_obj
file_obj.variables.keys()
botdepth = file_obj.variables['BOT_DEPTH']
depth_arr = botdepth[:]
depth_arr.shape
lon = file_obj.variables['LONGITUDE'][:]
lat = file_obj.variables['LATITUDE'][:]
time = file_obj.variables['TIME']
# swh_C = file_obj.variables['SWH_C'][:]
swh_KU = file_obj.variables['SWH_KU'][:]
swh_KU.plot()

# mp = Basemap(projection='merc',
#              llcrnrlon=23.5,
#              llcrnrlat=56.5,
#              urcrnrlon=107.5,
#              urcrnrlat=80.4,
#              resolution='i')
# # lon, lat = np.meshgrid(lon, lat)
# # x, y = mp(lon, lat)
# mp.drawcoastlines()
# mp.drawstates()
# mp.drawcountries()
# plt.title('cryosat2')
#
# plt.show()
# # c_scheme = mp.pcolor(x, y, np.squeeze)

