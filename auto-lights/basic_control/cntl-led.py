#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

gpios = 4,5,6,12,13,16,17,18,19,20,21,22,23,24,25,26,27

one = 22,26
two = 21,20,23,26,27
three = 21,20,23,19,27
four = 22,20,23,19

def displayled(gpios,display):
    for led in gpios:
        GPIO.setup(led, GPIO.OUT)

    for led in gpios:
        GPIO.output(led, GPIO.LOW)

    for led in display:
        GPIO.setup(led, GPIO.OUT)

    for led in display:
        GPIO.output(led, GPIO.HIGH)


displayled(gpios,four) 

