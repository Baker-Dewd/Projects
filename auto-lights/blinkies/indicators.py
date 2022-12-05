#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global gpios,leftBulbs
gpios = 4,5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27
for led in gpios:
    GPIO.setup(led,GPIO.OUT)

leftBulbs       = 17,18,19,20,21,22
leftTurnBulbs   = 18,19
rightBulbs      = 23,23,23,23,23,23
rightTurnBulbs  = 23,23
markers         = 17,20,23,23
reverse         = 23,23
Brakes          = 21,23


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


def leftTurnPlus():
    sleep(.5)
    for ledLeftOn in leftTurnBulbs:
        GPIO.output(ledLeftOn,GPIO.HIGH)
    sleep(.1)

    for ledLeftOff in leftTurnBulbs:
        GPIO.output(ledLeftOff,GPIO.LOW)
    sleep(.1)

    for ledLeftOn in leftTurnBulbs:
        GPIO.output(ledLeftOn,GPIO.HIGH)
    sleep(.1)

    for ledLeftOff in leftTurnBulbs:
        GPIO.output(ledLeftOff,GPIO.LOW)
    sleep(.1)


def RightTurn():
    for ledRightOn in rightTurnBulbs:
        GPIO.output(ledRightOn,GPIO.HIGH)
    sleep(.5)

    for ledRightOff in rightTurnBulbs:
        GPIO.output(ledRightOff,GPIO.LOW)
    sleep(.5)


def brakesOn():
    for ledBrakesOn in Brakes:
        GPIO.output(ledBrakesOn,GPIO.HIGH)


def brakesOff():
    for ledBrakesOff in Brakes:
        GPIO.output(ledBrakesOff,GPIO.LOW)


alloff()
# while True:


# Actions are sorted. Next to trigger on inputs
#    if input(1) == 1:
#        leftTurn()

#        indicatorsOn()  ## Works
#        leftTurn()      ## Standard Singlas
#        leftTurnPlus()  ## Double Flash signal
#        brakesOn()      ## Works


