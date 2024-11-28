import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN)     # Touch sensor (BCM pin 4)
GPIO.setup(18, GPIO.OUT)   # LED (BCM pin 18)

GPIO.setup(4, GPIO.IN)     # Touch sensor (BCM pin 4)
GPIO.setup(18, GPIO.OUT)   # LED (BCM pin 18)

while True:
    if GPIO.input(4):  # If touch detected
        print("LED on")
        GPIO.output(18, GPIO.HIGH)  # Turn LED on
        time.sleep(1)
        print("LED off")
        GPIO.output(18, GPIO.LOW)  # Turn LED off
    else:
        GPIO.output(18, GPIO.LOW)  # Ensure LED is off when no touch
