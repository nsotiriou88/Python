# anchorFunc
"""This function determines the tag position matrix"""

import numpy as np
import sys
import itertools as itt
import math
import copy
import matplotlib.pyplot as plt

def coordinateFunc(ancMat, anc2DPos, tagMat, tagPos, actualPositions):


    # Determine number of anchors
    ancNum, _ = ancMat.shape
    
    # Define temporary tag position matrix
    tempTagPos = np.array([[0.00, 0.00],[0.00, 0.00],[0.00, 0.00]])

    # Create all 3 anchor combinations
    ancList = list(range(0,ancNum))
    ancIts = [x for x in itt.combinations(ancList, 3) ]
    lenIts = len(ancIts)


    # Initialize arVec which contains aspect ratios (figures of merit) for equilaterial triangles
    arVec = np.zeros((lenIts, 1))


    # Loop over the ancIts list and find the most equilateral triangle
    for j in range(0,lenIts):
        triIts = [x for x in itt.combinations(ancIts[j], 2) ]

        d1 = ancMat[triIts[0][0], triIts[0][1]]
        d2 = ancMat[triIts[1][0], triIts[1][1]]
        d3 = ancMat[triIts[2][0], triIts[2][1]]

        s = 0.5*(d1 + d2 + d3)
        arVec[j,0] = (d1*d2*d3)/(4*(s-d1)*(s-d2)*(s-d3))
    

    # Now we choose the most equilateral triangle
    sortArgs = np.argsort(np.absolute(arVec),0)
    
    # And we also create vectors of its cyclic permutations
    refTri1 = list(ancIts[sortArgs[0][0]])
    refTri2 = [refTri1[1],refTri1[2],refTri1[0]]
    refTri3 = [refTri1[2],refTri1[0],refTri1[1]]


    # Now we will declare that the first point in refTri1 is the origin
    # We will then declare that the second point lies on the x-axis
    anc2DPos[refTri1[1],:] = np.array([ancMat[refTri1[0]][refTri1[1]],0])
    


    # Now we determine the third point relative to the other 
    d1 = ancMat[refTri1[0]][refTri1[1]]
    d2 = ancMat[refTri1[1]][refTri1[2]]
    d3 = ancMat[refTri1[2]][refTri1[0]]


    # Now calculate the angles in the triangle
    cosTheta1 = (d1**2 + d3**2 - d2**2 )/(2*d1*d3)
    theta1 = math.acos(cosTheta1)
    

    # Using trig we find the third anchor
    anc2DPos[refTri1[2],:] = np.array([d3*cosTheta1,d3*np.sin(theta1)])
    

    # We have now found 3 anchors
    ancsFound = 3
    ancsFoundList = list(refTri1)
       
    
    # Using these cyclic permutations we can define a coordinate transformation matrix
    x2 = anc2DPos[refTri2[1], :] - anc2DPos[refTri2[0], :]
    x2 = x2/np.linalg.norm(x2)
    y2 = np.array([-x2[1],x2[0]])

    R2 = np.zeros((2,2))
    R2[:,0] = x2
    R2[:,1] = y2
    

    # And we define one more coordinate transformation
    x3 = anc2DPos[refTri3[1], :] - anc2DPos[refTri3[0], :]
    x3 = x3/np.linalg.norm(x3)
    y3 = np.array([-x3[1],x3[0]])

    R3 = np.zeros((2,2))
    R3[:,0] = x3
    R3[:,1] = y3
    #R3 = np.transpose(R3)


    # We still have to find these anchors
    pointsToFind = [x for x in ancList if x not in refTri1]


    # Now we loop over the remaining points
    # Remember d1 = distance from anchor[0] to anchor[1]
    for j in pointsToFind:

        # Calculate the coordinates using all three orientations 
        # or "view points". We do this because if a point is colinear with the x-axis
        # then the triangle is degenerate and we 
        d01 = ancMat[refTri1[0]][refTri1[1]]
        d0p = ancMat[refTri1[0]][j]
        d1p = ancMat[refTri1[1]][j]
        res1 = anc2DPos[refTri1[2],:]
        xp1 = ((d01**2 +d0p**2 - d1p**2)/(2*d01))
        ypm1 = np.array([np.sqrt(d0p**2 - xp1**2),-np.sqrt(d0p**2 - xp1**2)])

        d01 = ancMat[refTri2[0]][refTri2[1]]
        d0p = ancMat[refTri2[0]][j]
        d1p = ancMat[refTri2[1]][j]
        res2 = anc2DPos[refTri2[2],:]
        xp2 = ((d01**2 +d0p**2 - d1p**2)/(2*d01))
        ypm2 = np.array([np.sqrt(d0p**2 - xp2**2),-np.sqrt(d0p**2 - xp2**2)])

        d01 = ancMat[refTri3[0]][refTri3[1]]
        d0p = ancMat[refTri3[0]][j]
        d1p = ancMat[refTri3[1]][j]
        res3 = anc2DPos[refTri3[2],:]
        xp3 = ((d01**2 +d0p**2 - d1p**2)/(2*d01))
        ypm3 = np.array([np.sqrt(d0p**2 - xp3**2),-np.sqrt(d0p**2 - xp3**2)])

        
        
        # Transform the other values back into the original frame
        # We must transport the [xp2,ypm2] and [xp3,ypm3] points to the new origin
        xy1 = np.array(([xp1,xp1],[ypm1[0],ypm1[1]]))
        xy2 = np.dot(R2,np.array(([xp2,xp2],[ypm2[0],ypm2[1]]))) + np.array(([anc2DPos[refTri2[0]][0],anc2DPos[refTri2[0]][0]],[anc2DPos[refTri2[0]][1],anc2DPos[refTri2[0]][1]]))
        xy3 = np.dot(R3,np.array(([xp3,xp3],[ypm3[0],ypm3[1]]))) + np.array(([anc2DPos[refTri3[0]][0],anc2DPos[refTri3[0]][0]],[anc2DPos[refTri3[0]][1],anc2DPos[refTri3[0]][1]]))                                              


                
        # Now we must use the reflection resolver to make sure we have the correct solution
        distTol = 1
             
        # Check using LCS 1
        trueDist = ancMat[refTri1[2]][j]
        dist1 = np.linalg.norm(anc2DPos[refTri1[2],:] - xy1[:, 0])
        dist2 = np.linalg.norm(anc2DPos[refTri1[2],:] - xy1[:, 1])
        if trueDist - dist1 < distTol:
            soln1 = xy1[:, 0]            
        elif trueDist - dist2 < distTol:
            soln1 = xy1[:, 1]            
        else:
            soln1 = np.nan

        # Check using LCS 2
        trueDist = ancMat[refTri2[2]][j]
        dist1 = np.linalg.norm(anc2DPos[refTri2[2],:] - xy2[:, 0])
        dist2 = np.linalg.norm(anc2DPos[refTri2[2],:] - xy2[:, 1])
        if trueDist - dist1 < distTol:
            soln2 = xy2[:, 0]            
        elif trueDist - dist2 < distTol:
            soln2 = xy2[:, 1]            
        else:
            soln2 = np.nan     

                
        # Check using LCS 3
        trueDist = ancMat[refTri3[2]][j]
        dist1 = np.linalg.norm(anc2DPos[refTri3[2],:] - xy3[:, 0])
        dist2 = np.linalg.norm(anc2DPos[refTri3[2],:] - xy3[:, 1])
        if trueDist - dist1 < distTol:
            soln3 = xy3[:, 0]            
        elif trueDist - dist2 < distTol:
            soln3 = xy3[:, 1]            
        else:
            soln3 = np.nan         
        
        ###########################################################
        # BIG ASSUMPTION HERE: NEED TO ADD ROBUSTNESS
        ###########################################################
        # For now let's enter soln 1 into the anc2DPos matrix
        anc2DPos[j, :] = soln3

    ###############################################################
    # NOW LOCATE THE TAGS ON THE FIELD
    ###############################################################

    # Now we locate the tags and use their positions to fix the coordinate SystemError
        
    for j in range(0,3):

        # Calculate the coordinates using all three orientations 
        # or "view points". We do this because if a point is colinear with the x-axis
        # then the triangle is degenerate and we 
        d01 = ancMat[refTri1[0]][refTri1[1]]
        d0p = tagMat[j][refTri1[0]]
        d1p = tagMat[j][refTri1[1]]        
        xp1 = ((d01**2 +d0p**2 - d1p**2)/(2*d01))
        ypm1 = np.array([np.sqrt(d0p**2 - xp1**2),-np.sqrt(d0p**2 - xp1**2)])

        d01 = ancMat[refTri2[0]][refTri2[1]]
        d0p = tagMat[j][refTri2[0]]
        d1p = tagMat[j][refTri2[1]]                        
        xp2 = ((d01**2 +d0p**2 - d1p**2)/(2*d01))
        ypm2 = np.array([np.sqrt(d0p**2 - xp2**2),-np.sqrt(d0p**2 - xp2**2)])        

        d01 = ancMat[refTri3[0]][refTri3[1]]
        d0p = tagMat[j][refTri3[0]]
        d1p = tagMat[j][refTri3[1]]        
        xp3 = ((d01**2 +d0p**2 - d1p**2)/(2*d01))
        ypm3 = np.array([np.sqrt(d0p**2 - xp3**2),-np.sqrt(d0p**2 - xp3**2)])
                
        # Transform the other values back into the original frame
        # We must transport the [xp2,ypm2] and [xp3,ypm3] points to the new origin
        xy1 = np.array(([xp1,xp1],[ypm1[0],ypm1[1]]))
        xy2 = np.dot(R2,np.array(([xp2,xp2],[ypm2[0],ypm2[1]]))) + np.array(([anc2DPos[refTri2[0]][0],anc2DPos[refTri2[0]][0]],[anc2DPos[refTri2[0]][1],anc2DPos[refTri2[0]][1]]))
        xy3 = np.dot(R3,np.array(([xp3,xp3],[ypm3[0],ypm3[1]]))) + np.array(([anc2DPos[refTri3[0]][0],anc2DPos[refTri3[0]][0]],[anc2DPos[refTri3[0]][1],anc2DPos[refTri3[0]][1]]))                                              
                
        # Now we must use the reflection resolver to make sure we have the correct solution
        distTol = 1
             
        # Check using LCS 1
        trueDist = tagMat[j][refTri1[2]]        
        dist1 = np.linalg.norm(anc2DPos[refTri1[2],:] - xy1[:, 0])
        dist2 = np.linalg.norm(anc2DPos[refTri1[2],:] - xy1[:, 1])
        if trueDist - dist1 < distTol:
            soln1 = xy1[:, 0]            
        elif trueDist - dist2 < distTol:
            soln1 = xy1[:, 1]            
        else:
            soln1 = np.nan

        # Check using LCS 2        
        trueDist = tagMat[j][refTri2[2]]
        dist1 = np.linalg.norm(anc2DPos[refTri2[2],:] - xy2[:, 0])
        dist2 = np.linalg.norm(anc2DPos[refTri2[2],:] - xy2[:, 1])
        if trueDist - dist1 < distTol:
            soln2 = xy2[:, 0]            
        elif trueDist - dist2 < distTol:
            soln2 = xy2[:, 1]            
        else:
            soln2 = np.nan     

                
        # Check using LCS 3        
        trueDist = tagMat[j][refTri3[2]]
        dist1 = np.linalg.norm(anc2DPos[refTri3[2],:] - xy3[:, 0])
        dist2 = np.linalg.norm(anc2DPos[refTri3[2],:] - xy3[:, 1])
        if trueDist - dist1 < distTol:
            soln3 = xy3[:, 0]            
        elif trueDist - dist2 < distTol:
            soln3 = xy3[:, 1]            
        else:
            soln3 = np.nan         
                
        ###########################################################
        # BIG ASSUMPTION HERE: NEED TO ADD ROBUSTNESS
        ###########################################################
        # For now let's enter soln 1 into the tempTagPos matrix
        tempTagPos[j, :] = soln1



    plt.subplot(1, 2, 1)
    plt.scatter(actualPositions[:, 0], actualPositions[:, 1], color='red')
    plt.scatter(tagPos[0, 0], tagPos[0, 1], color='black', marker = 'o')
    plt.scatter(tagPos[1, 0], tagPos[1, 1], color='black', marker = 'x')
    plt.scatter(tagPos[2, 0], tagPos[2, 1], color='black', marker = '1')
    plt.title('Actual Position')
    plt.axis('equal')
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.scatter(anc2DPos[:, 0], anc2DPos[:, 1], color='blue')
    plt.scatter(tempTagPos[0, 0], tempTagPos[0, 1], color='black', marker = 'o')
    plt.scatter(tempTagPos[1, 0], tempTagPos[1, 1], color='black', marker = 'x')
    plt.scatter(tempTagPos[2, 0], tempTagPos[2, 1], color='black', marker = '1')
    plt.title('Calculated Position')
    plt.axis('equal')
    plt.grid()

    plt.show()
    sys.exit()



    # Now reorient the coordinate system to reflect the tag positions
    translateVec = copy.deepcopy(tempTagPos[0, :])
    
    # Translate
    for j in range(0,ancNum):
        anc2DPos[j, :] = anc2DPos[j, :] - translateVec
    for j in range(0,3):                                        
        tempTagPos[j, :] = tempTagPos[j, :] - translateVec
        


    # Rotate
    theta = np.arctan2(tempTagPos[1,1],tempTagPos[1,0])
    rotateMat = np.transpose(np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]]))

    anc2DPos = np.transpose(np.dot(rotateMat, np.transpose(anc2DPos)))
    tempTagPos = np.transpose(np.dot(rotateMat, np.transpose(tempTagPos)))
    
    # Flip the coordinate system
    # The tags were ordered around the field in a right-hand configuration
    # So the z component of the cross product is positive
    # Now we check if this is the case and flip if appropriate
    V1 = np.append(tempTagPos[1, :] - tempTagPos[0, :], [0.00])
    V2 = np.append(tempTagPos[2, :] - tempTagPos[1, :], [0.00])
    V3 = np.cross(V1,V2)

    # if V3[2] is negative then we must flip across the x-axis
    if V3[2]<0.00:
        anc2DPos[:,1] = -anc2DPos[:,1]
        tempTagPos[:,1] = -tempTagPos[:,1]

    return anc2DPos
