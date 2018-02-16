import json
import numpy as np

#########
# bSlope = np.asarray([0.72, 0.69, 0.83, 0.52, 0.51, 0.69])
bSlope = [0.72, 0.69, 0.83, 0.52, 0.51, 0.69]
aIntercept = [-32.17, -29.18, -37.66, -26.91, -26.06, -37.48]
linOffset = [-4.13, -1.77, -4.96, -10.77, -9.21, -13.45]
# linOffset = - linOffset * bSlope

data = {}
# data["slope_b"]=[]
# data["slope_b"].append(bSlope)
# data["intercept_a"]=[]
# data["intercept_a"].append(aIntercept)
# data["Linear_Offset"]=[]
# data["Linear_Offset"].append(linOffset)
data["bSlope"]=bSlope
data["aIntercept"]=aIntercept
data["linOffset"]=linOffset

# print(data)

with open('padCal_Config.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

with open('padCal_Config.json', 'r') as infile:
    a=json.load(infile)
    # for key in a:
    #     print(a[key])
    bk=a["slope_b"]

print(bk, "\n", type(bk))
