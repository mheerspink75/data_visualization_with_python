import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('./01_different_types_of_basic_Matplotlib_charts/csv_example.txt' , delimiter=',', unpack=True)

plt.plot(x,y,label='Loaded from File')
plt.xlabel('Plot Number')
plt.ylabel('Randomly Chosen Tutorial #')
plt.legend()
plt.title('Awesome Graph')
plt.show()