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
dataset = pd.read_csv('channel5-2.csv', delimiter = ',')
session = dataset.iloc[:, [0, 1, 2]].values

first_timestamp = session[0][0]

# Identify all tags by checking first 100 packets
tags = []
for i in range(0, 1000):
    if session[i][1] not in tags:
        tags.append(session[i][1])

tagName1 = '4EDC' # Man Antennas
tagName2 = '5081'
tagName3 = '50A2'
tagName4 = '4ED9' # UWB 3-5 Antennas
tagName5 = '4ED8'
tagName6 = '5087'

# Separate tags in different arrays
tag1 = [session[i, :] for i in range(np.size(session, 0)) if session[i, 1] == tagName1]
tag2 = [session[i, :] for i in range(np.size(session, 0)) if session[i, 1] == tagName2]
tag3 = [session[i, :] for i in range(np.size(session, 0)) if session[i, 1] == tagName3]
tag4 = [session[i, :] for i in range(np.size(session, 0)) if session[i, 1] == tagName4]
tag5 = [session[i, :] for i in range(np.size(session, 0)) if session[i, 1] == tagName5]
tag6 = [session[i, :] for i in range(np.size(session, 0)) if session[i, 1] == tagName6]

# Create the rssi1 and dist lists from json file
tag1Rssi = np.array([])
tag1Rssi2 = np.array([])
tag1Dist = np.array([])
timestamp1 = np.array([])

tag2Rssi = np.array([])
tag2Rssi2 = np.array([])
tag2Dist = np.array([])
timestamp2 = np.array([])

tag3Rssi = np.array([])
tag3Rssi2 = np.array([])
tag3Dist = np.array([])
timestamp3 = np.array([])

tag4Rssi = np.array([])
tag4Rssi2 = np.array([])
tag4Dist = np.array([])
timestamp4 = np.array([])

tag5Rssi = np.array([])
tag5Rssi2 = np.array([])
tag5Dist = np.array([])
timestamp5 = np.array([])

tag6Rssi = np.array([])
tag6Rssi2 = np.array([])
tag6Dist = np.array([])
timestamp6 = np.array([])

for i in range(len(tag1)):
    data = json.loads(tag1[i][2])
    timestamp1 = np.append(timestamp1, float(tag1[i][0]-first_timestamp))
#    for item in data:
    tag1Rssi = np.append(tag1Rssi, float(data[0]['rssi']))
    tag1Rssi2 = np.append(tag1Rssi2, float(data[0]['rssi2']))
    tag1Dist = np.append(tag1Dist, float(data[0]['dist']))
for i in range(len(tag2)):
    data = json.loads(tag2[i][2])
    timestamp2 = np.append(timestamp2, float(tag2[i][0]-first_timestamp))
#    for item in data:
    tag2Rssi = np.append(tag2Rssi, float(data[0]['rssi']))
    tag2Rssi2 = np.append(tag2Rssi2, float(data[0]['rssi2']))
    tag2Dist = np.append(tag2Dist, float(data[0]['dist']))
for i in range(len(tag3)):
    data = json.loads(tag3[i][2])
    timestamp3 = np.append(timestamp3, float(tag3[i][0]-first_timestamp))
#    for item in data:
    tag3Rssi = np.append(tag3Rssi, float(data[0]['rssi']))
    tag3Rssi2 = np.append(tag3Rssi2, float(data[0]['rssi2']))
    tag3Dist = np.append(tag3Dist, float(data[0]['dist']))
for i in range(len(tag4)):
    data = json.loads(tag4[i][2])
    timestamp4 = np.append(timestamp4, float(tag4[i][0]-first_timestamp))
#    for item in data:
    tag4Rssi = np.append(tag4Rssi, float(data[0]['rssi']))
    tag4Rssi2 = np.append(tag4Rssi2, float(data[0]['rssi2']))
    tag4Dist = np.append(tag4Dist, float(data[0]['dist']))
for i in range(len(tag5)):
    data = json.loads(tag5[i][2])
    timestamp5 = np.append(timestamp5, float(tag5[i][0]-first_timestamp))
#    for item in data:
    tag5Rssi = np.append(tag5Rssi, float(data[0]['rssi']))
    tag5Rssi2 = np.append(tag5Rssi2, float(data[0]['rssi2']))
    tag5Dist = np.append(tag5Dist, float(data[0]['dist']))
for i in range(len(tag6)):
    data = json.loads(tag6[i][2])
    timestamp6 = np.append(timestamp6, float(tag6[i][0]-first_timestamp))
#    for item in data:
    tag6Rssi = np.append(tag6Rssi, float(data[0]['rssi']))
    tag6Rssi2 = np.append(tag6Rssi2, float(data[0]['rssi2']))
    tag6Dist = np.append(tag6Dist, float(data[0]['dist']))

# Plotting Stuff

#plt.subplot(211)
#plt.plot(tag1Dist, tag1Rssi, 'r.', markersize = 0.5)
#plt.plot(tag2Dist, tag2Rssi, 'g.', markersize = 0.5)
#plt.plot(tag3Dist, tag3Rssi, 'y.', markersize = 0.5)
#plt.plot(tag4Dist, tag4Rssi, 'b.', markersize = 0.5)
#plt.plot(tag5Dist, tag5Rssi, 'c.', markersize = 0.5)
#plt.plot(tag6Dist, tag6Rssi, 'm.', markersize = 0.5)

#plt.plot(tag1Dist, tag1Rssi, 'r-', linewidth = 0.5)
#plt.plot(tag2Dist, tag2Rssi, 'g-', linewidth = 0.5)
#plt.plot(tag3Dist, tag3Rssi, 'y-', linewidth = 0.5)
#plt.plot(tag4Dist, tag4Rssi, 'b-', linewidth = 0.5)
#plt.plot(tag5Dist, tag5Rssi, 'c-', linewidth = 0.5)
#plt.plot(tag6Dist, tag6Rssi, 'm-', linewidth = 0.5)
#plt.title('Master to '+tagName1+'(red)-'+tagName2+'(green)-'+tagName3+'(yellow)-'+tagName4+'(blueSP)-'+tagName5+'(cyanSP)-'+tagName6+'(magentaSP) rssi')
#plt.xlabel('Distance (m)')
#plt.ylabel('rssi1 (db)')
#plt.grid(linestyle='--', linewidth=1)
#
#plt.subplot(212)
#plt.plot(tag1Dist, tag1Rssi2, 'r.', markersize = 0.5)
#plt.plot(tag2Dist, tag2Rssi2, 'g.', markersize = 0.5)
#plt.plot(tag3Dist, tag3Rssi2, 'y.', markersize = 0.5)
#plt.plot(tag4Dist, tag4Rssi2, 'b.', markersize = 0.5)
#plt.plot(tag5Dist, tag5Rssi2, 'c.', markersize = 0.5)
#plt.plot(tag6Dist, tag6Rssi2, 'm.', markersize = 0.5)

#plt.plot(tag1Dist, tag1Rssi2, 'r-', linewidth = 0.5)
#plt.plot(tag2Dist, tag2Rssi2, 'g-', linewidth = 0.5)
#plt.plot(tag3Dist, tag3Rssi2, 'y-', linewidth = 0.5)
#plt.plot(tag4Dist, tag4Rssi2, 'b-', linewidth = 0.5)
#plt.plot(tag5Dist, tag5Rssi2, 'c-', linewidth = 0.5)
#plt.plot(tag6Dist, tag6Rssi2, 'm-', linewidth = 0.5)
#plt.title('Master to '+tagName1+'(red)-'+tagName2+'(green)-'+tagName3+'(yellow)-'+tagName4+'(blueSP)-'+tagName5+'(cyanSP)-'+tagName6+'(magentaSP) rssi2')
#plt.xlabel('Distance (m)')
#plt.ylabel('rssi2 (db)')
#plt.grid(linestyle='--', linewidth=1)


#====================================
#====================================

plt.subplot(311)
plt.plot(timestamp1, tag1Rssi, 'r-', linewidth = 0.5)
#plt.plot(timestamp2, tag2Rssi, 'g-', linewidth = 0.5)
#plt.plot(timestamp3, tag3Rssi, 'y-', linewidth = 0.5)
plt.plot(timestamp4, tag4Rssi, 'b-', linewidth = 0.5)
#plt.plot(timestamp5, tag5Rssi, 'c-', linewidth = 0.5)
#plt.plot(timestamp6, tag6Rssi, 'm-', linewidth = 0.5)
plt.title('Master to '+tagName1+'(red)-'+tagName2+'(green)-'+tagName3+'(yellow)-'+tagName4+'(blueSP)-'+tagName5+'(cyanSP)-'+tagName6+'(magentaSP) rssi')
plt.xlabel('samples over time')
plt.ylabel('rssi1 (db)')
plt.grid(linestyle='--', linewidth=1)

plt.subplot(312)
plt.plot(timestamp1, tag1Rssi2, 'r-', linewidth = 0.5)
#plt.plot(timestamp2, tag2Rssi2, 'g-', linewidth = 0.5)
#plt.plot(timestamp3, tag3Rssi2, 'y-', linewidth = 0.5)
plt.plot(timestamp4, tag4Rssi2, 'b-', linewidth = 0.5)
#plt.plot(timestamp5, tag5Rssi2, 'c-', linewidth = 0.5)
#plt.plot(timestamp6, tag6Rssi2, 'm-', linewidth = 0.5)
plt.title('Master to '+tagName1+'(red)-'+tagName2+'(green)-'+tagName3+'(yellow)-'+tagName4+'(blueSP)-'+tagName5+'(cyanSP)-'+tagName6+'(magentaSP) rssi2')
plt.xlabel('samples over time')
plt.ylabel('rssi2 (db)')
plt.grid(linestyle='--', linewidth=1)

plt.subplot(313)
plt.plot(timestamp1, tag1Dist, 'r.', markersize = 0.5)
#plt.plot(timestamp2, tag2Dist, 'g.', markersize = 0.5)
#plt.plot(timestamp3, tag3Dist, 'y.', markersize = 0.5)
plt.plot(timestamp4, tag4Dist, 'b.', markersize = 0.5)
#plt.plot(timestamp5, tag5Dist, 'c.', markersize = 0.5)
#plt.plot(timestamp6, tag6Dist, 'm.', markersize = 0.5)
plt.xlabel('samples over time')
plt.ylabel('dist (m)')
plt.grid(linestyle='--', linewidth=1)


#====================================
#====================================


#plt.subplot(813)
#plt.plot(timestamp1, tag1Dist, 'r.', markersize = 0.5)
#plt.title('Master to '+tagName1+' dist')
#plt.xlabel('samples over time')
#plt.ylabel('dist (m)')
#plt.grid(linestyle='--', linewidth=1)
#
#plt.subplot(814)
#plt.plot(timestamp2, tag2Dist, 'g.', markersize = 0.5)
#plt.title('Master to '+tagName2+' dist')
#plt.xlabel('samples over time')
#plt.ylabel('dist (m)')
#plt.grid(linestyle='--', linewidth=1)
#
#plt.subplot(815)
#plt.plot(timestamp3, tag3Dist, 'y.', markersize = 0.5)
#plt.title('Master to '+tagName3+' dist')
#plt.xlabel('samples over time')
#plt.ylabel('dist (m)')
#plt.grid(linestyle='--', linewidth=1)
#
#plt.subplot(816)
#plt.plot(timestamp4, tag4Dist, 'b.', markersize = 0.5)
#plt.title('Master to '+tagName4+' dist')
#plt.xlabel('samples over time')
#plt.ylabel('dist (m)')
#plt.grid(linestyle='--', linewidth=1)
#
#plt.subplot(817)
#plt.plot(timestamp5, tag5Dist, 'c.', markersize = 0.5)
#plt.title('Master to '+tagName5+' dist')
#plt.xlabel('samples over time')
#plt.ylabel('dist (m)')
#plt.grid(linestyle='--', linewidth=1)
#
#plt.subplot(818)
#plt.plot(timestamp6, tag6Dist, 'm.', markersize = 0.5)
#plt.title('Master to '+tagName6+' dist')
#plt.xlabel('samples over time')
#plt.ylabel('dist (m)')
#plt.grid(linestyle='--', linewidth=1)


plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
#plt.savefig('plots/'+tagName+'.png')
plt.show()
