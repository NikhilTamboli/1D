import pygame
from pygame.locals import *
import math as m
from struct import *
import serial
import sys
import time
import random
import ast


ser = serial.Serial(baudrate='115200', timeout=.5, port='COM4')
time.sleep(5)

# ser = serial.Serial('/dev/ttyACM0', 9600)
# time.sleep(2)

win_width, win_height = (1600, 50)
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
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
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

sensitivity = m.pi/256
move_speed = 0.01

precision = 0.01

wk, sk, ak, dk = False, False, False, False

run = True


leds = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

ind = 0
br = 150
while run:
    clock.tick(fps)
    # print(leds[0])
    # ser.write(pack('60h', br*leds[0], br*leds[1], br*leds[2], br*leds[3], br*leds[4], br*leds[5], br*leds[6], br*leds[7], br*leds[8],
    #           br*leds[9], br*leds[10], br*leds[11], br*leds[12], br*leds[13], br *
    #                leds[14], br*leds[15], br*leds[16], br *
    #                leds[17], br*leds[18], br*leds[19],
    #                br*leds[20], br*leds[21], br*leds[22], br*leds[23], br*leds[24], br *
    #                leds[25], br*leds[26], br *
    #                leds[27], br*leds[28], br*leds[29],
    #                br*leds[30], br*leds[31], br*leds[32], br*leds[33], br*leds[34], br *
    #                leds[35], br*leds[36], br *
    #                leds[37], br*leds[38], br*leds[39],
    #                br*leds[40], br*leds[41], br*leds[42], br*leds[43], br*leds[44], br *
    #                leds[45], br*leds[46], br *
    #                leds[47], br*leds[48], br*leds[49],
    #                br*leds[50], br*leds[51], br*leds[52], br*leds[53], br*leds[54], br*leds[55], br*leds[56], br*leds[57], br*leds[58], br*leds[59],))  # the 15h is 15 element, and h is an int type data
    # ser.write(pack('60h', br*100, br*100, br*100, br*100, br*100, br*100,
    #           br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100,
    #                br*100, br*100, br*100, br*100, br*100, br*100,
    #                br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100,
    #                br*100, br*100, br*100, br*100, br*100, br*100,
    #                br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100,
    #                br*100, br*100, br*100, br*100, br*100, br*100,
    #                br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100, br*100,))
    ser.write(pack('20h', leds[0], leds[1], leds[2], leds[3], leds[4], leds[5], leds[6], leds[7], leds[8], leds[9],
              leds[10], leds[11], leds[12], leds[13], leds[14], leds[15], leds[16], leds[17], leds[18], leds[19]))
    # ser.write(pack('20h', br, br, br, br, br, br, br, br, br,
    #           br, br, br, br, br, br, br, br, br, br, br))

    # time.sleep(.01)
    # print(leds[0], leds[1], leds[2], leds[3], leds[4], leds[5], leds[6], leds[7], leds[8],
    #       leds[9], leds[10], leds[11], leds[12], leds[13], leds[14], leds[15], leds[16], leds[17], leds[18],
    #       leds[19])
    # print(str(ser.readline()))
    leds = []
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

    for i in range(fov+1):
        rot_d = rot_r + m.radians(i - fov/2)
        x, y = (xpos, ypos)
        sin, cos = (precision*m.sin(rot_d), precision*m.cos(rot_d))
        j = 0
        while True:
            x, y = (x + cos, y + sin)
            j += 1
            if environment[int(x)][int(y)] != 0:
                tile = environment[int(x)][int(y)]
                d = j
                j = j * m.cos(m.radians(i-fov/2))
                # height = (10/j * 2500)
                height = 2500
                break
        if d > 255:
            d = 255

        if (ind % 6 == 0):
            pygame.draw.line(display,
                             (0, 255-d, 255-d),  # color
                             (i*(win_width/fov), (win_height/2) + height),  # pos 1
                             (i*(win_width/fov), (win_height/2) - height),  # pos 2
                             width=int(win_width/fov))
            # pixel = [0, 255-d, 255-d]
            # leds.append(0)
            leds.append(255-d)
            # leds.append(255-d)
        ind += 1
