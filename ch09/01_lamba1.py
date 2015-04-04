#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

#GPIO numaralarına göre hazır et
GPIO.setmode(GPIO.BCM)

#pinleri tanımlayalım
anahtar = 18


#pinlere giriş çıkış ayarlayalım
GPIO.setup(anahtar, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:

	while True:

		#GPIO, toprağa bağlı olduğu için düşük akım bekliyor
		GPIO.wait_for_edge(anahtar, GPIO.FALLING)
		print('aciyor')

		GPIO.wait_for_edge(anahtar, GPIO.RISING)
		print('kapiyor')


except KeyboardInterrupt:
	print('ctrl+c yapmis')

except:
	print('Bir hata var!')

finally:
	GPIO.cleanup()