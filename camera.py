from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (1920,1080)

camera.framerate = 30
camera.start_preview()
#camera.annotate_text = "PHOTONICS WINDOW"
camera.start_recording('/home/pi/Documents/EC463-Miniproject/adam2.h264')

sleep(5)




# camera.capture('/home/pi/Documents/pic1.jpg')
camera.stop_recording()
camera.stop_preview()
