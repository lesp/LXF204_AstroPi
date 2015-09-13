import pygame
from pygame.locals import *
from sense_hat import SenseHat
import time

sense = SenseHat()

pygame.init()
pygame.display.set_mode((688,361))

def image():
    pygame.display.set_caption("Linux Format presents...")
    picture = pygame.image.load("image.png")
    screen = pygame.display.set_mode((688,361))
    screen.blit(picture,(0,0))
    pygame.display.flip()

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
    if temp < 20:
        sense.show_message("The temperature is %s C" % temp, text_colour=[0,0,255])
    elif temp > 20 and temp < 30:
        sense.show_message("The temperature is %s C" % temp, text_colour=[0,255,0])
    else:
        sense.show_message("The temperature is %s C" % temp, text_colour=[255,0,0])

def humidity():
    humid = round(sense.get_humidity(),1)
    sense.show_message("Humidity: %s %%" % humid)

def pressure():
    pressure = round(sense.get_pressure(),1)
    sense.show_message("Pressure %s Millibars" % pressure)

def invader():
    for i in range(8):
        x = [0,255,0]
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
        time.sleep(0.5)
        invader = [
            o,o,o,o,o,o,o,o,
            o,x,x,o,o,x,x,o,
            o,x,x,x,x,x,x,o,
            x,o,x,x,x,x,o,x,
            x,x,x,x,x,x,x,x,
            x,o,x,x,x,x,o,x,
            x,o,x,o,o,x,o,x,
            x,x,o,o,o,o,x,x,
        ]
        sense.set_pixels(invader)
        time.sleep(0.5)
    sense.clear()    

sense.low_light = True
image()
sense.clear()
sense.show_message("READY",text_colour=[0,255,0])
while True:
    try:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                joystick(event)
    except KeyboardInterrupt:
        pygame.quit()
