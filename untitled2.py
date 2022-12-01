# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:33:29 2022

@author: davi.nascimento
"""

import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()

spec = fig.add_gridspec(1,2)

ax1 = fig.add_subplot(spec[0], projection='3d')
ax2 = fig.add_subplot(spec[1], projection='3d')
# ax = plt.axes(projection='3d')



# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax1.plot3D(xline, yline, zline, 'gray')

# # Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax2.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

plt.show()