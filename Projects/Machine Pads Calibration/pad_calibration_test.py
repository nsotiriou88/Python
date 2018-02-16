# The purpose of the code is to test the Calibrated Pads after the
# force calibration code with known static loads, so that we test
# the calibration constats that we produced. The code imports these 
# constants from the JSON file that is exported after the force
# calibration code is finished. The code is also asking to export
# the CSV file with the results. Data from Tags comes as (L1,L2,L3,
# R1,R2,R3).
##########################
# Reading from the serial#
##########################

import serial
import numpy as np
import sys
import termios
import atexit
import json
from select import select

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

# Reading from serial port. Set up the appropriate port!!!-------
ser = serial.Serial('/dev/cu.usbmodem16042201', 115200)

# Weights array, buffer and average of sensor forces
noM = 5

circBuff = np.zeros((100, 6), dtype=np.float)
Fi = np.zeros((noM, 6), dtype=np.float)
TestForce = np.zeros(6, dtype=np.float)

# Calibration Constants of the Load Cells (Mass = Volt*B + A + Offset).
# Importing them from JSON padCal_config.json
with open('padCal_Config.json', 'r') as infile:
    data=json.load(infile)
    bSlopeData=data["bSlope"]
    aInterceptData=data["aIntercept"]
    linOffsetData=data["linOffset"]

bSlope = np.asarray(bSlopeData)
aIntercept = np.asarray(aInterceptData)
linOffset = np.asarray(linOffsetData)
linOffset = - linOffset * bSlope

##################################
# Terminal initialisation
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

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

###########################
#######    START    #######
###########################

print()

# Setting buffer counter
k = 0

# For the 5 Fi averages, for calibration only. We use the same script with SerialEx for
# the calibration; we can change weight each time we fill one buffer. Total of 5.
for i in range(0, noM):

    check = 'Y'

    while check == 'Y':
        # Reading from serial port.
        try:
            force = str(ser.readline(), 'utf-8')
        except UnicodeDecodeError:
            continue
        force = force.replace('\r', '')
        force = force.replace('\n', '')
        sforce = force.split(',')

        # Filling Buffer Matrix if we have a sforce array of 6 values.
        if len(sforce) == 6:
            try:
                circBuff[np.mod(k, 100), :] = sforce[:]
            except ValueError:
                continue

            # Increace counter for buffer
            k += 1

            # Displaying message when buffer is filled to continue
            if np.mod(k, 100) == 99:
                # Calculate and presenting the Buffer Average
                Fi[i, :] = np.average(circBuff, axis=0)
                for j in range(0, 3):
                    temp = np.copy(Fi[i, j])
                    Fi[i, j] = Fi[i, j+3]
                    Fi[i, j+3] = temp
                Fi[i, :] = Fi[i, :] * bSlope + linOffset + aIntercept

                # Printing the Load Cells average array
                print(50*'-')
                print('LOAD CELLS AVERAGES')
                print(np.round(Fi, 2))
                print(50*'-')
                # Message for buffer being filled.
                print(17*'=', 'Buffer filled!', 17*'=')
                print()


                # Press Y if you want to refill the buffer for any reason, or type any other
                # key if you wish to continue with the next weight.
                print(i + 1, 'set(s) of averages for Load Cells are saved.')
                check = input('Do you want to refill buffer for this load?(y/n)  ').upper()
                print()

                # Display continuously the force data from Tag
                if check != 'Y' and i != noM-1:
                    while True:
                        if kbhit():
                            ch = getch()
                            break

                        try:
                            force = str(ser.readline(), 'utf-8')
                        except UnicodeDecodeError:
                            continue
                        force = force.replace('\r', '')
                        force = force.replace('\n', '')
                        sforce = force.split(',')
                        try:
                            if len(sforce) == 6:
                                TestForce[:] = sforce[:]
                                for j in range(0, 3):
                                    temp2 = np.copy(TestForce[j])
                                    TestForce[j] = TestForce[j+3]
                                    TestForce[j+3] = temp2
                                TestForce = TestForce * bSlope + linOffset + aIntercept
                                print(np.round(TestForce, 2))
                        except ValueError:
                            continue

                # Resetting/Cleaning buffers, unless we finished our experiment noM times.
                if i < 4:
                    print('Resetting buffers........')
                    print()
                    k = 0
                    circBuff = np.zeros((100, 6))
                    for j in range(0, 400):
                        try:
                            force = str(ser.readline(), 'utf-8')
                        except UnicodeDecodeError:
                            continue
                elif i == 4 and check == "Y":
                    print('Resetting buffers........')
                    print()
                    k = 0
                    circBuff = np.zeros((100, 6))
                    for j in range(0, 400):
                        try:
                            force = str(ser.readline(), 'utf-8')
                        except UnicodeDecodeError:
                            continue


#########################
# Printing the matrix Fi#
#########################
print()
print()
print(51*'=')
print("FINAL Averages array for Fi (volt): ")
print(np.round(Fi, 2))
print(51*'=')


print()
print('Done!')


#####################################
print()
#####################################


#################
# Exporting data#
#################

save = input('Do you want to export the Averages in CSV files??? (y/n)  ').upper()
print()
if save == 'Y':
    print()
    print('CSV file Saved!')
    np.savetxt('CalData.csv', Fi, fmt='%4.3f', delimiter=',', header='Right 1, Right 2, Right 3, Left 1, Left 2, Left 3')
    print()

print('Finished. Program Exits.')
print()
