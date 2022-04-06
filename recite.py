# File: recite.py
# ECE 3872 Spring 2022 Wonderland Project
# Author: Navneet Lingala
# Robot Program for Decoding and Processing
# Students must complete this program to process their scripts
# An example has been provided below.

import os
import RPi.GPIO as GPIO
from gpiozero import Servo,AngularServo
from time import sleep
from pygame import mixer

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
servo = AngularServo(17, min_angle = 0, max_angle = 180, min_pulse_width = 0.0006, max_pulse_width = 0.0024)

mixer.init()



SERVER_DATA_PATH = r'/Users/pengjinghong/Desktop/whiterabbit-code/server'    # MODIFIABLE: Change robot data path as needed.
SCRIPTS = 1    # MODIFIABLE: Change number of files expected to be received by Director.

# reads file on cue
# Other computation can be coded here
import gtts
from playsound import playsound

def main():
    tts = gtts.gTTS("Hello world")
    
    count = 1
    read = []
    # Directory will be continuously polled for new files until
    # the number of files dictated by SCRIPTS has been polled.
    while count <= SCRIPTS:
        if not os.listdir(SERVER_DATA_PATH):
            continue
        files = os.listdir(SERVER_DATA_PATH)[0]
        if files not in read:
            # Some code has been written to get you started
            # *********** Your code goes here *********** # 
            print("read successfully1")
            read.append(files)
            count = count + 1
            with open('./server/test.txt', encoding='utf8') as f:
                lines = f.readlines()
            tts = gtts.gTTS(lines[0])
            tts.save("hello.mp3")
            playsound("hello.mp3")
            servo.min()
            sleep(0.5)
            servo.mid()
            sleep(0.5)
            servo.max()
            sleep(0.5)
            servo.mid()
            sleep(0.5)
            servo.min()


            # *********** Your code goes here *********** #
    
    
    print("End Of Wonderland")


# Script to call main function
if __name__ == "__main__":
    main()
