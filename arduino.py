# Arduino forum 2020 - https://forum.arduino.cc/index.php?topic=714968
import serial
from struct import *
import sys
import time
import random
import ast

try:
    ser = serial.Serial(baudrate='230400', timeout=.5, port='COM3')
except:
    print('Port open error')

time.sleep(5)  # no delete!
br = 100
while True:
    # try:
    ser.write(pack('20h', br, br, br, br, br, br, br, br, br,
              br, br, br, br, br, br, br, br, br, br, br))  # the 15h is 15 element, and h is an int type data
    time.sleep(.01)
    # dat = ser.readline()  # read a line data

    # if dat != b'' and dat != b'\r\n':
    #     try:  # convert in list type the readed data
    #         dats = str(dat)
    #         dat1 = dats.replace("b", "")
    #         dat2 = dat1.replace("'", '')
    #         dat3 = dat2[:-4]
    #         # list_ value can you use in program
    #         list_ = ast.literal_eval(dat3)
    #         print(dat3)
    #     except:
    #         print('Error in corvert, readed: ', dats)
    # time.sleep(.05)
    # except KeyboardInterrupt:
    #     break
    # except:
    #     print(str(sys.exc_info()))  # print error
    #     break

# the delays need, that the bytes are good order
