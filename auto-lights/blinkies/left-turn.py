#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# I wonder if a mapping would work better here.
# states[0] = 0,1,0,0,0,1,1,0
# states[1] = 1,1,0,0,1,0,1,0 
# states[2] = 0,1,0,0,0,1,1,0
# states[3] = 1,1,0,0,1,0,1,0 
# ( etc )

# double()
# for led in states
#   states[0] on,off
#   states[2] on,off
#   etc

global gpios,leftBulbs
gpios       = 4,5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27
leftBulbs   = 17,18,19,20,21,22
rightBulbs  = 23,23,23,23,23,23
markers     = 23,23,4,23
reverse     = 23,23

######  0  1  2  3  4  5
# 0 == Front Marker
# 1 == Front Turn Signal
# 2 == Rear Turn Signal
# 3 == Rear Brake
# 4 == Rear Marker
# 5 == Reverse Light
######

# Open Loop :: 
# Switch 1 on == Markers
# Switch 2 on == Left Turn
# Switch 3 on == Right Markers
# Switch  2&3 == Hazards
# Switch 4 on == Brakes

###### 


def alloff():
    for led in gpios:
        GPIO.setup(led,GPIO.OUT)
    for led in gpios:
        GPIO.output(led,GPIO.LOW)

def double():
    while True:
        alloff()
        GPIO.output(leftBulbs[1],GPIO.HIGH)
        GPIO.output(leftBulbs[2],GPIO.HIGH)
        sleep(.1)
        GPIO.output(leftBulbs[1],GPIO.LOW)
        GPIO.output(leftBulbs[2],GPIO.LOW)
        sleep(.1)
        GPIO.output(leftBulbs[1],GPIO.HIGH)
        GPIO.output(leftBulbs[2],GPIO.HIGH)
        sleep(.1)
        GPIO.output(leftBulbs[1],GPIO.LOW)
        GPIO.output(leftBulbs[2],GPIO.LOW)
        sleep(.3)
        

def doubleplus():
    while True:
        alloff()
        GPIO.output(leftBulbs[1],GPIO.HIGH)
        GPIO.output(leftBulbs[2],GPIO.HIGH)
        sleep(.1)
        GPIO.output(leftBulbs[2],GPIO.LOW)
        sleep(.1)
        GPIO.output(leftBulbs[4],GPIO.HIGH)
        sleep(.1)
        GPIO.output(leftBulbs[4],GPIO.LOW)
        GPIO.output(leftBulbs[2],GPIO.HIGH)
        sleep(.1)
        GPIO.output(leftBulbs[1],GPIO.LOW)
        GPIO.output(leftBulbs[2],GPIO.LOW)
        GPIO.output(leftBulbs[4],GPIO.LOW)
        sleep(.3)


def standard():
    while True:
        alloff()
        sleep(.5)
        GPIO.output(leftBulbs[1],GPIO.HIGH)
        GPIO.output(leftBulbs[2],GPIO.HIGH)
        sleep(.2)


#standard()
double()
#doubleplus()


