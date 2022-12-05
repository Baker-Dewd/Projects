#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global gpios,leftBulbs,LeftTurnBulbs,RightBulbs,RightTurnBulbs,MarkerBulbs,Headlightbulbs,BrakeBulbs
global LeftTurnSwitch,RightTurnSwitch,BrakeSwitch,MarkerSwitch,HeadlightSwitch

gpios = 4,5,6,12,13,16,17,18,19,20,21,22
for led in gpios:
    GPIO.setup(led,GPIO.OUT)

switches = 23,24,25,26,27
for switch in switches:
    GPIO.setup(switch,GPIO.IN)

LeftBulbs       = 17,18,19,20,21,22
LeftTurnBulbs   = 18,19
RightBulbs      = 4,5,6,12,13,16
RightTurnBulbs  = 4,5
MarkerBulbs     = 17,20,5,12
HeadlightBulbs  = 22,16
BrakeBulbs      = 21,13

LeftTurnSwitch  = 23
RightTurnSwitch = 24
BrakeSwitch     = 25
MarkerSwitch    = 26
HeadlightSwitch = 27 


def alloff():
    for led in gpios:
        GPIO.output(led,GPIO.LOW)


def indicatorsOn():
    for ledMarkers in MarkerBulbs:
        GPIO.output(ledMarkers,GPIO.HIGH)
        GPIO.output(ledMarkers,GPIO.LOW)
        break


def leftTurn():
    for ledLeftOn in LeftTurnBulbs:
        GPIO.output(ledLeftOn,GPIO.HIGH)
    sleep(.5)

    for ledLeftOff in LeftTurnBulbs:
        GPIO.output(ledLeftOff,GPIO.LOW)
    sleep(.5)


def leftTurnPlus():
    sleep(.5)
    for ledLeftOn in LeftTurnBulbs:
        GPIO.output(ledLeftOn,GPIO.HIGH)
    sleep(.1)

    for ledLeftOff in LeftTurnBulbs:
        GPIO.output(ledLeftOff,GPIO.LOW)
    sleep(.1)

    for ledLeftOn in LeftTurnBulbs:
        GPIO.output(ledLeftOn,GPIO.HIGH)
    sleep(.1)

    for ledLeftOff in LeftTurnBulbs:
        GPIO.output(ledLeftOff,GPIO.LOW)
    sleep(.1)
        


def RightTurn():
    for ledRightOn in rightTurnBulbs:
        GPIO.output(ledRightOn,GPIO.HIGH)
    sleep(.5)
#        leftTurnPlus()  ## Double Flash signal

    for ledRightOff in rightTurnBulbs:
        GPIO.output(ledRightOff,GPIO.LOW)
    sleep(.5)


def brakes():
    for ledBrakes in BrakeBulbs:
        GPIO.output(ledBrakes,GPIO.HIGH)
        GPIO.output(ledBrakes,GPIO.LOW)
        break


alloff()
while True:

#    if GPIO.input(23):
#     brakes()      ## Works
     indicatorsOn()  ## Works

     leftTurnPlus()      ## Fast double signal

#        indicatorsOn()  ## Works
#    leftTurn()      ## Standard Signals
#        leftTurnPlus()  ## Double Flash signal
#        brakesOn()      ## Works


