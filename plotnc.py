# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import cartopy.crs as ccrs
# m=Basemap(projection='mill')
# m.drawcoastlines()
# plt.show()

# ax = plt.axes(projection=ccrs.PlateCarree())
# ax.coastlines()
# # plt.savefig('coastlines.pdf')
# # plt.savefig('coastlines.png')
# plt.show()

# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt
#
# ax = plt.axes(projection=ccrs.Mollweide())
# ax.stock_img()
# plt.show()
#
# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt
#
# ax = plt.axes(projection=ccrs.PlateCarree())
# ax.stock_img()
#
# ny_lon, ny_lat = -75, 43
# delhi_lon, delhi_lat = 77.23, 28.61
#
# plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
#          color='blue', linewidth=2, marker='o',
#          transform=ccrs.Geodetic(),
#          )
#
# plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
#          color='gray', linestyle='--',
#          transform=ccrs.PlateCarree(),
#          )
#
# plt.text(ny_lon - 3, ny_lat - 12, 'New York',
#          horizontalalignment='right',
#          transform=ccrs.Geodetic())
#
# plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
#          horizontalalignment='left',
#          transform=ccrs.Geodetic())
#
# plt.show()


import matplotlib.pyplot as plt
fig, ax =plt.subplots()