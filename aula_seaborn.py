# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 19:51:42 2022

@author: davi.nascimento
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('iris.csv')

df.columns = ['sepal_length', 'sepal_width', 
              'petal_length', 'petal_width','variety']

sns.pairplot(data=df, hue='variety')

# plot 9
# mc = df.corr()

# sns.heatmap(data=mc, annot=True, cmap='crest')


plt.show()
# fig = plt.figure()

# spec = fig.add_gridspec(2,2)

# fig, axes = plt.subplots(2, 2)



# ax0 = fig.add_subplot(spec[0,0])
# sns.set_theme(style='white',  palette="Set2")

# Plot 8
# fig, axes = plt.subplots(1,3)

# sns.violinplot(data=df, y='sepal_width',ax=axes[0])
# axes[0].set_title('Violin Plot')

# sns.boxplot(data=df, y='sepal_width',ax=axes[1])
# axes[1].set_title('Box Plot')
# sns.kdeplot(data=df, y='sepal_width',ax=axes[2])
# axes[2].set_title('KDE Plot')



#plot
# sns.boxplot(data=df, x='variety',y='petal_width', hue='variety')


# Plot 6
# fig, axes = plt.subplots(2,2)

# sns.kdeplot(data=df, x='sepal_length', hue='variety',ax=axes[0,0])
# sns.kdeplot(data=df, x='sepal_width', hue='variety',ax=axes[1,0])
# sns.kdeplot(data=df, x='petal_length', hue='variety',ax=axes[0,1])
# sns.kdeplot(data=df, x='petal_width', hue='variety',ax=axes[1,1])



# Plot 5
# sns.displot(data=df, 
#             x='petal_width', 
#             kde=True,
#             hue='variety')



# sns.kdeplot(data=df, x='petal_width', hue='variety')

# sns.stripplot(data=df,
#               x='variety',
#               y='petal_width')

# Plot 4

# sns.scatterplot(data=df, 
#               y='sepal_length', 
#               x='sepal_width',
#               hue='variety')


# plot 3
# sns.lineplot(data=df, 
#              y='sepal_length', 
#              x='sepal_width',
#              hue='variety')

# Plot 2
# sns.lineplot(data=df, y='sepal_length', x='sepal_width')

# Plot 1
# d = np.random.rand(4)

# sns.set_theme(style='darkgrid',  palette="pastel")

# sns.lineplot(
#     x=['a','b','c','d'],
#     y=d)




