import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pylab import cm
import scipy.integrate as integrate


# Edit the font, font size, and axes width
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['font.size'] = 22

# creating a figure, adding an axes and setting limits
fig = plt.figure(figsize=(10.5, 6))
ax = plt.axes()
ax.set_aspect('equal')

# setting facecolor
ax.set_facecolor('k')

# setting figure window color
fig.patch.set_facecolor('k')

# labels
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_title('2D Random Walk', color='w', size=20)

# adjusting ticks
ax.xaxis.set_tick_params(which='major', size=10,
                         width=2, direction='out', top='')
ax.yaxis.set_tick_params(which='major', size=10,
                         width=2, direction='out', right='')

# setting up a dice list from which a moving direction in 2D, each equally probable, will be drawn
dice = ['up', 'down', 'right', 'left']

# setting up initial conditions
x = 0
y = 0
t = 0

# number of iterations
n = 1000

# generating colors
colors = cm.get_cmap('prism', n)

# setting up the loop & if conditions
while t < n:
    x0 = x
    y0 = y

    # random index, which will be used to draw a direction from the dice list. Analagous to a throw of the dice
    roll = int(np.random.randint(0, 4, 1))

    # drawing from the dice list
    direction = dice[roll]

    # setting up if conditions depending on the direction drawn
    if direction == 'up':
        y += 0.1
        ax.plot([x0, x], [y0, y], '-', color=colors(t), marker='s')
    elif direction == 'down':
        y -= 0.1
        ax.plot([x0, x], [y0, y], '-', color=colors(t), marker='s')
    elif direction == 'right':
        x += 0.1
        ax.plot([x0, x], [y0, y], '-', color=colors(t), marker='s')
    elif direction == 'left':
        x -= 0.1
        ax.plot([x0, x], [y0, y], '-', color=colors(t), marker='s')

    plt.pause(0.1)
    # incrementing the time
    t += 1

plt.show()
