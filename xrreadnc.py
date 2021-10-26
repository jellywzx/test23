import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import numpy as np
import pandas as pd
import os

cryosat2 = xr.open_dataset('D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_065N-180E-DM00.nc')
swh_KU = cryosat2['SWH_KU_CAL']
    # .sel(TIME=slice('2016','2018'))
swh_KU[swh_KU>30] = np.nan
swhKU = swh_KU.dropna(dim='TIME')
plt.figure()
swh_KU.plot(color='r', linestyle='--', marker='o', label='CRYOSAT2')

hy2 = xr.open_dataset('D:/wzx/data/HY-2/IMOS_SRS-Surface-Waves_MW_HY-2_FV02_065N-180E-DM00.nc')
swh_KU_hy2 = hy2['SWH_KU_CAL'].sel(TIME=slice('2016','2018'))
swh_KU_hy2[swh_KU_hy2>30] = np.nan
swh_KU_hy2 = swh_KU_hy2.dropna(dim='TIME')
swh_KU_hy2.plot(color='b',linestyle='--',marker='*',label='HY2')

s3 = xr.open_dataset('D:/wzx/data/SENTINEL-3A/IMOS_SRS-Surface-Waves_MW_SENTINEL-3A_FV02_065N-180E-DM00.nc')
swh_KU_s3 = s3['SWH_KU_CAL'].sel(TIME=slice('2016','2018'))
swh_KU_s3.plot(color='g',linestyle='--',marker='x',label='SENTINEL-3A')
plt.legend()
plt.title('65N 180E Calibrated significant wave height')

# 0N 0E
cryosat2 = xr.open_dataset('D:/wzx/data/CRYOSAT-2/IMOS_SRS-Surface-Waves_MW_CRYOSAT-2_FV02_000N-000E-DM00.nc')
swh_KU = cryosat2['SWH_KU_CAL'].sel(TIME=slice('2016','2018'))
swh_KU[swh_KU>30] = np.nan
swhKU = swh_KU.dropna(dim='TIME')
plt.figure()
swh_KU.plot(color='r', linestyle='--', marker='o', label='CRYOSAT2')

hy2 = xr.open_dataset('D:/wzx/data/HY-2/IMOS_SRS-Surface-Waves_MW_HY-2_FV02_000N-000E-DM00.nc')
swh_KU_hy2 = hy2['SWH_KU_CAL'].sel(TIME=slice('2016','2018'))
swh_KU_hy2[swh_KU_hy2>30] = np.nan
swh_KU_hy2 = swh_KU_hy2.dropna(dim='TIME')
swh_KU_hy2.plot(color='b',linestyle='--',marker='*',label='HY2')

s3 = xr.open_dataset('D:/wzx/data/SENTINEL-3A/IMOS_SRS-Surface-Waves_MW_SENTINEL-3A_FV02_000N-000E-DM00.nc')
swh_KU_s3 = s3['SWH_KU_CAL'].sel(TIME=slice('2016','2018'))
swh_KU_s3.plot(color='g',linestyle='--',marker='x',label='SENTINEL-3A')
plt.legend()
plt.title('0N 0E Calibrated significant wave height')








# plot number of waves
swhKUdf = swhKU.to_dataframe()
a = swhKUdf['SWH_KU_CAL'].value_counts()
plt.bar(a.index,a.values)
plt.ylabel('number of waves')
plt.xlabel('Hs(m)')
plt.title('65N 180E CRYOSAT-2 swh_KU')


# ers1 = xr.open_dataset('D:/wzx/data/ERS-1/IMOS_SRS-Surface-Waves_MW_ERS-1_FV02_065N-180E-DM00.nc')
# swh_KU_ers1 = ers1['SWH_KU_CAL']
# # if contain Nan data
# swh_KU_ers1[swh_KU_ers1>30] = np.nan
# swh_KU_ers1 = swh_KU_ers1.dropna(dim='TIME')
# # if data is OK
# swh_KU_ers1.plot(color='b',linestyle='--',marker='o')
# # plt.title('ERS-1 swh_KU')

# ers2 = xr.open_dataset('D:/wzx/data/ERS-2/IMOS_SRS-Surface-Waves_MW_ERS-2_FV02_065N-180E-DM00.nc')
# swh_KU = ers2['SWH_KU_CAL']
# swh_KU.plot(color='r',linestyle='--',marker='o')
# plt.title('ERS-2 swh_KU')

hy2 = xr.open_dataset('D:/wzx/data/HY-2/IMOS_SRS-Surface-Waves_MW_HY-2_FV02_065N-180E-DM00.nc')
swh_KU_hy2 = hy2['SWH_KU_CAL']
swh_KU_hy2[swh_KU_hy2>30] = np.nan
swh_KU_hy2 = swh_KU_hy2.dropna(dim='TIME')
swh_KU_hy2.plot(color='b',linestyle='--',marker='*',label='HY2')
# plt.title('HY-2 swh_KU')

# # 需要drop极低值
# jason1 = xr.open_dataset('D:/wzx/data/JASON-1/IMOS_SRS-Surface-Waves_MW_JASON-1_FV02_065N-180E-DM00.nc')
# swh_KU = jason1['SWH_KU_CAL']
# # swh_KU[swh_KU>30] = np.nan
# # swhKU = swh_KU.dropna(dim='TIME')
# swh_KU.plot(color='r',linestyle='--',marker='o')
# plt.title('JASON-1 swh_KU')

# # 没有180E的数据，只有181E的数据
# # 需要drop极低值
# jason2 = xr.open_dataset('D:/wzx/data/JASON-2/IMOS_SRS-Surface-Waves_MW_JASON-2_FV02_065N-181E-DM00.nc')
# swh_KU = jason1['SWH_KU_CAL']
# # swh_KU[swh_KU>30] = np.nan
# # swhKU = swh_KU.dropna(dim='TIME')
# swh_KU.plot(color='r',linestyle='--',marker='o')
# plt.title('JASON-2 swh_KU')

#这个经纬度是65N,181E
# jason3 = xr.open_dataset('D:/wzx/data/JASON-3/IMOS_SRS-Surface-Waves_MW_JASON-3_FV02_065N-181E-DM00.nc')
# swh_KU_jason3 = jason3['SWH_KU_CAL']
# # swh_KU[swh_KU>30] = np.nan
# # swhKU = swh_KU.dropna(dim='TIME')
# swh_KU_jason3.plot(color='g',linestyle='--',marker='o')
# # plt.title('JASON-3 swh_KU')

# # 这个SARAL数据没有Ku波段的有效波高
# saral = xr.open_dataset('D:/wzx/data/SARAL/IMOS_SRS-Surface-Waves_MW_SARAL_FV02_065N-180E-DM00.nc')
# swh_KU = saral['SWH_KU_CAL']
# # swh_KU[swh_KU>30] = np.nan
# # swhKU = swh_KU.dropna(dim='TIME')
# swh_KU.plot(color='r',linestyle='--',marker='o')
# plt.title('SARAL swh_KU')

s3 = xr.open_dataset('D:/wzx/data/SENTINEL-3A/IMOS_SRS-Surface-Waves_MW_SENTINEL-3A_FV02_065N-180E-DM00.nc')
swh_KU_s3 = s3['SWH_KU_CAL']
# swh_KU[swh_KU>30] = np.nan
# swhKU = swh_KU.dropna(dim='TIME')
swh_KU_s3.plot(color='g',linestyle='--',marker='x',label='SENTINEL-3A')
# plt.title('SENTINEL-3A swh_KU')
plt.legend()
plt.title('65N 180E Calibrated significant wave height')

topex = xr.open_dataset('D:/wzx/data/TOPEX/IMOS_SRS-Surface-Waves_MW_TOPEX_FV02_065N-180E-DM00.nc')
swh_KU_topex = topex['SWH_KU_CAL']
# swh_KU[swh_KU>30] = np.nan
# swhKU = swh_KU.dropna(dim='TIME')
swh_KU_topex.plot(color='k',linestyle='--',marker='o')
# plt.title('TOPEX swh_KU')







swhKUdf = swhKU.to_dataframe()
a = swhKUdf['SWH_KU_CAL'].value_counts()
# plot number of waves
plt.bar(a.index,a.values)
plt.ylabel('number of waves')
plt.xlabel('Hs(m)')










# swh_rsp = swh_KU.resample(TIME='1D',skipna=True).interpolate('linear')




#drop Nan data in dataframe according to the value
# a = a[a.values != 967]


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


