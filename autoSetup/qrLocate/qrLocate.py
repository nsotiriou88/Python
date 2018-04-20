# qrLocate
"""This function uses a QR factorization to locate the tag which is implicitly a least square errors search"""

import numpy as np
import sys
import itertools as itt
import math
import copy
import matplotlib.pyplot as plt
import random

def qrLocate(tagMeas, anc2DPos, refTri1, useAncs, ancNum, ancMat):

    
    # This is the anchor that is the linearizer
    linTool = refTri1[0]

    # These are the remaining anchors that are not the linearizer
    remAncs = [x for x in range(0, ancNum) if x != refTri1[0]]

    # Now we randomly sample useAncs from remAncs --> create avAncs = available anchors
    if len(remAncs)>useAncs:
        avAncs = random.sample(remAncs, useAncs)
    else:
        # Set the available anchors and reset the useAncs number
        avAncs = remAncs
        useAncs = len(avAncs)


    # Create [A] and {b}
    A  = np.zeros((useAncs, 2))
    b  = np.zeros((useAncs, 1))
    
    for k in range(0, useAncs):
        A[k, :] = [anc2DPos[avAncs[k], 0] - anc2DPos[linTool, 0], anc2DPos[avAncs[k], 1] - anc2DPos[linTool, 1]]
        b[k] = 0.5*(tagMeas[linTool]**2 - tagMeas[avAncs[k]]**2 + ancMat[linTool, avAncs[k]]**2)

    # Perform QR factorization
    Q, R = np.linalg.qr(A)

    # Perform backward substitution
    qrTagPos = np.zeros((2, 1))
    tempVar = np.dot(np.transpose(Q), b)
    qrTagPos[1] = tempVar[1]/R[1, 1]
    qrTagPos[0] = (tempVar[0] - R[0, 1]*qrTagPos[1])/R[0, 0]

    # NORMALLY WE ADD anc2DPos[linTool, :] TO THE ANSWER qrTagPos
    # BUT IN THIS CASE WE'VE CHOSEN THE LINEARISER WHICH IS ALREADY [0, 0]


    return np.transpose(qrTagPos)
