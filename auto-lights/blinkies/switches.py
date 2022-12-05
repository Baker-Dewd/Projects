#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global gpios,leftBulbs
gpios = 4,5,6,12,13,16,17,18,19,20,21,22
for led in gpios:
    GPIO.setup(led,GPIO.OUT)

switches = 23,24,25,26,27
for switch in switches:
    GPIO.setup(switch,GPIO.IN)

LeftBulbs       = 17,18,19,20,21,22
LeftTurnBulbs   = 18,19
RrightBulbs     = 4,5,6,12,13,16
RightTurnBulbs  = 4,5
MarkerBulbs     = 17,20,5,12
HeadlightBulbs  = 22,16
BrakeBulbs      = 21,13

LeftTurnSwitch  = 23
RightTurnSwitch = 24
BrakeSwitch     = 25
MarkerSwitch    = 26
HeadlightSwitch = 27 


while True:
    if GPIO.input(23):
        print "Port 23 is 1/HIGH/True - LED ON"

#    if GPIO.input(24):
#        print "Port 24 is 1/HIGH/True - LED ON"

# alloff()


# Actions are sorted. Next to trigger on inputs
#    if input(1) == 1:
#        leftTurn()

#        indicatorsOn()  ## Works
#        leftTurn()      ## Standard Singlas
#        leftTurnPlus()  ## Double Flash signal
#        brakesOn()      ## Works


