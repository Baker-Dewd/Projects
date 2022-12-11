#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)


GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)

GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
