import time
import picamera

camera = picamera.PiCamera()
time.sleep(1)
camera.capture('arda.jpg')
camera.close()