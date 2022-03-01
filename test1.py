from gpiozero import Servo,AngularServo
from time import sleep
from pygame import mixer

mixer.init()
sound = mixer.Sound("/home/pi/Downloads/sample3.wav")
sound.play()


servo = AngularServo(17, min_angle = 0, max_angle = 180, min_pulse_width = 0.0006, max_pulse_width = 0.0024)


try:
    while True:
        servo.min()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.max()
        sleep(0.5)
except KeyboardInterrupt:
    print("stop")