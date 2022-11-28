# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:29:08 2022

@author: davi.nascimento
"""
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('iris.csv')

df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width','variety']



fig = plt.figure()

spec = fig.add_gridspec(3,3)


ax0 = fig.add_subplot(spec[0, :])
ax0.plot(df['sepal_length'])



ax1 = fig.add_subplot(spec[1,0])
ax1.scatter(df['petal_length'], df['petal_width'])


ax2 = fig.add_subplot(spec[1,1])
ax2.plot(df['sepal_width'], color='r')



ax3 = fig.add_subplot(spec[1:,2])
ax3.bar(df['sepal_length'], df['sepal_width'])



ax4 = fig.add_subplot(spec[2,:2])
ax4.plot(df['sepal_length'])


plt.show()


# fig = plt.figure()

# spec = fig.add_gridspec(2,2)


# ax0 = fig.add_subplot(spec[0, :])
# ax0.plot(df['sepal_length'])

# ax1= fig.add_subplot(spec[1,0])

# ax1.scatter(df['petal_length'],df['petal_width'])


# ax2= fig.add_subplot(spec[1,1])
# ax2.plot(df['sepal_width'], color='r')


# plt.plot(df['sepal_length'])
# plt.show()