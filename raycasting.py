import pygame
from pygame.locals import *
import math as m
from struct import *
import serial
import sys
import time
import random
import ast


ser = serial.Serial(baudrate='230400', timeout=.5, port='COM3')
time.sleep(5)

# ser = serial.Serial('/dev/ttyACM0', 9600)
# time.sleep(2)

win_width, win_height = (800, 50)
# win_width, win_height = (700, 800)
fps = 165  # 165hz monitor btw the way
display = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Raycasting")
clock = pygame.time.Clock()

environment = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

# environment = [
#     [1, 1, 1, 1],
#     [1, 0, 0, 1],
#     [1, 0, 0, 1],
#     [1, 1, 1, 1],
# ]

fov = 359
xpos, ypos = (1, 1)
rot_r = 0

sensitivity = m.pi/256*2
move_speed = 0.005

precision = 0.009

wk, sk, ak, dk = False, False, False, False

run = True


def renderMaze(maze):
    x = 0
    y = 0
    for row in maze:
        for block in row:
        #block dimension 60*60 
        # 0 represents movable cell
            if block == 0:
                pygame.draw.rect(display, (255, 205, 178), (x, y, 60, 60))
        # 1 represents wall
            elif block == 1:
                pygame.draw.rect(display, (229, 152, 155) ,(x, y, 60, 60))
        # 2 represents destination
            elif block == 2:
                pygame.draw.rect(display, (255, 183, 0), (x, y, 60, 60))
                
        # to display the starting cell
            elif block == 3:
                pygame.draw.rect(display, (120, 150, 100), (x, y, 60, 60))
            
        #since dimension of rectangle is 60*60, we move the starting coordinate after each block is drawn
            x = x+60
        y = y+60
        x = 0

leds = []

ind = 0
br = 150
while run:
    clock.tick(fps)
    if(len(leds)>0):
        ser.write(pack('60h', leds[0], leds[1], leds[2], leds[3], leds[4], leds[5], leds[6], leds[7], leds[8], leds[9],leds[10], leds[11], leds[12], leds[13], leds[14], leds[15], leds[16], leds[17], leds[18], leds[19], leds[20], leds[21], leds[22], leds[23], leds[24],leds[25], leds[26], leds[27], leds[28], leds[29],leds[30],leds[31],leds[32],leds[33],leds[34],leds[35],leds[36],leds[37],leds[38],leds[39], leds[40],leds[41],leds[42],leds[43],leds[44],leds[45],leds[46],leds[47],leds[48],leds[49],leds[50],leds[51],leds[52],leds[53],leds[54],leds[55],leds[56],leds[57],leds[58],leds[59]))

    leds = []
    # renderMaze(environment)
    pygame.display.update()
    pygame.display.set_caption(
        "Raycasting - FPS: " + str(round(clock.get_fps())))

    for e in pygame.event.get():
        if e.type == QUIT:
            run = False

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
    if dk == True:
        rot_r += sensitivity
    if environment[int(x)][int(y)] == 0:
        xpos, ypos = (x, y)

    display.fill((0, 0, 0))

    if(environment[int(x)][int(y)]==2):
        print("end")

    for i in range(fov+1):
        rot_d = rot_r + m.radians(i - fov/2)
        x, y = (xpos, ypos)
        sin, cos = (precision*m.sin(rot_d), precision*m.cos(rot_d))
        j = 0
        while True:
            x, y = (x + cos, y + sin)
            j += 1
            if environment[int(x)][int(y)] == 1:
                tile = environment[int(x)][int(y)]
                d = j
                j = j * m.cos(m.radians(i-fov/2))
                # height = (10/j * 2500)
                height = 2500
                break
        if d > 255:
            d = 255
        pygame.draw.line(display,
                            (0, 255-d, 255-d),  # color
                            (i*(win_width/fov), (win_height/2) + height),  # pos 1
                            (i*(win_width/fov), (win_height/2) - height),  # pos 2
                            width=int(win_width/fov))            
        if(ind%6==0):

            leds.append(255-d)
        ind += 1