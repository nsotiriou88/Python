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
imuSet1 = '{"command":"sensOut","id":"'
imuSet2 = '","mode":"agm"}'



    
        



def tagFunc(tagNames, ancNum, TCP_IP, TCP_PORT, UDP_IP, UDP_PORT):

    # ENTER FILENAME HERE
    with open("test.txt", 'w', buffering=20*(1024**2)) as myfile:

        counter = 0

        # Receive data from the UDP stream     
        udpSock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        udpSock.bind((UDP_IP, UDP_PORT))

        #Receive data from the UDP stream
        while 1:
            data, addr = udpSock.recvfrom(4096) # buffer size is 1600 bytes 
            newVar = data.splitlines()
            #data = data.decode("utf-8").split()[0]        
            #doc = json.loads(data)        
            
            for x in range(0, len(newVar)):            
                data = newVar[x-1].decode("utf-8")
                #print(json.loads(data))
                myfile.write(data + '\n')
                
                print('Saving message ' + str(counter) + '\n')
                counter +=1




    return tagNames



