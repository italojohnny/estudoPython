import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

button = 18
led_red = 16
led_yellow = 15
led_green = 13
count = 0

GPIO.setup(button, GPIO.IN)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

while True:
    if GPIO.input(button):
        count = count +1
        time.sleep(0.2)

    if count == 1: GPIO.output(led_red, GPIO.HIGH)
    if count == 2: GPIO.output(led_yellow, GPIO.HIGH)
    if count == 3: GPIO.output(led_green, GPIO.HIGH)

    if count == 4:
        count = 0
        GPIO.output(led_red, GPIO.LOW)
        GPIO.output(led_yellow, GPIO.LOW)
        GPIO.output(led_green, GPIO.LOW)

