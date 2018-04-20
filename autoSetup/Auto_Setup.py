#!/usr/bin/python3
# Auto-Setup2D
"""
This function allows a 2D anchor setup to be created by using tag measurements from 
three reasonably well-known places to be used to fix the coordinate system
"""

# Import useful functions
import socket
import json
import time
import re
import numpy as np
from json import JSONDecoder
from functools import partial
import sys, os
import matplotlib.pyplot as plt
import signal
from subprocess import Popen, PIPE

# Import outside functions
from anchorFunc import anchorFunc
from calFunc import calFunc
from tagFunc import tagFunc
from coordinateFunc2 import coordinateFunc2
from qrLocate import qrLocate
from writeAnchorList import writeAnchorList

# Import the config settings
import config




# Determine the inter-anchor position matrix 
if config.debugData.lower() != 'yes':
    ancMat, ancNames, masterId = anchorFunc.anchorFunc(config.buffSize, config.ancNum, config.ancMat, config.ancMatBuff, config.ancNames, config.TCP_IP, config.TCP_PORT, config.plotAnchorHealth)
else:
    ancMat = config.ancMat
    ancNames = config.ancNames
    masterId = config.masterId
print(ancNames)




# Perform anchor calibration based on the measurements in ancMat
if config.calibrateAncs.lower() == 'no':
    calFunc.calFunc(config.buffSize, config.ancNum, ancMat, ancNames, config.TCP_IP, config.TCP_PORT)




# Determine the number of tags present and get the tag distance matrix
"""
I can make this function better if I allow it to not necessarily get 100 measurements from each anchor, but say
more than or equal to 5... And then in coordinateFunc I just chose the five anchors which have measurements to UserWarning
the qrLocate algorithm
"""
if config.debugData.lower == 'no':
    tagMat, tagNames, tagNum = tagFunc.tagFunc(config.buffSize, config.tagMat, config.tagNames, ancNames, config.ancNum, config.TCP_IP, config.TCP_PORT, config.UDP_IP, config.UDP_PORT)
else:
    tagMat = config.tagMat
    tagNames = config.tagNames




# Determine the 2D coordinate system
anc2DPos = coordinateFunc2.coordinateFunc2(ancMat, config.anc2DPos, tagMat, config.tagPos, config.actualPositions)


sys.exit()


# Write the anchorList.json here
writeAnchorList.writeAnchorList(anc2DPos, ancNames, config.ancNum, masterId)




# Run ASE shell-script
#aseLocation = '~/Dropbox/Miscellaneous/Sportable\ Technologies/Sportable\ 2017/Algorithms_Old_Code//Python/Auto_Setup_2D/ASE/rtls-engine -1 -e7 -a1 -s -f 127.0.0.1'
#p1 = Popen([aseLocation], stdin=PIPE, shell=True,  preexec_fn=os.setsid)
print('\nSleep 5 seconds before opening the Mangager')
time.sleep(5)




# Now open Manager
managerLocation = '~/Dropbox/Miscellaneous/Sportable\ Technologies/Sportable\ 2017/Algorithms_Old_Code//Python/Auto_Setup_2D/Manager/rtls-manager-linux-64bit'
os.system(managerLocation)




# Gracefully close the ASE
#closeASE = input('Kill THE ASE Y/N: ').lower()
#if closeASE == 'y':
#    os.killpg(os.getpgid(p1.pid), signal.SIGTERM)
