import pygame
import sys

pygame.init()  # Loads pygame engine
pygame.joystick.init()  # main joystick device system

try:
	j = pygame.joystick.Joystick(0) # create a joystick instance
	j.init() # init instance
	print ("Enabled joystick: {0}".format(j.get_name()))
except pygame.error:
	print ("no joystick found.")



def gameLoop():

    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('goodbye')
                sys.exit()
            if event.type == pygame.JOYAXISMOTION:
                # print("here")  # Joystick
                if j.get_axis(0) >= 0.5:
                    print ("right has been pressed")  # Right

                if j.get_axis(0) <= -1:
                    print ("left has been pressed")   # Left

                    #print (lead_x_change, lead_y_change)

                if j.get_axis(1) >= 0.5:

                    print ("Down has been pressed")  # Down
                if j.get_axis(1) <= -1:

                    print ("Up has been pressed")    # Up

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick Button pressed")




gameLoop()

pygame.joystick.quit()