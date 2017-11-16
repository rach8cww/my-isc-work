print
print "Gridded Plotting Exercise"
print

import matplotlib.pyplot as plt # imports pyplot as plt
from map_data.py import *
from mpl_toolkits.basemap import Basemap

# part 1 - NetCDF and plotting

fig = plt.figure()

m = Basemap(projection = 'cyl', 11crnrlat = -90, urcrnrlat = 90, 11crnrlon = -180, urcrnrlon = 180, resolution = 'c')

m.drawcoastlines()

im1 = m.pcolormesh(lons, lats, tas, shading = 'flat',
cmap = plt.cm.jet, latlon = True)

plt.savefig('tas1.png')
plt.pause(20)
