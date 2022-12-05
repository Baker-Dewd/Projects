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
gpios = 4,5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27
for led in gpios:
    GPIO.setup(led,GPIO.OUT)

#leftBulbs       = 17,18,19,20,21,22
markers         = 17,18,19,20,21,22
leftTurnBulbs   = 18,20
rightBulbs      = 23,23,23,23,23,23
rightTurn       = 23,23
#markers         = 17,19,23,23
reverse         = 23,23
Brakes          = 21,23


######  0  1  2  3  4  5
# 0 == Front Marker :: Left
# 1 == Front Turn Signal
# 2 == Rear Turn Signal
# 3 == Rear Brake
# 4 == Rear Marker
# 5 == Reverse Light
######

###### 


def alloff():
    for led in gpios:
        GPIO.output(led,GPIO.LOW)


def indicatorsOn():
    for ledMarkerOn in markers:
        GPIO.output(ledMarkerOn,GPIO.HIGH)

def indicatorsOff():
    for ledMarkerOff in markers:
        GPIO.output(ledMarkerOff,GPIO.LOW)

def leftTurn():
    for ledLeftOn in leftTurnBulbs:
        GPIO.output(ledLeftOn,GPIO.HIGH)
    sleep(.5)

    for ledLeftOff in leftTurnBulbs:
        GPIO.output(ledLeftOff,GPIO.LOW)
    sleep(.5)

def brakesOn():
    for ledBrakesOn in Brakes:
        GPIO.output(ledBrakesOn,GPIO.HIGH)
        
def brakesOff():
    for ledBrakesOff in Brakes:
        GPIO.output(ledBrakesOff,GPIO.LOW)



alloff()
while True:

# Switch 1 on == Markers
# Switch 2 on == Left Turn
# Switch 3 on == Right Markers
# Switch  2&3 == Hazards
# Switch 4 on == Brakes

#    if input(1) == 1:
#        leftTurn()

        indicatorsOn()
        #leftTurn()
        #brakesOff()


# How to handle turning on the markers, and leaving them on for the duration of the loop.


#standard()
#double()


