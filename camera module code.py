from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
picam2.start()

# Capture an image
picam2.capture_file("image.jpg")

# Wait for the camera to finish
sleep(2)

picam2.stop()

