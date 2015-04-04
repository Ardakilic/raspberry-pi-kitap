#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time #beklemeler içim lazım

#GPIO numaralarına göre hazır et
GPIO.setmode(GPIO.BCM)

#pin'i tanımlayalım
led = 23

#GPIO üzerinden bu led'e output vereceğimiz (yakıp söndürme, akım verme vs) için
#bu pin GPIO.OUT olarak tanımlı
GPIO.setup(led, GPIO.OUT, pull_up_down = GPIO.PUD_UP)

mors = {
	' ': ' ',
	"'": '.----.',
	'(': '-.--.-',
	')': '-.--.-',
	',': '--..--',
	'-': '-....-',
	'.': '.-.-.-',
	'/': '-..-.',
	'0': '-----',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.',
	':': '---...',
	';': '-.-.-.',
	'?': '..--..',
	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--.',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',
	'_': '..--.-'
}

#şimdi de nokta ve çizgiyi tanımlamalıyız:
def nokta():
	GPIO.output(led,1)
	time.sleep(0.2)
	GPIO.output(led,0)
	time.sleep(0.2)

def cizgi():
	GPIO.output(led,1)
	time.sleep(0.4)
	GPIO.output(led,0)
	time.sleep(0.2)


while True:

	giris = raw_input('bir metin girin: ')
	for harf in giris:
		for sembol in mors[harf.upper()]:
			#eğer sembol çizgi ise
			if sembol == '-':
				cizgi()
			#eğer sembol nokta ise
			elif sembol == '.':
				nokta()
			#sembol başka bir şey ise
			else:
				time.sleep(0.2)

		#harfler arası 0.5 saniye bekle
		time.sleep(0.5)