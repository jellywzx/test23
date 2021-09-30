from netCDF4 import Dataset
# rootgrp = Dataset("test.nc","w",format="NETCDF4")
# print(rootgrp.data_model)
# rootgrp.close()
rootgrp= Dataset("test.nc", "a")
fcstgrp = rootgrp.createGroup("forecasts")
analgrp = rootgrp.createGroup("analyses")
print(rootgrp.groups)
fcstgrp1 = rootgrp.createGroup("/forecasts/model1")
fcstgrp2 = rootgrp.createGroup("/forecasts/model2")
def walktree(top):
    yield top.group.values()
    for value in top.groups.values():
        yield from walktree(value)
print(rootgrp)
# for children in walktree(rootgrp):
#     for child in children:
#         print(child)

level = rootgrp.createDimension("level",None)
time = rootgrp.createDimension("time",None)
lat = rootgrp.createDimension("lat",73)
lon = rootgrp.createDimension("lon",144)
print(rootgrp.dimensions)

print(len(lon))
print(lon.isunlimited())
print(time.isunlimited())
for dimobj in rootgrp.dimensions.value():
    print(dimobj)