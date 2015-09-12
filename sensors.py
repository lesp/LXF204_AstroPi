import pygame
from pygame.locals import *
from sense_hat import SenseHat
import time

sense = SenseHat()

sense.show_message("READY",text_colour=[0,255,0])

pygame.init()
pygame.display.set_mode((640,480))

def joystick(event):
    if event.key == pygame.K_DOWN:
        invader()
    elif event.key == pygame.K_UP:
        pressure()
    elif event.key == pygame.K_LEFT:
        temperature()
    elif event.key == pygame.K_RIGHT:
        humidity()

def temperature():
    temp = round(sense.get_temperature(),1)
    sense.show_message("The temperature is %s C" % temp)

def humidity():
    humid = round(sense.get_humidity(),1)
    sense.show_message("Humidity: %s %%" % humid)

def pressure():
    pressure = round(sense.get_pressure(),1)
    sense.show_message("Pressure %s Millibars" % pressure)

def invader():
    x = [0,255,0]
    for i in range(3):
        o = [0,0,0]
        invader = [
            o,x,o,o,o,o,x,o,
            o,o,x,o,o,x,o,o,
            o,x,x,x,x,x,x,o,
            x,x,o,x,x,o,x,x,
            x,x,x,x,x,x,x,x,
            x,o,x,x,x,x,o,x,
            x,o,x,o,o,x,o,x,
            o,o,x,x,x,x,o,o,
        ]
        sense.set_pixels(invader)
        time.sleep(2)
        x = [255,0,0]

sense.low_light = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == KEYDOWN:
            joystick(event)
