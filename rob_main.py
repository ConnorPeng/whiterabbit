import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
print("setup")

while True:
    if GPIO.input(23) == GPIO.HIGH:
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        print("test mode")
    elif GPIO.input(24) == GPIO.HIGH:
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)
        print("normal mode")
    else:
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)
        print("idle")
        