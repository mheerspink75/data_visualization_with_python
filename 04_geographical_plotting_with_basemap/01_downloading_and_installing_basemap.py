# conda install -c anaconda basemap
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap()

m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()

plt.show()
