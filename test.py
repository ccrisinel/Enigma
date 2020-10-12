#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [6,13,19,26]

# loop through pins and set mode default state is 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
   


# active each relay for 2 seconds with 2 second delay between each activation

try:
	while True:

		for i in pinList: 
			GPIO.output(i, GPIO.HIGH)
			print(i), " on"
			time.sleep(0.15)
		time.sleep(0.6)
		for i in pinList:
			GPIO.output(i, GPIO.LOW)
			print(i), " off"
			#time.sleep(0.1)
except KeyboardInterrupt:

	print("extinction")
	# Reset GPIO settings
	for i in pinList:
			GPIO.output(i, GPIO.LOW)
			print(f"{i} off")
	GPIO.cleanup()
	