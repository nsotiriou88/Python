# anchorFunc
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
listAncs = '{\"command\":\"listAnchors\"}'
newSess = '{\"command\":\"newSess\"}'



def anchorFunc(buffSize, ancNum, ancMat, ancMatBuff, ancNames, TCP_IP, TCP_PORT, plotAnchorHealth):

    # Define useful counters etc
    ancCounter = 0


    # Open the socket and request a new session
    #tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #tcpSock.connect((TCP_IP, TCP_PORT))
    #tcpSock.send(newSess.encode())
    #print('MASTER SLEEPING FOR 12 SECONDS\n')
    #time.sleep(12)

    # Open a TCP socket and request master to list Anchors
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.connect((TCP_IP, TCP_PORT))
    tcpSock.send(listAncs.encode())
    print('\nRequesting anchor list from master')
    time.sleep(0.5)    
    data = tcpSock.recv(4096).decode("utf-8")

    # Now pull out the anchor names and get their distances
    print(data)

    doc = json.loads(data)
    print('\nExtracting the anchor names\n')
    for anchor in doc['anchors']:

        # Current anchor name
        ancNames[ancCounter] = anchor['id']
        ancCounter += 1

        if anchor['roles'] == '0x000F0000':
            # Then this is the Master
            masterId = anchor['id']
            

    # NOW WE CHECK: Did ancNum anchors respond?
    if ancCounter != ancNum:
        sys.exit('\n\nNOT ENOUGH ANCHORS RESPONDED\n\n')


    for k in range(buffSize):
        print('Extracting measurement ' + str(k) + '\n')
        for j in range(ancNum):

            currentAnc = ancNames[j]


            # Send message over socket
            msgString = '{\"command\":\"getDist\",\"id\":\"' + currentAnc + '\"}'
            tcpSock.send(msgString.encode())
            time.sleep(0.1)
            data = tcpSock.recv(2048).decode("utf-8")



            # Now fill the distance matrix
            doc = json.loads(data)
            for anchor in doc['distances']:

                # Current anchor name
                ancMeasID = anchor['anchor']

                # Current anchor distance
                ancMeasDist = anchor['dist']

                # Current anchor position in ancNames
                ancInd = [i for i, x in enumerate(ancNames) if x == ancMeasID]

                # Enter data into ancMat
                ancMatBuff[j, ancInd, k] = ancMeasDist

    for m in range(ancNum):
        for n in range(ancNum):
            ancMat[m, n] = np.median(ancMatBuff[m, n, :])


    tcpSock.close()
    
    
    if plotAnchorHealth.lower() == 'yes':
        pltCount = 0
        fig, axs = plt.subplots(ancNum, ancNum, facecolor ='w', edgecolor='k')
        fig.subplots_adjust(hspace = 1, wspace = 1)
        axs = axs.ravel()
        for m in range(ancNum):
            for n in range(ancNum):
                if m==n:
                    pltCount +=1
                    continue
                axs[pltCount].hist(ancMatBuff[m, n, :], bins = 10)
                pltCount +=1
                
        plt.show()        

    print(ancMat)
    print('\n')
    print('Master ID = ' + masterId + '\n')

    return ancMat, ancNames, masterId
