import RPi.GPIO as GPIO
from gpiozero import Servo,AngularServo
from time import sleep
from pygame import mixer

mixer.init()
servo = AngularServo(17, min_angle = 0, max_angle = 180, min_pulse_width = 0.0006, max_pulse_width = 0.0024)




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
        # outout sound
        sound = mixer.Sound("/home/pi/Downloads/sample3.wav")
        sound.play()
        #servo movement
        servo.min()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.max()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.min()

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
        