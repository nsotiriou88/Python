# writeAnchorList
"""This function writes anchorList.json"""

import socket
import numpy as np
import sys
import json
import time
from json import JSONDecoder
import matplotlib.pyplot as plt




def writeAnchorList(anc2DPos, ancNames, ancNum, masterId):

    
    print(anc2DPos)
    print('\n')
    print(ancNames)    
    

    ##################################################################
    # Write ASE config
    ##################################################################

    """
    {"response":"listAnchors","status":"ok","anchors":[{"id":"0x0x0117","coordinates": {"x":-44.343,"y":75.137,"z":13.74,"heading":0.000,"pqf":0.000}},{"id":"0x0x0116","coordinates": {"x":-44.368,"y":75.101,"z":9.589,"heading":0.000,"pqf":0.000}},{"id":"0x0x013D","coordinates": {"x":-62.311,"y":64.729,"z":8.749,"heading":0.000,"pqf":0.000}},{"id":"0x0x013C","coordinates": {"x":-62.319,"y":64.805,"z":3.675,"heading":0.000,"pqf":0.000}},{"id":"0x0x0138","coordinates": {"x":-70.748,"y":5.406,"z":9.398,"heading":0.000,"pqf":0.000}},{"id":"0x0x0136","coordinates": {"x":-70.748,"y":5.408,"z":4.384,"heading":0.000,"pqf":0.000}},{"id":"0x0x007E","coordinates": {"x":-45.916,"y":-4.64,"z":14.493,"heading":0.000,"pqf":0.000}},{"id":"0x0x00AE","coordinates": {"x":-45.844,"y":-4.666,"z":10.425,"heading":0.000,"pqf":0.000}},{"id":"0x0x009D","coordinates": {"x":45.691,"y":-4.998,"z":15.56,"heading":0.000,"pqf":0.000}},{"id":"0x0x00B6","coordinates": {"x":45.663,"y":-4.972,"z":11.431,"heading":0.000,"pqf":0.000}},{"id":"0x0x0132","coordinates": {"x":63.277,"y":5.298,"z":10.2,"heading":0.000,"pqf":0.000}},{"id":"0x0x0131","coordinates": {"x":63.267,"y":5.269,"z":5.124,"heading":0.000,"pqf":0.000}},{"id":"0x0x0135","coordinates": {"x":63.582,"y":65.305,"z":9.93,"heading":0.000,"pqf":0.000}},{"id":"0x0x0133","coordinates": {"x":63.445,"y":65.276,"z":4.824,"heading":0.000,"pqf":0.000}},{"id":"0x0x012F","coordinates": {"x":46.834,"y":75.007,"z":15.126,"heading":0.000,"pqf":0.000}},{"id":"0x0x012A","coordinates": {"x":46.903,"y":74.912,"z":11.119,"heading":0.000,"pqf":0.000}}]}
    """



    jsonString = '{"response":"listAnchors","status":"ok","anchors":['
    idString = '{"id":"'
    coordinateString = '","coordinates":{"x":'
    yString = ',"y":'
    zString = ',"z":'
    endString = ',"heading":0.000,"pqf":0.000}},'
    endString2 = ',"heading":0.000,"pqf":0.000}}]}'


    for k in range(0, ancNum-1):
        jsonString = jsonString + idString + ancNames[k] + coordinateString + str(round(anc2DPos[k,0],2))\
        + yString + str(round(anc2DPos[k,1],2)) + zString + str(0.00) + endString
    jsonString = jsonString + idString + ancNames[ancNum-1] + coordinateString + str(round(anc2DPos[ancNum-1,0],2))\
    + yString + str(round(anc2DPos[ancNum-1,1],2)) + zString + str(0.00) + endString2



    # Now write to file
    #jsonAseText = json.loads(jsonString)
    with open("ASE/anchorList.json", "w") as text_file:
        text_file.write(jsonString)
        #text_file.write(json.dumps(jsonAseText, indent=4))
        
    
    
    ##################################################################
    # Write Manager config
    ##################################################################
   
    masterInd = ancNames.index(masterId)
    ancIDs = list(range(0, ancNum))
    ancIDs.remove(masterInd)

    managerString = '{"node":[{"id":"'+ masterId + '","role": "master","coordinates":{"x":' \
                    + str(anc2DPos[masterInd, 0]) + ',"y":' + str(anc2DPos[masterInd, 1]) + ',"z":3.00}},'
    roleString = '","role":"anchor","coordinates":{"x":'
    endString = '"master":{"ip":"auto"},"zone": [{"name": "FIELD","x": -74.63,"y": -12.15,"z": 0.0,"length": 149.26,"width": 94.33,"height": 2.63,"image": "sportable_images/Field.jpg","target": "__self__"}],"gui": {"background-color": "#A1BBCE","grid": {"x-axis-color": "#FFFF00","y-axis-color":"#FFFF00","axis-color": "#666666","step-axis-color": "#FFFF00","step-size": 100},"perspective": true}}'


    for k in ancIDs:
        managerString = managerString + '{"id": "' + ancNames[k] + roleString + str(round(anc2DPos[k, 0],2)) \
        + ',"y":' + str(anc2DPos[k, 1]) + ',"z":3.00}},'
        if k == ancNum-1:
            managerString = managerString + '{"id": "' + ancNames[k] + roleString + str(round(anc2DPos[k, 0],2)) \
        + ',"y":' + str(round(anc2DPos[k, 1])) + ',"z":3.00}}],' + endString
    
    # Now write to file
    jsonManagerText = json.loads(managerString)
    with open("Manager/openrtls.json", "w") as text_file:
        text_file.write(json.dumps(jsonManagerText, indent=4))


    return None
