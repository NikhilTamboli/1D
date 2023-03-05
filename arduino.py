import serial
import time
import struct


print('This program allows a user to turn an LED on and off')
print('type H to turn the LED on')
print('type L to turn the LED off')
print('type q to quit')

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)


def writeToArduino(data):
    string = b''

    for i in data:
        string += struct.pack('!B', i)

    # ser.write(string)
    # ser.write((byte*)arr, sizeof(arr))


# user_input = 'L'
# while user_input != 'q':
#     user_input = input('H = on, L = off, q = quit: ')
#     byte_command = user_input.encode('utf-8')
#     # ser.write(byte_command)   # send a byte
#     d = [byte_command]
#     writeToArduino(byte_command)
#     time.sleep(0.5)  # wait 0.5 seconds

print('q entered. Exiting the program')


ser.close()
