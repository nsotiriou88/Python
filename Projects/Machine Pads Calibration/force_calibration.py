# This code is used to calibrate individual pads, with the help
# of the calibrated Load Cells (Stephen's Machine). BE AWARE of
# the cerial ports that they need to be assigned via hardcoding
# and the fact that the calibration constants for the Load Cells
# are hard coded too (no need for change). The code is asking to
# export various CSV files with the results. Data from Machine
# comes as (R1,R2,R3,L1,L2,L3). Data from Tags comes as (L1,L2,
# L3,R1,R2,R3).
########################################
# Collecting Force-pad Data from Serial#
########################################

import serial
import numpy as np
from scipy import stats
import sys
import termios
import atexit
from select import select
import json


################################
# Displaying all USB port paths#
################################

# import serial.tools.list_ports
# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p)


#####################################
# INITIALISATION -- ATTENTION NEEDED#
#####################################

# Reading from serial port: TAGS---------------------------------
padPort = serial.Serial('/dev/cu.usbmodem16042201', 115200)
# Reading from serial port 2: LOAD CELLS-------------------------
loadPort = serial.Serial('/dev/cu.wchusbserial1410', 115200)


# NUMBER of Measurements noM and Buffer Size
noM = 5
buffsize = 100


# Calibration Constants of the Load Cells (Mass = Volt*B + A + Offset).
bSlopeLC = np.array([5.601, 5.908, 5.683, 5.847, 5.803, 5.396])
aInterceptLC = np.array([-2.220, 15.906, 2.854, 9.658, 9.290, -6.818])
linOffsetVoltLC = np.array([15.030, 3.914, 10.996, 6.222, 6.470, 21.488])
# Reversing because of linear calibration from excel for Volt = Mass*B + A.
aInterceptLC = - aInterceptLC / bSlopeLC
linOffsetVoltLC = - linOffsetVoltLC / bSlopeLC
bSlopeLC = 1 / bSlopeLC


# Weights array, buffer and averages for Tags and Load Cells
TagBuffer = np.zeros((buffsize, 6), dtype=np.float)
LoadBuffer = np.zeros((buffsize, 6), dtype=np.float)
AvgTagi = np.zeros((noM, 6), dtype=np.float)
AvgLoadi = np.zeros((noM, 6), dtype=np.float)
TestForce = np.zeros(6, dtype=np.float)

# Terminal initialisation
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

##################################
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def putch(ch):
    sys.stdout.write(ch)

def getch():
    return sys.stdin.read(1)

def getche():
    ch = getch()
    putch(ch)
    return ch

def kbhit():
    dr, dw, de = select([sys.stdin], [], [], 0)
    #    return dr <> []
    return dr

atexit.register(set_normal_term)
set_curses_term()
##################################

# Dictionary for the sensors
sensor = {1: "Right 1 Sensor (Bottom)",
          2: "Right 2 Sensor (Middle)",
          3: "Right 3 Sensor (Top)",
          4: "Left 1 Sensor (Bottom)",
          5: "Left 2 Sensor (Middle)",
          6: "Left 3 Sensor (Top)"}


###########################
#######    START    #######
###########################

print()

# Setting buffer counter
k = 0

# Calculating the averages for certain different loads(noM)
for i in range(0, noM):

    checkBuff = 'Y'

    while checkBuff == 'Y':
        # Reading from TAG and LOAD CELLS serial port.
        try:
            TagForce = str(padPort.readline(), 'utf-8')
            LoadCForce = str(loadPort.readline(), 'utf-8')
        except UnicodeDecodeError:
            continue

        # Removing the return and new line.
        TagForce = TagForce.replace('\r', '')
        TagForce = TagForce.replace('\n', '')
        LoadCForce = LoadCForce.replace('\r', '')
        LoadCForce = LoadCForce.replace('\n', '')

        # Storing values in a slice.
        TagForceStr = TagForce.split(',')
        LoadCForceStr = LoadCForce.split(',')

        # Filling Buffer Matrix if we have string arrays that they are of
        # 6 values. Otherwise, we reject them to fill the buffers again and
        # reduce the counter in order to try and refill the same raw.
        if len(TagForceStr) == 6 and len(LoadCForceStr) == 6:
            try:
                TagBuffer[np.mod(k, buffsize), :] = TagForceStr[:]
                LoadBuffer[np.mod(k, buffsize), :] = LoadCForceStr[:]
            except ValueError:
                continue

            # Increace counter for buffer
            k += 1

            # Displaying message when buffers are filled to continue
            if np.mod(k, buffsize) == (buffsize-1):
                # Calculate and presenting the Buffer Averages
                AvgTagi[i, :] = np.average(TagBuffer, axis=0)
                AvgLoadi[i, :] = np.average(LoadBuffer, axis=0)

                # Printing the Load cells after multiplying the values with the slope and
                # adding the offset.
                print(50*'-')
                print('LOAD CELLS AVERAGES')
                # Mass = Volt*B + A + Offset & removing the Linear Offset from Calibration
                AvgLoadi[i, :] = AvgLoadi[i, :] * bSlopeLC + linOffsetVoltLC + aInterceptLC
                print(np.round(AvgLoadi, 2))
                print(50*'-')
                print('TAG AVERAGES')
                # Swap columns for Tag Force, as it comes as: L1, L2, L3, R1, R2, R3.
                for j in range(0, 3):
                    temp = np.copy(AvgTagi[i, j])
                    AvgTagi[i, j] = AvgTagi[i, j+3]
                    AvgTagi[i, j+3] = temp
                print(np.round(AvgTagi, 2))
                print(50*'-')
                # Message for buffer being filled.
                print(17*'=', 'Buffers filled!', 17*'=')
                print()


                # Press Y or y if you want to refill the buffer for any reason, or type any
                # other key if you wish to continue with the next weight.
                print(i + 1, 'set(s) of averages for TAG and Load Cells are saved.')
                print()
                print()
                checkBuff = input('Do you want to refill buffer for this load??? (y/n)  ').upper()
                print()

                # Display continuously the force data from Load Cells
                if checkBuff != 'Y' and i != noM-1:
                    while True:
                        if kbhit():
                            ch = getch()
                            break

                        try:
                            # TagForce = str(port1.readline(), 'utf-8')
                            LoadCForce = str(loadPort.readline(), 'utf-8')
                        except UnicodeDecodeError:
                            continue
                        LoadCForce = LoadCForce.replace('\r', '')
                        LoadCForce = LoadCForce.replace('\n', '')
                        LoadCForceStr = LoadCForce.split(',')
                        try:
                            if len(LoadCForceStr) == 6:
                                TestForce[:] = LoadCForceStr[:]
                                TestForce = TestForce * bSlopeLC + linOffsetVoltLC + aInterceptLC
                                print(np.round(TestForce, 2))
                        except ValueError:
                            continue


                # Resetting/Cleaning buffers, unless we finished our experiment noM times.
                if i < (noM-1):
                    print('Resetting buffers........')
                    print()
                    k = 0
                    TagBuffer = np.zeros((buffsize, 6))
                    LoadBuffer = np.zeros((buffsize, 6))
                    for j in range(0, 400):
                        try:
                            TagForce = str(padPort.readline(), 'utf-8')
                            LoadCForce = str(loadPort.readline(), 'utf-8')
                        except UnicodeDecodeError:
                            continue
                elif i == (noM-1) and checkBuff == "Y":
                    print('Resetting buffers........')
                    print()
                    k = 0
                    TagBuffer = np.zeros((buffsize, 6))
                    LoadBuffer = np.zeros((buffsize, 6))
                    for j in range(0, 400):
                        try:
                            TagForce = str(padPort.readline(), 'utf-8')
                            LoadCForce = str(loadPort.readline(), 'utf-8')
                        except UnicodeDecodeError:
                            continue


#############################################
# Printing the AvgLoadi and AvgTagi matrices#
#############################################

print()
print()
print(51*'=')
print("FINAL AvgLoadi Load Cells array (Kg): ")
AvgLoadi = np.round(AvgLoadi, 2)
print(AvgLoadi)
print(51*'=')
print("FINAL AvgTagi TAGS array (swapped): ")
AvgTagi = np.round(AvgTagi, 2)
print(AvgTagi)
print(51*'=')


print()
print('All Done!!!')

#####################################
print()
#####################################


#################
# Exporting data#
#################

saveBuffs = input('Do you want to export the Averages in CSV files??? (y/n)  ').upper()
print()
if saveBuffs == 'Y':
    print()
    print('CSV files for AvgLoadi and AvgTagi Saved!')
    np.savetxt('LoadCells_Averages.csv', AvgLoadi, fmt='%4.3f', delimiter=',', header='Right 1, Right 2, Right 3, Left 1, Left 2, Left 3')
    np.savetxt('Tag_Averages.csv', AvgTagi, fmt='%4.3f', delimiter=',', header='Right 1, Right 2, Right 3, Left 1, Left 2, Left 3')
    print()

print()


#######################
# Least Square Fitting#
#######################

# Initialising arrays for slope, intercept and R2
Slopes = np.zeros(6, dtype=np.float)
Intercepts = np.zeros(6, dtype=np.float)
R2 = np.zeros(6, dtype=np.float)

print(50*'-')
# For all 6 Sensors LSQ fitting
for i in range(0, 6):
    Slopes[i], Intercepts[i], R2[i], p_value, std_err = stats.linregress(AvgLoadi[:, i], AvgTagi[:, i])
    print("Set of data for sensor", sensor[i+1])
    print()
    print('The slope is:', np.round(Slopes[i], 2))
    print('The intercept is:', np.round(Intercepts[i], 2))
    print('The R2 is:', np.round(R2[i]**2, 2))
    print(50*'-')

print()


#########################################
# Exporting CSV results from the sensors#
#########################################

saveLin = input('Do you want to export the LSQ data in CSV files??? (y/n)  ').upper()
print()
if saveLin == 'Y':
    print()
    print('CSV files of TAGS for Slopes, Intercepts and R2 Saved!')
    np.savetxt('Slopes-TagCalibration.csv', Slopes, fmt='%4.3f', delimiter=',', header='Slopes')
    np.savetxt('Intercepts-TagCalibration.csv', Intercepts, fmt='%4.3f', delimiter=',', header='Intercepts')
    np.savetxt('R2-TagCalibration.csv', R2, fmt='%4.3f', delimiter=',', header='R2')
    print()
print()


#############
# JSON stuff#
#############

saveJSON = input('Do you want to export JSON config calibration??? (y/n)  ').upper()
print()
if saveJSON == 'Y':
    print()
    print('JSON file exported!')

    # Calculate the data for export to JSON
    LinOff=np.zeros(6, dtype=np.float)
    LinOff=AvgTagi[0, :]-Intercepts
    Intercepts=-Intercepts/Slopes
    Slopes=1/Slopes
    
    # Converting to Python lists for JSON
    np.round(Slopes, 2)
    np.round(Intercepts, 2)
    np.round(LinOff, 2)
    bSlope=Slopes.tolist()
    aIntercept=Intercepts.tolist()
    linOffset=LinOff.tolist()
    print()

    with open('padCal_Config.json', 'w') as outfile:
        data={}
        data["bSlope"]=bSlope
        data["aIntercept"]=aIntercept
        data["linOffset"]=linOffset
        json.dump(data, outfile, indent=4)


print('Finished. Program Exits.')
print()
