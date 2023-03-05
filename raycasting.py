import pygame
from pygame.locals import *
import math as m
import serial
import time
import struct

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

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
fov = 359
xpos, ypos = (1, 1)
rot_r = 0

sensitivity = m.pi/256
move_speed = 0.01

precision = 0.01

wk, sk, ak, dk = False, False, False, False

run = True


def showLED(data):
    # for i in range(len(data)):
    #     ser.write(data[i])
    ser.write(data)
    # print(data)


leds = []

ind = 0
while run:
    clock.tick(fps)
    # showLED((bytearray(leds)))
    showLED(leds)
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
        if e.type == KEYUP:
            if e.key == pygame.K_w:
                wk = False
            if e.key == pygame.K_s:
                sk = False
            if e.key == pygame.K_a:
                ak = False
            if e.key == pygame.K_d:
                dk = False

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
            pixel = [0, 255-d, 255-d]
            leds.append(0)
            leds.append(255-d)
            leds.append(255-d)
        ind += 1
