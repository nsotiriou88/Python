#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:08:54 2019

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

#%% Import functions

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#%% Define useful functions

def cart2pol(X):
    rho = np.sqrt(X[:, 0]**2 + X[:, 1]**2)
    phi = np.arctan2(X[:, 1], X[:, 0])
    return(rho, phi)


#%% Read in data from CSV file

data = pd.read_csv('M_O2.SCOUT.csv', header= None)  # read in CSV data using pandas data frame
data = data.values
data = data[:, 1:4]


#%%  Do subtractions and translations

translated_data = np.zeros(np.shape(data))

for i in range( len( data ) ):
   translated_data[i, :] = data[i, :] - data[0, :]

#%% Rotate data 
   
#sort_index = np.argsort(translated_data[:, 0])
#print(np.column_stack((translated_data[sort_index, :],sort_index)))
   
x_dir = translated_data[96, :] - translated_data[100, :]   
y_dir = translated_data[105, :] - translated_data[100, :]   

x_vec = x_dir/np.linalg.norm(x_dir)
y_vec = y_dir/np.linalg.norm(y_dir)
z_vec = np.cross(x_vec, y_vec)

y_vec2 = np.cross(z_vec, x_vec)

rotate_mat = np.array([x_vec, y_vec2, z_vec])

rotated_data = np.transpose(np.dot(rotate_mat,np.transpose(translated_data)))
   
   
#%% Divide data into three categories
   
Floor = rotated_data[rotated_data[:, 2] < 1, :]   
Railings = rotated_data[(rotated_data[:, 2] > 1)&(rotated_data[:, 2] < 10), :]   
Catwalk = rotated_data[rotated_data[:, 2] > 10, :]   

# Try and pull out the perimeter points
Ring = np.linalg.norm(Catwalk[:, 0:2], axis = 1)
Perimeter = Catwalk[Ring>40, :]


#np.column_stack((Perimeter[sort_index, :], sort_index))
PList = np.array([24, 0, 17, 2, 1, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19])
locs1 = Perimeter[PList, 0:2]
(rho, phi) = cart2pol(locs1)
sort_index = np.argsort(phi)
locs2 = Perimeter[PList, :]
locs3 = locs2[sort_index, :]
locs3 = np.row_stack((locs3,locs3[0, :]))


Field_Corners = np.zeros(shape = (4,3))
Field_Corners[0, :] = [-27.5, 16.0, 0.0]
Field_Corners[1, :] = [-27.5, -16.0, 0.0]
Field_Corners[2, :] = [27.5, -16.0, 0.0]
Field_Corners[3, :] = [27.5, 16.0, 0.0]

#%%
X = translated_data[:, 0]
Y = translated_data[:, 1]
Z = translated_data[:, 2]

fig = plt.figure()
ax = Axes3D(fig)


ax.scatter(rotated_data[:, 0], rotated_data[:, 1], rotated_data[:, 2], color='black')
ax.plot(locs3[:, 0], locs3[:, 1], locs3[:, 2], color='red')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Plot the field
verts = [list(zip(Field_Corners[:, 0],Field_Corners[:, 1], Field_Corners[:, 2]))]
ax.add_collection3d(Poly3DCollection(verts, facecolors = 'green'))


max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

#plt.gca().set_aspect('equal', adjustable='box')
plt.show()