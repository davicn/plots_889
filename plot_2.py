# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:09:23 2022

@author: davi.nascimento
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('iris.csv')

df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width','variety']

types = df['variety'].unique() #['Setosa', 'Versicolor', 'Virginica']


df1 = df[df['variety']==types[0]]
df2 = df[df['variety']==types[1]]
df3 = df[df['variety']==types[2]]

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

# ax.plot(1,1,1, marker='o')

ax.scatter(df1['sepal_length'], df1['sepal_width'], df1['petal_length'], label=types[0], marker='^')
ax.scatter(df2['sepal_length'], df2['sepal_width'], df2['petal_length'], label=types[1])
ax.scatter(df3['sepal_length'], df3['sepal_width'], df3['petal_length'], label=types[2])


ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
ax.set_zlabel('petal_length')

ax.legend()


plt.show()