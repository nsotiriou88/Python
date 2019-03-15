#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu July 5 11:05:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88


This script is for extracting results (RSSI, anchor coverage etc.)
in a heatmap format. It reads from a csv file and anchors.json.
NOTE: This script does not use database access, therefore it cannot
load huge session files. The purpose of this script is for testing
experiments. Please make sure that master is the first anchor in the
anchors.json"""

#Imports
import os
import numpy as np
import json
import csv
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib as mpl
# import sys
# from mpl_toolkits.mplot3d import Axes3D



def plot_field():
    """This functions plots the outlines for the Rugby field. Please
    change the dimensions of the field according to the venue, for more
    accurate results. It also cleans the previous plot canvas."""
    plt.clf()
    #Plot field
    plt.plot([-50,-50], [0,70], 'k-')
    plt.plot([0,0], [0,70], 'k-')
    plt.plot([50,50], [0,70], 'k-')
    plt.plot([-50,50], [70,70], 'k-')
    plt.plot([-50,50], [0,0], 'k-')
    #Plot hut
    plt.plot([-5,5], [-8,-8], 'k-')
    plt.plot([-5,5], [-4,-4], 'k-')
    plt.plot([-5,-5], [-4,-8], 'k-')
    plt.plot([5,5], [-4,-8], 'k-')
    #Plot hut left
    plt.plot([-6,-12], [-8,-8], 'k-')
    plt.plot([-6,-12], [-4,-4], 'k-')
    plt.plot([-6,-6], [-4,-8], 'k-')
    plt.plot([-12,-12], [-4,-8], 'k-')
    #Plot hut right
    plt.plot([6,12], [-8,-8], 'k-')
    plt.plot([6,12], [-4,-4], 'k-')
    plt.plot([6,6], [-4,-8], 'k-')
    plt.plot([12,12], [-4,-8], 'k-')
    #Plot stand
    plt.plot([-50,25], [80,80], 'k-')
    plt.plot([-50,25], [85,85], 'k-')
    plt.plot([-50,-50], [80,85], 'k-')
    plt.plot([25,25], [80,85], 'k-')
    plt.annotate('STANDS', xy=(-25, 81), xytext=(-25, 81))
    #Plot stand left
    plt.plot([-70,-67], [10,10], 'k-')
    plt.plot([-70,-67], [60,60], 'k-')
    plt.plot([-70,-70], [10,60], 'k-')
    plt.plot([-67,-67], [10,60], 'k-')
    plt.annotate('STANDS', xy=(-65, 35), xytext=(-65, 35), rotation=90)
    #Plot tower
    plt.plot([-70], [85], 'gx')
    plt.annotate('TOWER', xy=(-70, 85), xytext=(-70, 85))
    #Minimise white space on sides
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    

def plot_anchors():
    """Plots the anchor positions and names on the field."""
    anchi = []
    xi, yi = np.array([]), np.array([])
    # zi = np.array([])
    with open('anchors.json', 'r') as file:
        datai = json.load(file)
        for key, _ in datai.items():
            if key != '0x0':
                xi = np.append(xi, float(datai[key]['pos']['x']))
                yi = np.append(yi, float(datai[key]['pos']['y']))
                # zi = np.append(zi, float(datai[key]['pos']['z']))
                if float(datai[key]['pos']['z']) > 13:
                    anchi.append(key+'HLi')
                else:
                    anchi.append(key)
    plt.plot(xi, yi, 'r.')
    for i in range(len(anchi)):
        if i%2 == 0:
            plt.annotate(anchi[i], xy=(xi[i], yi[i]), xytext=(xi[i]-8, yi[i]))
        else:
            plt.annotate(anchi[i], xy=(xi[i], yi[i]), xytext=(xi[i]-8, yi[i]-3.5))


################## START ##################
#%% Dictionary for registering CSV rows and anchors.json
anchors = [] 
sessionDict = {}
with open('anchors.json', 'r') as file:
    dataAnc = json.load(file)
    for key, _ in dataAnc.items():
        if key != '0x0':
            anchors.append(key)
            
# Separate csv files to file per # Separate csv files to file per 
dataset = pd.read_csv('6 anchor replaced 2.csv', delimiter=',', encoding="ISO-8859-1")
tags = dataset.tag_id.unique()
for tag in tags:
    df = dataset.loc[dataset['tag_id'] == tag]
    with open(tag+'.csv', 'w') as file_out:
        df.to_csv(file_out, index=False)


#%% Open the csv file
files = [file for file in os.listdir('.') if os.path.isfile(file)]
for file in files:
    if file[-3:] == 'csv':
        f = file
with open(f, 'r') as csvfile:
    #iterate through packets
    session = csv.reader(csvfile, delimiter=',')
    i=0
    for row in session:
        #build dictionary
        if i == 0:
            for item in row:
                sessionDict[item] = []
            
        #add column values in dictionary(comment out not needed ones for better performance)
        if i != 0: #REVIEW
            sessionDict['tag_id'].append(row[0])
            sessionDict['timestamp'].append(float(row[1]))
            # sessionDict['timelocal'].append(float(row[2]))
            sessionDict['x'].append(float(row[3]))
            sessionDict['y'].append(float(row[4]))
            # sessionDict['z'].append(float(row[5]))
            # sessionDict['ball'].append(row[6])
            # sessionDict['ball_stats'].append(row[7])
            sessionDict['imu_raw'].append(row[8])
            # sessionDict['imu'].append(row[9])
            # sessionDict['force'].append(row[10])
            sessionDict['meas'].append(row[11])
            # sessionDict['play_id'].append(row[12])
            # sessionDict['session_id'].append(int(row[13]))

        i+=1

#Check length of dictionaries if they match and print number of anchors
print("Number of anchors:", len(anchors))
print(anchors)
if len(sessionDict['tag_id'])==len(sessionDict['timestamp']) and len(sessionDict['tag_id'])==len(sessionDict['x']) and len(sessionDict['tag_id'])==len(sessionDict['y']) and len(sessionDict['tag_id'])==len(sessionDict['z']) and len(sessionDict['tag_id'])==len(sessionDict['imu']) and len(sessionDict['tag_id'])==len(sessionDict['meas']):
    print('All data is imported correct. Length of packets:', len(sessionDict['tag_id']))


######### Start plotting stuff #########
    
#Plot RSSI, RSSI2 heatmaps for all anchors in anchor list
#Create rssi dictionaries for all the anchors
RSSI = {}
RSSI2 = {}
measX = {}
measY = {}
IMUmap = {}
noIMUmap = {}
for anchor in anchors:
    RSSI[anchor] = np.array([])
    RSSI2[anchor] = np.array([])
    measX[anchor] = np.array([])
    measY[anchor] = np.array([])
    IMUmap[anchor] = []
    noIMUmap[anchor] = []

#Create the X, Y coordinates map
x, y = np.array([]), np.array([])
#Create lists for registering discrete measurements, by appending the coordinates as many times as the number of anchors in meas
xDiscrete, yDiscrete = np.array([]), np.array([])

#Packet iteration for measurements
for i in range(len(sessionDict['meas'])):
    x = np.append(x, sessionDict['x'][i])
    y = np.append(y, sessionDict['y'][i])
    #check if json receives null value
    if sessionDict['meas'][i] != 'null':
        data = json.loads(sessionDict['meas'][i])
    else:
        data = json.loads("{}")
    #iter through measurements in the packet
    tempAnchorList = []
    for item in data:
        xDiscrete = np.append(xDiscrete, float(sessionDict['x'][i]))
        yDiscrete = np.append(yDiscrete, float(sessionDict['y'][i]))
        RSSI[item['anchor']] = np.append(RSSI[item['anchor']], float(item['rssi']))
        RSSI2[item['anchor']] = np.append(RSSI2[item['anchor']], float(item['rssi2']))
        measX[item['anchor']] = np.append(measX[item['anchor']], float(sessionDict['x'][i]))
        measY[item['anchor']] = np.append(measY[item['anchor']], float(sessionDict['y'][i]))
        tempAnchorList.append(item['anchor'])

    #Check if all anchors were included otherwise set nil value for absent ones
    for anchor in anchors:
        #Check also if imu_raw was registered, otherwise append coordinates for plotting IMU/noIMU map
        if sessionDict['imu_raw'][i] == 'null':
            noIMUmap[anchor].append([float(sessionDict['x'][i]), float(sessionDict['y'][i])])
        else:
            IMUmap[anchor].append([float(sessionDict['x'][i]), float(sessionDict['y'][i])])
        if anchor in tempAnchorList:
            continue
        else:
            #Assing value 0 on RSSI and RSSI2 for no measurements
            RSSI[anchor] = np.append(RSSI[anchor], float(0))
            RSSI2[anchor] = np.append(RSSI2[anchor], float(0))
            #Assign big value on x and y measurements for no measurements
            measX[anchor] = np.append(measX[anchor], float(1000))
            measY[anchor] = np.append(measY[anchor], float(1000))

#Create plotter folder
path = "plotter_"+sessionDict['tag_id'][0]
try:
    os.mkdir(path)
except:
    pass

#Plot MEAS-2D Frequency Histogram for all anchors(at least one anchor measurement)===========
plot_field()
plt.hist2d(x, y, bins=[np.arange(-72,67,2),np.arange(-10,87,2)], vmax=30, cmap='YlGnBu')
plt.colorbar().set_label('# of measurements', rotation=270)
#Legends
plt.title("Measurements received for TAG ["+sessionDict['tag_id'][0]+"] from\nAll Anchors(at least one Anc Meas).")
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plot_anchors()

# plt.show()
plt.savefig(path+"/FreqMeasAllAnchors_"+sessionDict['tag_id'][0]+".png", dpi=200)


#Plot MEAS-2D Frequency Histogram for all anchors individually(discrete measurements)===========
plot_field()
plt.hist2d(xDiscrete, yDiscrete, bins=[np.arange(-72,67,2),np.arange(-10,87,2)], vmax=200, cmap='YlGnBu')
plt.colorbar().set_label('# of discrete measurements', rotation=270)
#Legends
plt.title("Measurements received for TAG ["+sessionDict['tag_id'][0]+"] from All Anchors\n(discrete Anc Meas). Average of "+str(round(xDiscrete.shape[0]/len(sessionDict['x']), 2))+" anc meas per point.")
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plot_anchors()

# plt.show()
plt.savefig(path+"/FreqMeasDiscAncs_"+sessionDict['tag_id'][0]+".png", dpi=200)


#Plot IMU/No IMU measurements from Master===========
for j in range(len(anchors)):
    plot_field()
    #comvert list to numpy array
    IMU = np.array(IMUmap[anchors[j]])
    noIMU = np.array(noIMUmap[anchors[j]])
    try:
        plt.scatter(IMU[:, 0], IMU[:, 1], s=0.4, label='Points with IMU', alpha=0.8)
        plt.scatter(noIMU[:, 0], noIMU[:, 1], s=0.4, label='Points without IMU', alpha=0.8)
    except:
        pass
    #Legends
    plt.title("Points with IMU measurements from TAG ["+sessionDict['tag_id'][0]+"].\n"+anchors[j]+" only - "+str(round(100*(noIMU.shape[0]/(noIMU.shape[0]+IMU.shape[0])), 2))+"% packet loss.")
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.legend()
    plot_anchors()

    # plt.show()
    plt.savefig(path+"/IMUpoints_"+sessionDict['tag_id'][0]+anchors[j]+".png", dpi=200)


#%% Plot Trajectory from Archimedes===========
plot_field()
plt.plot(x, y, 'r-', linewidth=0.4)
#Legends
plt.title("Arcimedes Trajectory for TAG ["+sessionDict['tag_id'][0]+"].")
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plot_anchors()

# plt.show()
plt.savefig(path+"/Trajectory_"+sessionDict['tag_id'][0]+".png", dpi=200)


###################################################
#%% ######Generating individual anchor heatmaps####
###################################################
for anchor in anchors:
    try:
        os.mkdir(path+"/"+anchor)
    except:
        continue

    #RSSI plots===========
    try:
        plot_field()
        #Calculate nil/no nil measurements
        zero = []
        noZero = []
        counter = 0
        for val in RSSI[anchor]:
            if val > -70:
                zero.append(counter)
            else:
                noZero.append(counter)
            counter+=1
        #Remove ~last 2 seconds
        zero = zero[:-40]
        noZero = noZero[:-40]

        #Plot the rssi map
        plt.scatter(x[noZero], y[noZero], c=RSSI[anchor][noZero], s=10, vmin=-95, vmax=-77, marker=",", alpha=0.3)
        plt.colorbar().set_label('dB', rotation=270)

        X, Y = np.array(x[zero]), np.array(y[zero])
        plt.plot(X, Y, 'r,')

        #Legends
        plt.title("RSSI plot for TAG ["+sessionDict['tag_id'][0]+"] from ANCHOR {"+anchor+"}. Red dots\nrepresent points with no measurement. Meas loss: "+str(round(100*(X.shape[0]/len(sessionDict['x'])), 2))+"%")
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plot_anchors()

        # plt.show()
        plt.savefig(path+"/"+anchor+"/rssi"+anchor+".png", dpi=200)
    except:
        pass


    #RSSI2 plots===========
    try:
        plot_field()
        #Calculate nil/no nil measurements
        zero = []
        noZero = []
        counter = 0
        for val in RSSI2[anchor]:
            if val > -70:
                zero.append(counter)
            else:
                noZero.append(counter)
            counter+=1
        #Remove last 3 values
        zero = zero[:-3]
        noZero = noZero[:-3]

        #Plot the rssi2 map
        plt.scatter(x[noZero], y[noZero], c=RSSI2[anchor][noZero], s=10, vmin=-95, vmax=-77, marker=",", alpha=0.3)
        plt.colorbar().set_label('dB', rotation=270)

        X, Y = np.array(x[zero]), np.array(y[zero])
        plt.plot(X, Y, 'r,')

        #Legends
        plt.title("RSSI2 plot for TAG ["+sessionDict['tag_id'][0]+"] from ANCHOR {"+anchor+"}. Red dots\nrepresent points with no measurement. Meas loss: "+str(round(100*(X.shape[0]/len(sessionDict['x'])), 2))+"%")
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plot_anchors()

        # plt.show()
        plt.savefig(path+"/"+anchor+"/rssi2"+anchor+".png", dpi=200)
    except:
        pass

    
    #Plot MEAS logging from master===========
    try:
        plot_field()
        #Calculate nil/no nil measurements
        zero = []
        noZero = []
        counter = 0
        for val in measX[anchor]:
            if val > 999:
                zero.append(counter)
            else:
                noZero.append(counter)
            counter+=1
        #Remove last 3 values
        zero = zero[:-3]
        noZero = noZero[:-3]

        #Plot points with measurements reported
        plt.hist2d(x[noZero], y[noZero], bins=[np.arange(-72,67,2),np.arange(-10,87,2)], vmax=20, cmap='YlGnBu')
        plt.colorbar().set_label('# of measurements from anchor', rotation=270)

        X, Y = np.array(x[zero]), np.array(y[zero])
        plt.plot(X, Y, 'r,')

        #Legends
        plt.title("Measurements received for TAG ["+sessionDict['tag_id'][0]+"] from ANCHOR {"+anchor+"}. Red dots\nrepresent points with no measurement. Meas loss: "+str(round(100*(X.shape[0]/len(sessionDict['x'])), 2))+"%")
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plot_anchors()

        # plt.show()
        plt.savefig(path+"/"+anchor+"/measFrom"+anchor+".png", dpi=200)
    except:
        pass
