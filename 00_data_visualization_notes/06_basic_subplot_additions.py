import random
import matplotlib.pyplot as plt

# if you just show one graph, you don’t need to define a figure
fig = plt.figure()


def create_plots():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(8)
        xs.append(x)
        ys.append(y)
    return xs, ys


# first axis: height, width, subplot number
ax1 = fig.add_subplot(311)
# second axis
ax2 = fig.add_subplot(312)
# third axis
ax3 = fig.add_subplot(313)

x, y = create_plots()
ax1.plot(x, y)

x, y = create_plots()
ax2.plot(x, y)

x, y = create_plots()
ax3.plot(x, y)

plt.show()
