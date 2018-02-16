# Least square fitting

import numpy as np
from scipy import stats


Fi = np.array([[20.0, 40.0, 60.0, 80.0, 100.0, 120], [20.0, 40.0, 60.0, 80.0, 100.0, 120],
               [20.0, 40.0, 60.0, 80.0, 100.0, 120], [20.0, 40.0, 60.0, 80.0, 100.0, 120],
               [20.0, 40.0, 60.0, 80.0, 100.0, 120]])
xdata = np.array([20.0, 40.0, 60.0, 80.0, 100.0])
# ydata = Fi
slope = np.zeros((6), dtype=np.float)
inter = np.zeros((6), dtype=np.float)
R2 = np.zeros((6), dtype=np.float)
# p_value = np.zeros((6), dtype=np.float)
# std_err = np.zeros((6), dtype=np.float)

Fi = np.random.rand(5, 6)
sensor = {1: "Right 1 Sensor (Bottom)",
          2: "Right 2 Sensor (Middle)",
          3: "Right 3 Sensor (Top)",
          4: "Left 3 Sensor (Top)",
          5: "Left 2 Sensor (Middle)",
          6: "Left 1 Sensor (Bottom)"}


for i in range(0, 6):
    slope[i], inter[i], R2[i], p_value, std_err = stats.linregress(xdata, Fi[:, i])
    print("Set of data for sensor", sensor[i+1])
    print()
    print('The slope is:', slope[i])
    print('The intercept is:', inter[i])
    print('The R2 is:', R2[i]**2)
    print(50*'-')



# Need to ask about the weights for creating the x values of the array.
# Maybe at serial process
