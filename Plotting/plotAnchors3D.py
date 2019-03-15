#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:56:00 2019

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import json


with open('anchors.json', 'r') as file:
    anchorsDict = json.load(file)
    anchors = np.array([])
    for item in anchorsDict.values():
        if item['id'] != '0x0':
            temp = [item['id'], item['pos']['x'], item['pos']['y'], item['pos']['z']]
            anchors = np.append(anchors, temp, 0)

anchors = np.reshape(anchors, (len(anchorsDict)-1, 4))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Prepare all arrays for plotting
ancName = []
x = [] #anchors
y = []
z = []
i = 0
for row in anchors:
    ancName.append(row[0])
    x.append(float(row[1]))
    y.append(float(row[2]))
    z.append(float(row[3]))

# Plots points and annotate
ax.scatter(x, y, z, c='r', marker='o')
for i in range(0, len(ancName)):
#    label = ancName[i][2:]+' ('+str(x[i])+','+str(y[i])+','+str(z[i])+')'
    label = ancName[i][2:]
    ax.text(x[i], y[i], z[i], label)

# Plot pitch dimensions
X = np.arange(-45, 45)
Y = np.arange(0, 70)
X, Y = np.meshgrid(X, Y)
Z = np.zeros((70,90))
surf = ax.plot_surface(X, Y, Z, color='green', linewidth=1, antialiased=True)


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
