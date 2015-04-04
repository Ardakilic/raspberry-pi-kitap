#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO # GPIO kutuphanesini ice aktar
GPIO.setmode(GPIO.BOARD) #Board uzerindeki numaralandirma gecerli olsun
GPIO.setup(16, GPIO.OUT) #16 nolu board pinini out moda al
GPIO.output(16,False) #16 nolu board pinini aktif et