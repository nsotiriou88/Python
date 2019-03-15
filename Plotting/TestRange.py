# -*- coding: utf-8 -*-
"""
Created on Thu July 5 11:05:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json


### START ###
# Importing the dataset
dataset = pd.read_csv('exp0.csv', delimiter = ';')
session = dataset.iloc[:, [0, 1, 2]].values

# Keep the timestamp of the first recorded packet for reference
startTime = session[0][0]

masterID = '0x78C'
anchor1ID = '0x9CB'
anchor2ID = '0x9B6'

master1 = []
master2 = []
anchor1 = []
anchor2 = []

for line in session:
    if line[1] == masterID:
        data = json.loads(line[2])
        for item in data:
            if item['anchor'] == anchor1ID:
                master1.append([float(item['dist']), float(item['rssi'])])
            elif item['anchor'] == anchor2ID:
                master2.append([float(item['dist']), float(item['rssi'])])
    elif line[1] == anchor1ID:
        data = json.loads(line[2])
        for item in data:
            if item['anchor'] == masterID:
                anchor1.append([float(item['dist']), float(item['rssi'])])
    elif line[1] == anchor2ID:
        data = json.loads(line[2])
        for item in data:
            if item['anchor'] == masterID:
                anchor2.append([float(item['dist']), float(item['rssi'])])

# Convert list to numpy array
master1 = np.array(master1)
master2 = np.array(master2)
anchor1 = np.array(anchor1)
anchor2 = np.array(anchor2)


# Plotting Stuff
plt.subplot(221)
plt.plot(master1[:, 0], master1[:, 1], 'r.')
plt.title('Master report to '+anchor1ID+' (rssi-dist) - Max dist:'+str(np.max(master1[:, 0]))+' - Total:'+str(master1.shape[0]))
plt.xlabel('dist (m)')
plt.ylabel('rssi (db)')
plt.grid(linestyle='--', linewidth=1)

plt.subplot(222)
plt.plot(anchor1[:, 0], anchor1[:, 1], 'b.')
plt.title('Anchor '+anchor1ID+' report to Master (rssi-dist) - Max dist:'+str(np.max(anchor1[:, 0]))+' - Total:'+str(anchor1.shape[0]))
plt.xlabel('dist (m)')
plt.ylabel('rssi (db)')
plt.grid(linestyle='--', linewidth=1)

plt.subplot(223)
plt.plot(master2[:, 0], master2[:, 1], 'r.')
plt.title('Master report to '+anchor2ID+' (rssi-dist) - Max dist:'+str(np.max(master2[:, 0]))+' - Total:'+str(master2.shape[0]))
plt.xlabel('dist (m)')
plt.ylabel('rssi (db)')
plt.grid(linestyle='--', linewidth=1)

plt.subplot(224)
plt.plot(anchor2[:, 0], anchor2[:, 1], 'b.')
plt.title('Anchor '+anchor2ID+' report to Master (rssi-dist) - Max dist:'+str(np.max(anchor2[:, 0]))+' - Total:'+str(anchor1.shape[0]))
plt.xlabel('dist (m)')
plt.ylabel('rssi (db)')
plt.grid(linestyle='--', linewidth=1)


plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
#plt.savefig('plots/'+tagName+'.png')
plt.show()

