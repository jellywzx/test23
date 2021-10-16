import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import numpy as np
import pandas as pd
import os


# fig, ax = plt.subplots()
cryosat2 = xr.open_dataset('D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')
# ers1 = xr.open_dataset('D:/wzx/data/ERS-1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_000N-000E-DM00.nc')
# jason1 = xr.open_dataset('D:/wzx/data/JASON-1/IMOS_SRS-Surface-Waves_MW_JASON-1_FV02_000N-000E-DM00.nc')
# saral = xr.open_dataset('D:/wzx/data/SARAL/IMOS_SRS-Surface-Waves_MW_SARAL_FV02_000N-000E-DM00.nc')
lon = cryosat2['LONGITUDE']
lat = cryosat2['LATITUDE']
Londf=lon.to_dataframe()
Latdf=lat.to_dataframe()
time = cryosat2['TIME']
swh_KU = cryosat2['SWH_KU']

# swh_KU.plot(color = 'k')
# uwnd = cryosat2['UWND']
# uwnd.plot(color= 'b')
#
# jasonswhC = jason1['SWH_C']
# jasonswhC.plot(color ='k')
#
# twin1=ax.twinx()
# jasonswhKU = jason1['SWH_KU']
# jasonswhKU.plot(color ='b')


#对nc格式数据进行重采样
cryosat2 = xr.open_dataset('D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')
swh_KU = cryosat2['SWH_KU']
swh_KUdataframe=swh_KU.to_dataframe()
result = swh_KUdataframe.groupby([(swh_KUdataframe.index.year),(swh_KUdataframe.index.month)]).mean()

swh_KU.groupby('TIME.dayofyear').mean('TIME')
swh_KU.resample(TIME='1MS').mean()
swh_KU.resample(TIME='SM').mean()
swh_KU.groupby('TIME.dayofyear')
swh_KU.groupby('TIME.year')

month_length = swh_KU.TIME.dt.days_in_month
a = swh_KU.sel(TIME='2010-8').to_series()

# 读取多个nc文件
filePath = 'D:/wzx/data/test'
files = os.listdir(filePath)
# for file in files:
#     f = xr.open_dataset(filePath+"\\"+file)
#     swh_KU=f['SWH_KU']

# for dirpath, dirnames, filenames in os.walk(filePath):
#     data = xr.open_dataset(filenames)
#     print(data)

for file in files:
    f=xr.open_dataset(filePath+"\\"+file)
    swh_KU = f['SWH_KU']
    lon = f['LONGITUDE']
    lat = f['LATITUDE']
    time = f['TIME']
    swh_KUdataframe = swh_KU.to_dataframe()
    swh_resampled = swh_KUdataframe.groupby([(swh_KUdataframe.index.year), (swh_KUdataframe.index.month)]).mean()
    # swh_resampled=swh_resampled.to_dataarray()
    ds=xr.Dataset(
        data_vars={'swh_KU':(['TIME'], swh_resampled['SWH_KU'])},
        # dict(swh_KU=(['TIME'],swh_resampled)),
        coords=dict(lon=(["TIME"], swh_resampled['LONGITUDE']),
                    lat=(['TIME'], swh_resampled['LATITUDE']),
                    TIME=pd.to_datetime(swh_resampled.index.get_level_values(0).astype(str)+'-'+swh_resampled.index.get_level_values(1).astype(str),format='%Y-%m'))

    )
    # d = xr.DataArray(
    #     data=swh_resampled['SWH_KU'],
    #     dims=['TIME'],
    #     coords=dict(
    #         lon=("LONGITUDE", swh_resampled['LONGITUDE']),
    #         lat=("LATITUDE", swh_resampled['LATITUDE']),
    #         time=time
    #     )
    # )

