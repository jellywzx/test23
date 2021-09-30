import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
fig, ax = plt.subplots()
# cryosat2 = xr.open_dataset('D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')
# ers1 = xr.open_dataset('D:/wzx/data/ERS-1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_000N-000E-DM00.nc')
jason1 = xr.open_dataset('D:/wzx/data/JASON-1/IMOS_SRS-Surface-Waves_MW_JASON-1_FV02_000N-000E-DM00.nc')
# saral = xr.open_dataset('D:/wzx/data/SARAL/IMOS_SRS-Surface-Waves_MW_SARAL_FV02_000N-000E-DM00.nc')
# lon = cryosat2['LONGITUDE']
# lat = cryosat2['LATITUDE']
# time = cryosat2['TIME']


# swh_KU = cryosat2['SWH_KU']
# swh_KU.plot(color = 'k')
# uwnd = cryosat2['UWND']
# uwnd.plot(color= 'b')

jasonswhC = jason1['SWH_C']
jasonswhC.plot(color ='k')

twin1=ax.twinx()
jasonswhKU = jason1['SWH_KU']
jasonswhKU.plot(color ='b')