#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(10, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
