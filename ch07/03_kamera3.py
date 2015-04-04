import time
import picamera

camera = picamera.PiCamera()
time.sleep(1)
camera.start_recording('arda.h264')
time.sleep(5)
camera.stop_recording()
camera.close()