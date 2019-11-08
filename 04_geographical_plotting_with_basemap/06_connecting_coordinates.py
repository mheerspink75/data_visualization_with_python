from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
            llcrnrlat=20,
            llcrnrlon=-130,
            urcrnrlat=50,
            urcrnrlon=-60,
            resolution='l')


m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='black')

xs = []
ys = []

# 29 north 95 west
# Houston, TX
hlat, hlon = 29.7604, -95.3698
xpt, ypt = m(hlon, hlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'r*', markersize=15)

# Boulder, CO
blat, blon = 40.125, -104.237
xpt, ypt = m(blon, blat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'bo')

land_check = m.is_land(xpt, ypt)
print(land_check)

m.plot(xs, ys, 'r', linewidth=2, label='Flight 115')

m.drawgreatcircle(hlon, hlat, blon, blat, linewidth=2, color='c', label='Great circle')

plt.legend()
plt.title('Basemap Example with Title')
plt.show()