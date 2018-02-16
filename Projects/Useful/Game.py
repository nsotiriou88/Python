import pygame, sys
from pygame.locals import *
import serial
import numpy as np



pygame.init()
pygame.display.set_mode((300, 150))
pygame.display.set_caption("Press space to continue")
bSlope = np.array([5.601, 5.908, 5.683, 5.847, 5.803, 5.396])
aIntercept = np.array([-2.220, 15.906, 2.854, 9.658, 9.290, -6.818])
linOffsetVolt = np.array([15.030, 3.914, 10.996, 6.222, 6.470, 21.488])
TestForce = np.zeros(6, dtype=np.float)

port1 = serial.Serial('/dev/cu.usbmodem1421', 115200)
# port1 = serial.Serial('/dev/cu.wchusbserial1410', 115200)


for i in range(0, 3):

    X = 1
    while X == 1:
        for event in pygame.event.get():
            TagForce = str(port1.readline(), 'utf-8')
            TagForce = TagForce.replace('\r', '')
            TagForce = TagForce.replace('\n', '')
            TestForceStr = TagForce.split(',')
            if len(TestForceStr) == 6:
                TestForce[:] = TestForceStr[:]
                TestForce = (TestForce - aIntercept - linOffsetVolt) / bSlope
                print(TestForce)
            if event.type == QUIT:
                # EXIT with closing window
                sys.exit()
            if event.type == KEYDOWN and event.dict['key'] == 32:
                print(str(event.dict['key']))
                # EXIT with pressing a key
                X = 2
        pygame.event.pump()
    print("my name is nick")

print('Program exited after 3 iterations.')
