# calFunc
"""This function determines the inter-anchor position matrix"""

import socket
import numpy as np
import sys
#import re
import json
import time
from json import JSONDecoder
import matplotlib.pyplot as plt


# OpenRTLS API commands

getUwbAntConfig = '{\"command\":\"getUwbAntConfig\",\"id\":\"'


def calFunc(buffSize, ancNum, ancMat, ancNames, TCP_IP, TCP_PORT):

    ###########################################################################
    # Get the current delay values

    currentDelays = np.zeros((1, ancNum))

    # Open a TCP socket and request master to list Anchors
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.connect((TCP_IP, TCP_PORT))
    
    for k in range(ancNum):
        
        commandString = getUwbAntConfig + ancNames[k] + '\"}'
        tcpSock.send(commandString.encode())        
        time.sleep(1)
        data = tcpSock.recv(1024).decode("utf-8").split("\n")
        
        # Check if we caught the "status":"ok" response
        if 'ok' in data[0]:            
            doc = json.loads(data[0])            
            currentDelays[0, k] = doc['rxDelay']
    
        elif 'ok' in data[1]:            
            doc = json.loads(data[1])
            currentDelays[0, k] = doc['rxDelay']
    
        else:
            print(data)
            sys.exit('MASSI ERROR BROTTHHHHEEERRRR')

    print(currentDelays)
    
    ###########################################################################
    # Now calculate the least squares corrections based on the anchor order in 
    # the name vector ancNames

    c = 299792458
    clickTime = 157e-12
    counter =0

    delayMat = np.zeros((ancNum*(ancNum-1),2*ancNum-1))
    measVec =  np.zeros((ancNum*(ancNum-1),1))

        
    for j in range(ancNum):
        for i  in range(ancNum):
            if i==j:
                continue            
            # Enter the true distance expressions
            if (i==0) or (j==0):                
                delayMat[counter, ancNum -1 + max(i,j)] = 1
            elif i>j:
                delayMat[counter, ancNum -1 + i] = 1
                delayMat[counter, ancNum -1 + j] = -1
            elif i<j:
                delayMat[counter, ancNum -1 + i] = -1
                delayMat[counter, ancNum -1 + j] = 1
            
            # Enter the correction terms
            delayMat[counter, j] = 1

            # Enter the measured distances
            measVec[counter] = ancMat[j, i]

            counter +=1

    print(delayMat)
    print('\n')
    print(measVec)
    sys.exit()
    return

