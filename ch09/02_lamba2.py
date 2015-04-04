#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time #beklemeler içim lazım

#GPIO numaralarına göre hazır et
GPIO.setmode(GPIO.BCM)

#pinleri tanımlayalım
anahtar = 18
kirmizi = 23
sari    = 24
yesil   = 25

#pinlere giriş çıkış ayarlayalım
GPIO.setup(anahtar, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(kirmizi, GPIO.OUT, pull_up_down = GPIO.PUD_UP)
GPIO.setup(sari, GPIO.OUT, pull_up_down = GPIO.PUD_UP)
GPIO.setup(yesil, GPIO.OUT, pull_up_down = GPIO.PUD_UP)

#durum sıfırlama fonksiyonu
def sifirla():
	GPIO.output(kirmizi,GPIO.LOW)
	GPIO.output(sari,GPIO.LOW)
	GPIO.output(yesil,GPIO.LOW)

#kırmızı ışıktan yeşile geçiş
def kirmizidanYesile():
	print('kirmizidan yesile donuyor..')
	sifirla()
	GPIO.output(kirmizi,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(sari,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(kirmizi,GPIO.LOW)
	GPIO.output(sari,GPIO.LOW)
	GPIO.output(yesil,GPIO.HIGH)

#yeşil ışıktan kırmızıya geçiş
def yesildenKirmiziya():
	print('yesilden kirmiziya donuyor..')
	sifirla()
	GPIO.output(yesil,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(yesil,GPIO.LOW)
	GPIO.output(sari,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(sari,GPIO.LOW)
	GPIO.output(kirmizi,GPIO.HIGH)

try:

	#açınca bi durumları sıfırlasın
	sifirla()

	while True:

		#GPIO, toprağa bağlı olduğu için düşük akım bekliyor
		GPIO.wait_for_edge(anahtar, GPIO.FALLING)
		kirmizidanYesile()

		GPIO.wait_for_edge(anahtar, GPIO.RISING)
		yesildenKirmiziya()

except KeyboardInterrupt:
	print('ctrl+c yapmis')

except:
	print('Bir hata var!')

finally:
	GPIO.cleanup()