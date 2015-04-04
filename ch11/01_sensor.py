#!/usr/bin/env python
# -*- coding: utf-8 -*-

#kodlar adafruit'ten esinlenmiştir.
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def sensorOku(pin):

	#sayaç değeri
	sayac = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

	#0.1 saniye periyodunda aralıklarla ölçüyoruz
	time.sleep(0.1)

	GPIO.setup(pin, GPIO.IN)
	#girişin low değerine eşit olmayana kadar (yani kondansatör aslında dolana kadar) sayaç değeri yükseliyor
	while (GPIO.input(pin) == GPIO.LOW):
		sayac += 1

	return sayac

while True:
	print sensorOku(23) # 23 nolu GPIO okunsun