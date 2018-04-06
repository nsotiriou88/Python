#!/usr/bin/python

import socket
import json
import time
import re
import numpy as np
from json import JSONDecoder
from functools import partial
import sys

# Import outside functions
from tagFunc import tagFunc



UDP_IP = ""
UDP_PORT = 8787
TCP_IP = '192.168.1.129'
TCP_PORT = 8784


# QUATERNION
{"command":"sensOut","id":"0xDECA363034300B5D","mode":"quat"}

# YAW PITCH ROLL
{"command":"sensOut","id":"0xDECA363034300B5D","mode":"ypr"}

# RAW IMU DATA
{"command":"sensOut","id":"0xDECA363034300B5D","mode":"agm"}

# NO IMU (DEFAULT)
{"command":"sensOut","id":"0xDECA363034300B5D","mode":"none"}


########################################################################################
# Initialize useful constants, vectors and matrices
########################################################################################
buffSize = 20
ancNum = 1
tagNames = ['0x45B6','0x4636']


########################################################################################
# Determine the number of tags present and get the tag distance matrix
########################################################################################
tagNames, tagNum = tagFunc.tagFunc(tagNames, ancNum, TCP_IP, TCP_PORT, UDP_IP, UDP_PORT)
