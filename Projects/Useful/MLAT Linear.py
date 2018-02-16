# MLAT Linearisation

import math
import numpy as np
import matplotlib.pyplot as plt

# Initialisation

anchors = 8
lin = 0    # This is for the reference point (the first of the beams).

# XY = 10*rand(anchors,2)

theta2 = np.linspace(0, 2*math.pi, anchors+1)
XY = 10*np.random.rand(anchors, 2)
T = 10*np.random.rand(1, 2)
D_Mat = np.zeros((anchors, 1))
theta = np.linspace(0, 2*math.pi, 100)


# Determine distances

for i in range(0, anchors):
    D_Mat[i] = math.sqrt(np.power((XY[i, 0]-T[0, 0]), 2)+np.power((XY[i, 1]-T[0, 1]), 2))

# Determine distance from target to lineariser

Dr2 = np.power((T[0, 0]-XY[lin, 0]), 2)+np.power((T[0, 1]-XY[lin, 1]), 2)

# Determine Di2, Dir2

Dir2 = np.zeros((anchors, 1))
Di2 = np.power(D_Mat, 2)


for i in range(1, anchors):
    Dir2[i] = np.power((XY[i, 0]-XY[lin, 0]), 2) + np.power((XY[i, 1]-XY[lin, 1]), 2)


# Setup solution Matrix

Sol_Mat = np.zeros((anchors-1, 2))
Sol_Vec = np.zeros((anchors-1, 1))

for i in range(1, anchors):
    Rowi = [XY[lin, 0]-XY[i, 0], XY[lin, 1]-XY[i, 1]]
    # Filling A matrix (Ax=b)
    Sol_Mat[i-1:] = Rowi
    # Filling B matrix
    Sol_Vec[i-1] = 0.5*(Dr2 + Dir2[i] - Di2[i])

# Solve the system x = (At*A)^-1*At*B

A = Sol_Mat
At = A.transpose()
AtA = np.dot(At, A)
Ai = np.linalg.inv(AtA)
X = np.dot(np.dot(Ai, At), Sol_Vec)
# Target needs to add the reference point. Generally we used
# the first value from XY, as the reference point.
Target = X.transpose()+XY[lin, :]

print('The T is: ', T)
print('The Target is: ', Target, '\n\n')

# Plotting Stuff

for j in range(0,anchors):
    plt.plot(D_Mat[j]*np.cos(theta)+XY[j, 0], D_Mat[j]*np.sin(theta)+XY[j, 1], 'r--')

plt.plot(XY[:, 0], XY[:, 1], 'ro', T[:, 0], T[:, 1], 'b^')

plt.plot(Target[:, 0], Target[:, 1], 'g.')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')


# Testing

# print('\n\n', D_Mat.transpose(), '\n\n', theta)


# Plot showing here, because otherwise the program stops until
# you exit the plot window.
plt.show()
