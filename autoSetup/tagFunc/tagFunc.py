# tagFunc
"""This function determines the tag position matrix"""

import socket
import numpy as np
import sys
import re
import json
import time
from json import JSONDecoder


########################################################################################
def find(s, ch):
    """This function returns all instances of the substring in a given input string"""
    return [i for i, ltr in enumerate(s) if ltr == ch]
########################################################################################


# OpenRTLS API commands
listTags = '{\"command\":\"listTags\"}'


def tagFunc(buffSize, tagMat, tagNames, ancNames, ancNum, TCP_IP, TCP_PORT, UDP_IP, UDP_PORT):


    # Define and initialize a tag counter
    tagNum = 0

    # Open the socket and request a tag list
    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.connect((TCP_IP, TCP_PORT))
    tcpSock.send(listTags.encode())
    print('\nRequesting tag list from master')
    time.sleep(0.5)
    data = tcpSock.recv(1024).decode("utf-8")


    # Now pull out the tag names
    doc = json.loads(data)    
    for tag in doc['tags']:

        # Current tag name
        tagNames.append(tag['id'])
        tagNum += 1


    # Tell the user which tags have been found
    print('\nThe following tags were found')
    print('\n')
    print(tagNames)
    

    # Check if there's more than one tag and ask which to use 
    if tagNum != 1:
        useTag = input('\nPlease enter the tag ID which you want to use to define the field: ')
        
        # Check if useTag is in the list of tags
        while useTag not in tagNames:
            print('\nYou have entered a tag not in the list\n')
            useTag = input('\nPlease enter the tag ID which you want to use to define the field: ')
        print('\nWe will now take three measurements using tag ',useTag)
    elif tagNum == 1:
        useTag = tagNames[0]

    # Gracefully close the TCP socket
    tcpSock.close()

    # Receive data from the UDP stream     
    udpSock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
    udpSock.bind((UDP_IP, UDP_PORT))


    # Now get the tag measurements by opening a UDP socket
    j = 0
    while j <=2:

        circBuff = np.zeros((ancNum, buffSize, 3))
        counter = 0
        anchorCnt = np.zeros(ancNum)
        anchorCnt2 = 0
        

        if j == 0:
            input("\nPress Enter to continue to take the first measurement...")
        elif j == 1:
            input("\nPress Enter to continue to take the second measurement...")
        elif j == 2:
            input("\nPress Enter to continue to take the third measurement...")

        # Initialize a useful counter which will count the number of outstanding measurements
        waitingFor = buffSize

        while any (circBuff[:, buffSize-1, j] == 0):
        
            #Receive data from the UDP stream
            data, addr = udpSock.recvfrom(4096) # buffer size is 1600 bytes 
            
            try:
                data = data.decode("utf-8").split()[0]        
            except:
                print(data)
                sys.exit()
            
            doc = json.loads(data)


            # Check if we have Tag-Anchor Communications
            if ('mode' not in doc) and (doc['id'] == useTag):
                for meas in doc['meas']:
                    if 'dist' in meas:
                        
                        # This is the current anchor
                        currentAnc = meas['anchor']
                        anchorPos = ancNames.index(currentAnc)
                        circBuffPos = int(np.mod(anchorCnt[anchorPos], buffSize))
                        circBuff[anchorPos, circBuffPos, j] = meas['dist']
                        anchorCnt[anchorPos] += 1
                waitingFor = np.max(np.count_nonzero(circBuff[anchorPos, circBuffPos, j], axis=0))
            print('\nWaiting for ' + str(waitingFor) + ' additional measurements')
            print(circBuff[:, :, j])
            print('\n')
        print('\nMeasurements have been recorded')    
        tagMat[j, :] = np.mean(circBuff[:, :, j].T, axis=0)
        print('\n')
        print(tagMat)

        throwAway = input("\nTHROW AWAY DATA? Y/N").lower()
        if throwAway == 'n':
            j+=1

            

        

    return tagMat, tagNames, tagNum
