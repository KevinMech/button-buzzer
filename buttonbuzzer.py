import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(11, GPIO.OUT)

buzz = GPIO.PWM(11, 300)
while(True):
    if GPIO.input(16) == 0:
        buzz.start(1)
    else:
        buzz.stop(0)
    time.sleep(0.1)
