#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #Board sıralaması değil şematik sıralama
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #23 No'lu pine girişte yüksek voltaj beklemesini söyledik
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) #24 No'lu pine girişte düşük voltaj beklemesini söyledik

while True: #sonsuz döngü

	if(GPIO.input(23) == 1): #eğer 23 nolu pindeki (3.3V besleme alan) tıklanırsa

		print("Birinci butona basildi")

	if(GPIO.input(24) == 0): #eğer 24 nolu pindeki (toprağa bağlı) tıklanırsa

		print("İkinci butona basildi")

GPIO.cleanup()