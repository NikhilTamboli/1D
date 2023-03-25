import pygame
from pygame.locals import *
import math as m
from struct import *
import serial
import sys
import time
import random
import ast
import asyncio
from pynput.keyboard import Key, Controller
import socket
import struct

HOST = '0.0.0.0'
PORT = 8888       # Port to listen on
 
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))
 
# Listen for incoming connections
server_socket.listen(1)
print('Listening on {}:{}'.format(HOST, PORT))

keyboard = Controller()

pygame.init()  # Loads pygame engine
pygame.joystick.init()  # main joystick device system

try:
	j = pygame.joystick.Joystick(0) # create a joystick instance
	j.init() # init instance
	print ("Enabled joystick: {0}".format(j.get_name()))
except pygame.error:
	print ("no joystick found.")

def gamepad():
        
        for event in pygame.event.get():
            # print("here")
            if event.type == pygame.QUIT:
                print('goodbye')
                sys.exit()
            if event.type == pygame.JOYAXISMOTION:
                if j.get_axis(0) >= 0.5:
                    print ("right has been pressed")  # Right
                    return "a"

                if j.get_axis(0) <= -1:
                    print ("left has been pressed")   # Left
                    return "d"
                    #print (lead_x_change, lead_y_change)

                if j.get_axis(1) >= 0.5:
                    print ("Down has been pressed")  # Down
                    return "s"
                
                if j.get_axis(1) <= -1:
                    print ("Up has been pressed")    # Up
                    return "w"

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick Button pressed")    

ser = serial.Serial(baudrate='230400', timeout=.5, port='COM4')
time.sleep(5)



def renderMaze(maze, display):
    x = 0
    y = 0
    for row in maze:
        for block in row:
        #block dimension 60*60 
        # 0 represents movable cell
            if block == 0:
                pygame.draw.rect(display, (255, 205, 178), (x, y, 20, 20))
        # 1 represents wall
            elif block == 1:
                pygame.draw.rect(display, (229, 152, 155) ,(x, y, 20, 20))
        # 2 represents destination
            elif block == 2:
                pygame.draw.rect(display, (255, 183, 0), (x, y, 20, 20))
                
        # to display the starting cell
            elif block == 3:
                pygame.draw.rect(display, (120, 150, 200), (x, y, 20, 20))
            
        #since dimension of rectangle is 60*60, we move the starting coordinate after each block is drawn
            x = x+20
        y = y+20
        x = 0
   

def game():

    prev = 0
    # win_width, win_height = (800, 50)
    win_width, win_height = (400, 450)
    fps = 165  # 165hz monitor btw the way
    display = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Raycasting")
    clock = pygame.time.Clock()

    environment = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    ]

    fov = 359
    xpos, ypos = (1, 1)
    rot_r = 0

    sensitivity = m.pi/256*2
    move_speed = 0.1

    precision = 0.0075

    wk, sk, ak, dk = False, False, False, False

    run = True

    leds = []

    ind = 0
    br = 150
    forward = 180

    end = False


    while run:

        # event = gamepad()
        # print(event)
        # print(chair())
        clock.tick(fps)
        if(len(leds)>0):
            ser.write(pack('60h', leds[0], leds[1], leds[2], leds[3], leds[4], leds[5], leds[6], leds[7], leds[8], leds[9],leds[10], leds[11], leds[12], leds[13], leds[14], leds[15], leds[16], leds[17], leds[18], leds[19], leds[20], leds[21], leds[22], leds[23], leds[24],leds[25], leds[26], leds[27], leds[28], leds[29],leds[30],leds[31],leds[32],leds[33],leds[34],leds[35],leds[36],leds[37],leds[38],leds[39], leds[40],leds[41],leds[42],leds[43],leds[44],leds[45],leds[46],leds[47],leds[48],leds[49],leds[50],leds[51],leds[52],leds[53],leds[54],leds[55],leds[56],leds[57],leds[58],leds[59]))

        leds = []
        renderMaze(environment, display)
        pygame.display.update()
        pygame.display.set_caption(
            "Raycasting - FPS: " + str(round(clock.get_fps())))

        for e in pygame.event.get():
            if e.type == QUIT:
                run = False

            if e.type==pygame.JOYAXISMOTION:
                print(e.axis)

            if e.type == pygame.JOYBUTTONDOWN:
                # print("Joystick Button  pressed") 
                if(e.button)==0:
                    sk=True
                if(e.button)==1:
                    dk=True
                if(e.button)==2:
                    ak=True
                if(e.button)==3:
                    wk=True    
            if e.type == pygame.JOYBUTTONUP:
                # print("Joystick Button released") 
                if(e.button)==0:
                    sk=False
                if(e.button)==1:
                    dk=False
                if(e.button)==2:
                    ak=False
                if(e.button)==3:
                    wk=False                                                         
                                        
                

            if e.type == KEYDOWN:
                if e.key == pygame.K_w:
                    wk = True
                if e.key == pygame.K_s:
                    sk = True
                if e.key == pygame.K_a:
                    ak = True
                if e.key == pygame.K_d:
                    dk = True
                if e.key == pygame.K_z:
                    br -= 1
            if e.type == KEYUP:
                if e.key == pygame.K_w:
                    wk = False
                if e.key == pygame.K_s:
                    sk = False
                if e.key == pygame.K_a:
                    ak = False
                if e.key == pygame.K_d:
                    dk = False
                if e.key == pygame.K_x:
                    br += 1

        x, y = (xpos, ypos)
                             

        if wk == True:
            x, y = (x+move_speed*m.cos(rot_r), y+move_speed*m.sin(rot_r))
        if sk == True:
            x, y = (x-move_speed*m.cos(rot_r), y-move_speed*m.sin(rot_r))
        if ak == True:
            rot_r -= sensitivity
            forward -= 0.5
            if forward<0:
                forward = 0

        if dk == True:
            rot_r += sensitivity
            forward += 0.5
            if forward>360:
                forward = 0
        
        ##########################################
        # Accept incoming connections
        client_socket, address = server_socket.accept()
        # print('Connection from {}'.format(address))
    
        # Receive float data from client
        data = client_socket.recv(1024)
        # float_data=float(data.decode())
        float_data = struct.unpack('f', data)[0]
        # print('Received: {}'.format(float_data))
        # print(f"{float_data:.3f}")
        temp = prev-float_data
        prev=float_data
        rot_r+=temp
        # forward+=temp*50    
        # Close the connection
        client_socket.close()   
        ##########################################

        if(environment[int(x)][int(y)]==2):
            # leds[0]=999
            end = True
            
        if environment[int(x)][int(y)] != 1:
            environment[int(xpos)][int(ypos)]=0
            xpos, ypos = (x, y)
            environment[int(xpos)][int(ypos)]=3

        display.fill((0, 0, 0))
            

        for i in range(fov+1):
            rot_d = rot_r + m.radians(i - fov/2)
            # rot_d = m.radians(i - fov/2)
            x, y = (xpos, ypos)
            sin, cos = (precision*m.sin(rot_d), precision*m.cos(rot_d))
            j = 0
            while True:
                x, y = (x + cos, y + sin)
                j += 1
                if environment[int(x)][int(y)] == 1 :
                    tile = environment[int(x)][int(y)]
                    d = j
                    j = j * m.cos(m.radians(i-fov/2))
                    # height = (10/j * 2500)
                    height = 2500
                    break
            if d > 255:
                d = 255
            if(not end):
                pygame.draw.line(display,
                                    (0, 255-d, 255-d),  # color
                                    (i*(win_width/fov), (win_height/2) + height),  # pos 1
                                    (i*(win_width/fov), (win_height/2) - height),  # pos 2
                                    width=int(win_width/fov))
                pygame.draw.line(display,
                                    (0, 255, 0),  # color
                                    (forward*(win_width/fov), (win_height/2) + height),  # pos 1
                                    (forward*(win_width/fov), (win_height/2) - height),  # pos 2
                                    width=10)                
                                           

                if(ind%6==0):
                    leds.append(255-d)  
                ind += 1
            else:
                for i in range(60):
                    leds.append(0)
                leds[0]=999
            
            
                

game()