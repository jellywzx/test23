import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import numpy as np
import pandas as pd
import os


# # fig, ax = plt.subplots()
cryosat2 = xr.open_dataset('G:\SYS\data\CRYOSAT-2\IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_065N-180E-DM00.nc')
# # ers1 = xr.open_dataset('D:/wzx/data/ERS-1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_000N-000E-DM00.nc')
# # jason1 = xr.open_dataset('D:/wzx/data/JASON-1/IMOS_SRS-Surface-Waves_MW_JASON-1_FV02_000N-000E-DM00.nc')
# # saral = xr.open_dataset('D:/wzx/data/SARAL/IMOS_SRS-Surface-Waves_MW_SARAL_FV02_000N-000E-DM00.nc')
lon = cryosat2['LONGITUDE']
lat = cryosat2['LATITUDE']
# Londf=lon.to_dataframe()
# Latdf=lat.to_dataframe()
time = cryosat2['TIME']
swh_KU = cryosat2['SWH_KU_CAL']
swhdf = swh_KU.to_dataframe()
pd.set_option("display.precision",3)

# plot number of waves
a = swhdf['SWH_KU_CAL'].value_counts()
#drop Nan data in dataframe according to the value
a = a[a.values != 967]
plt.bar(a.index,a.values)
plt.ylabel('number of waves')
plt.xlabel('Hs(m)')

# plot pdf
a=a.to_frame()
a['p']=a['SWH_KU'].values/a['SWH_KU'].values.sum()
plt.bar(a.index,a['p'])
plt.ylabel('probability')
plt.xlabel('Hs(m)')
plt.show()


# 无法改变数据的精确位数
# ========================
swhdf['SWH_KU'] = round(swhdf['SWH_KU'],3)
a = swhdf['SWH_KU'].value_counts()
plt.hist(a.index,a.values)
a_df=a.to_frame()
for i in swhdf.count():
    if swhdf['SWH_KU'].iloc[i-1]>32:
        #无法删除Nan值那一行 swhdf.drop(swhdf.iloc[i-1]

c = np.round(swhdf['SWH_KU'], 2)
for i in c:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

# ============================

# swh_KU.plot(color='k')
# uwnd = cryosat2['UWND']
# uwnd.plot(color= 'b')

# jasonswhC = jason1['SWH_C']
# jasonswhC.plot(color ='k')
#
# twin1=ax.twinx()
# jasonswhKU = jason1['SWH_KU']
# jasonswhKU.plot(color ='b')

#
# #对nc格式数据进行重采样
# cryosat2 = xr.open_dataset('D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')
# swh_KU = cryosat2['SWH_KU']
# swh_KUdataframe=swh_KU.to_dataframe()
# result = swh_KUdataframe.groupby([(swh_KUdataframe.index.year),(swh_KUdataframe.index.month)]).mean()
#
# swh_KU.groupby('TIME.dayofyear').mean('TIME')
# swh_KU.resample(TIME='1MS').mean()
# swh_KU.resample(TIME='SM').mean()
# swh_KU.groupby('TIME.dayofyear')
# swh_KU.groupby('TIME.year')
#
# month_length = swh_KU.TIME.dt.days_in_month
# a = swh_KU.sel(TIME='2010-8').to_series()

# 读取多个nc文件
filePath = 'D:/wzx/data/test'

#用os方法来遍历文件夹中所有的文件
# for dirpath, dirnames, filenames in os.walk(filePath):
#     data = xr.open_dataset(filenames)
#     print(data)

files = os.listdir(filePath)
for file in files:
    f = xr.open_dataset(filePath+"\\"+file)
    swh_KU = f['SWH_KU']
    lon = f['LONGITUDE']
    lat = f['LATITUDE']
    time = f['TIME']
    swh_KUdataframe = swh_KU.to_dataframe()
    # resample前需要先剔除NaN值，剩下的值进行月平均
    swh_KUdataframe = swh_KUdataframe[swh_KUdataframe['SWH_KU']<30]
    swh_resampled = swh_KUdataframe.groupby([(swh_KUdataframe.index.year), (swh_KUdataframe.index.month)]).mean()
    ds=xr.Dataset(
        data_vars={'swh_KU': (['TIME'], swh_resampled['SWH_KU'])},
        coords=dict(lon=(["TIME"], swh_resampled['LONGITUDE']),
                    lat=(['TIME'], swh_resampled['LATITUDE']),
                    TIME=pd.to_datetime(swh_resampled.index.get_level_values(0).astype(str)+'-'+swh_resampled.index.get_level_values(1).astype(str), format='%Y-%m'))
    )
    ds.to_netcdf(path='D:/wzx/data/testout'+"/"+file+"out.nc", mode="w")

    # d = xr.DataArray(
    #     data=swh_resampled['SWH_KU'],
    #     dims=['TIME'],
    #     coords=dict(
    #         lon=("LONGITUDE", swh_resampled['LONGITUDE']),
    #         lat=("LATITUDE", swh_resampled['LATITUDE']),
    #         time=time
    #     )
    # )

# cryosat2_resampled = xr.open_dataset('D:/wzx/data/testout/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_082N-000E-DM00.ncout.nc')
# crydf = cryosat2_resampled.to_dataframe()
# crydf.swh_KU = round(crydf.swh_KU, 2)
# a = crydf.swh_KU.value_counts()
def pdf(x):

    return


