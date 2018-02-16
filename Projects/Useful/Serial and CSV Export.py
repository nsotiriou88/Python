##################################################
# Reading from Serial Port Arduino and CSV Export#
##################################################


################################
# Displaying all USB port paths#
################################

import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)


##########################
# Reading from the serial#
##########################

import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
while True:
    b = ser.readline()
    print(b)


#################
# Exporting data#
#################

import numpy as np

Fi = np.array([533.3543543, 345.6546547, 34.23344])
print()
print('Done!')
print()
np.savetxt('Data.Sheet2.csv', Fi, fmt='%3.3f', delimiter=',', header='Kaka, Coco', footer='Blocko')
