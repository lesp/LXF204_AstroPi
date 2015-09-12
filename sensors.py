import pygame
from pygame.locals import *
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("READY",text_colour=[0,255,0])

pygame.init()
pygame.display.set_mode((640,480))

def joystick(event):
    if event.key == pygame.K_DOWN:
        print("DOWN")
        temperature()
    elif event.key == pygame.K_UP:
        print("UP")
        humidity()
    elif event.key == pygame.K_LEFT:
        print("LEFT")
    elif event.key == pygame.K_RIGHT:
        print("RIGHT")

def temperature():
    temp = sense.get_temperature()
    sense.show_message("The temperature is %s C" % temp)

def humidity():
    humid = sense.get_humidity()
    sense.show_message("Humidity: %s %%rH" % humidity)

sense.low_light = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == KEYDOWN:
            joystick(event)
