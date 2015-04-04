#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def yirmiUcFonksiyonu(channel):
	print("Birinci butona devreyi tamamladi")
	print("bouncetime=300 dedigimiz icin bu calistiktan 300 ms sonrasina kadar\n ikinci kez butonla tetiklenemeyecek")

GPIO.add_event_detect(23, GPIO.RISING, callback=yirmiUcFonksiyonu, bouncetime=300)

while True:
	GPIO.wait_for_edge(24, GPIO.FALLING)
	print("Ikinci buton devreyi tamamladi")
	GPIO.wait_for_edge(24, GPIO.RISING)
	print("Ikinci buton devresi koptu")
GPIO.cleanup()