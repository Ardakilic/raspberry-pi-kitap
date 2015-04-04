#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	GPIO.wait_for_edge(23, GPIO.RISING)
	print("Birinci buton devreyi tamamladi")
	GPIO.wait_for_edge(23, GPIO.FALLING)
	print("Birinci buton devresi koptu")

	GPIO.wait_for_edge(24, GPIO.FALLING)
	print("Ikinci buton devreyi tamamladi")
	GPIO.wait_for_edge(24, GPIO.RISING)
	print("Ikinci buton devresi koptu")

GPIO.cleanup()