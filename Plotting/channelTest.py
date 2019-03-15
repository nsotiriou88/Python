# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:45:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

# Importing the dataset
dataset = pd.read_csv('DanTestNew.csv', delimiter = ';')
session = dataset.iloc[:, [0, 1, 11]].values

# Identify all tags by checking first 100 packets
tags = []
for i in range(0, 100):
    if session[i][0] not in tags:
        tags.append(session[i][0])

for tagName in tags:
    plt.clf()
    # Separate tags in different arrays
    tag = [session[i, :] for i in range(np.size(session, 0)) if session[i, 0] == tagName]
    
    # Create the rssi1 and dist lists from json file
    tagRssi = np.array([])
    tagRssi2 = np.array([])
    tagDist = np.array([])
    timestamp = np.array([])
    
    for i in range(len(tag)):
        data = json.loads(tag[i][2])
        timestamp = np.append(timestamp, float(tag[i][1]))
        for item in data:
            tagRssi = np.append(tagRssi, float(item['rssi']))
            tagRssi2 = np.append(tagRssi2, float(item['rssi2']))
            tagDist = np.append(tagDist, float(item['dist']))
    
    # Plotting Stuff
    plt.subplot(311)
    plt.plot(timestamp, tagRssi, 'r-')
    plt.title('Master to '+tagName+' rssi')
    plt.ylabel('rssi1 (db)')
    plt.grid(linestyle='--', linewidth=1)

    plt.subplot(312)
    plt.plot(timestamp, tagRssi2, 'r-')
    plt.title('Master to '+tagName+' rssi2')
    plt.ylabel('rssi2 (db)')
    plt.grid(linestyle='--', linewidth=1)
    
    plt.subplot(313)
    plt.plot(timestamp, tagDist, 'bo')
    plt.title('Master to '+tagName+' dist')
    plt.xlabel('timestamp')
    plt.ylabel('dist (m)')
    plt.grid(linestyle='--', linewidth=1)
    
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    #plt.savefig('plots/'+tagName+'.png')
    plt.show()
    
    