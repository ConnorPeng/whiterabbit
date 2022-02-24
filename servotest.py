from gpiozero import Servo,AngularServo
from time import sleep


servo = AngularServo(17, min_angle = 0, max_angle = 180, min_pulse_width = 0.0006, max_pulse_width = 0.0024)
try:
    while True:
        
        servo.value = val
        sleep(0.3)
        val = val + 0.1
        if val >1:
            val = -1
except KeyboardInterrupt:
    print("stop")