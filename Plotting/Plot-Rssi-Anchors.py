# -*- coding: utf-8 -*-
"""
Created on Thu July 5 11:05:07 2018

@author: Nicholas Sotiriou - github: @nsotiriou88
"""

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import json

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

db = sqlite3.connect('Ealing-050718_Converted.sqlite')
cursor = db.cursor()

cursor.execute("SELECT * FROM firstCapture_12_25_withTime") #Add Table name here
firstExp = cursor.fetchall()


MasterTable = []
Table799 = []
for packet in firstExp:
    if packet[1] == '0x78C':
        MasterTable.append(packet)
    if packet[1] == '0x799':
        Table799.append(packet)

# Master's Packets
xM = []
yM1 = []
yM2 = []
i = 0
for packet in MasterTable:
    if '0x799' in packet[2]:
        data = json.loads(packet[2])
        for anchor in data:
            if anchor['anchor'] == '0x799':
                xM.append(i)
                i += 1
                yM1.append(anchor['rssi'])
                yM2.append(anchor['rssi2'])

# Packets from the Anchor
xA = []
yA1 = []
yA2 = []
j = 0
for packet in Table799:
    if '0x78C' in packet[2]:
        data = json.loads(packet[2])
        for anchor in data:
            if anchor['anchor'] == '0x78C':
                xA.append(j)
                j += 1
                yA1.append(anchor['rssi'])
                yA2.append(anchor['rssi2'])

#Convert lists to numpy arrays
xMn = np.asarray(xM)
yM1n = np.asarray(yM1)
yM2n = np.asarray(yM2)
xAn = np.asarray(xA)
yA1n = np.asarray(yA1)
yA2n = np.asarray(yA2)

# Plot Master to 799 rssi
plt.subplot(221)
plt.plot(xMn, yM1n, 'ro')
plt.title('Master to 0x799 rssi1')
plt.xlabel('samples over time')
plt.ylabel('rss1')
plt.grid(True)

# Plot Master to 799 rssi2
plt.subplot(222)
plt.plot(xMn, yM2n, 'bo')
plt.title('Master to 0x799 rssi2')
plt.xlabel('samples over time')
plt.ylabel('rss2')
plt.grid(True)

# Plot 799 to Master rssi
plt.subplot(223)
plt.plot(xAn, yA1n, 'ro')
plt.title('0x799 to Master rssi1')
plt.xlabel('samples over time')
plt.ylabel('rss1')
plt.grid(True)

# Plot 799 to Master rssi2
plt.subplot(224)
plt.plot(xAn, yA2n, 'bo')
plt.title('0x799 to Master rssi2')
plt.xlabel('samples over time')
plt.ylabel('rss2')
plt.grid(True)


plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()


db.close()
# print(yM2[0])#DEBUG
