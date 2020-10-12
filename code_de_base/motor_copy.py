#!/usr/bin/env python3
########################################################################
# Filename    : SteppingMotor.py
# Description : Drive SteppingMotor
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)
gpioList = [6,13,19,26]
motorPins = []


for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

# Sleep time variables

sleepTimeShort = 0.1
sleepTimeLong = 0.1

positionzero = 0
position_rounded = []
positionactuel = 0
positionactu26 = 0

CCWStep = (0x01,0x02,0x04,0x08) # define power supply order for rotating anticlockwise 
CWStep = (0x08,0x04,0x02,0x01)  # define power supply order for rotating clockwise

def Fpins(motor_no):
	motorPins = []
	if motor_no == 1:
		motorPins = [18, 23, 24, 25]
	elif motor_no == 2:
		motorPins = [31, 33, 35, 37]
	return motorPins


def setup():    
	global motorPins
	GPIO.setmode(GPIO.BCM)       # use real fucking GPIO Numbering
	for pin in motorPins:
		GPIO.setup(pin,GPIO.OUT)
		
# as for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
def moveOnePeriod(direction,ms):    
	for j in range(0,4,1):      # cycle for power supply order
		for i in range(0,4,1):  # assign to each pin
			if (direction == 1):# power supply order clockwise
				GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
			else :              # power supply order anticlockwise
				GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
		if(ms<3):       # the delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
			ms = 3
		time.sleep(ms*0.001)    



# continuous rotation function, the parameter steps specifies the rotation cycles, every four steps is a cycle
def moveSteps(direction, ms, steps):
	click = True

	GPIO.output(6, GPIO.LOW)
	GPIO.output(13, GPIO.HIGH)


	for i in range(steps):
		moveOnePeriod(direction, ms)
		if i in position_rounded:
			
			if click == True:
				GPIO.output(6, GPIO.HIGH)
				GPIO.output(13, GPIO.LOW)
				click = False
			else:
				GPIO.output(6, GPIO.LOW)
				GPIO.output(13, GPIO.HIGH)
				click = True







# function used to stop motor
def motorStop():
	for i in range(0,4,1):
		GPIO.output(motorPins[i],GPIO.LOW)

def going(go):
		
	global position_rounded
	global positionzero
	global positionactu26

	position = [0.0]

	s=0.0
	for i in range(0,25,1):
		s+=(512/26)
		position.append(s)
	for i in position:
		position_rounded.append(math.trunc(round(i,0)))
	
	print("la position {go} est {position_rounded[go]}")
	

	moveSteps(0,3,position_rounded[go])
	time.sleep(0.5)
	
	
	positionzero += position_rounded[go]
	if positionzero >= 512:
		positionzero %=  512

	positionactu26 += go
	if positionactu26 >= 26:
		positionactu26 %= 26
		

def move():

#        moveSteps(1,3,512)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
#        time.sleep(0.5)
#        moveSteps(0,3,512)  # rotating 360 deg anticlockwise
#        time.sleep(0.5)

	moveSteps(1,100,512)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
	time.sleep(2)

#     moveSteps(1,3,512)  # rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
#     time.sleep(2)

def gochiffre(motor, posititonchiffre):

	global Fpins, motorPins, positionactu26
	
	motorPins = Fpins(motor)

	setup()

	if (posititonchiffre+positionactu26) >= 26:
		posititonchiffre = 26 - positionactu26 + posititonchiffre
		
	else:
		posititonchiffre -= positionactu26
	print(posititonchiffre)
	going(posititonchiffre)	




def destroy():
	moveSteps(0,3,512-positionzero)
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program entrance

	print ('Program is starting...')

	try:
		while True:

			print(positionzero)

			#motor = int(input("Quel moteur voulez-vous utiliser ? "))
			motor = 1
			go = int(input("Sur quelle position ? "))
			#rep = int(input("Combien de fois ? "))
			rep = 1

			motorPins = Fpins(motor)

			setup()

			if (go+positionactu26) >= 26:
				go = 26 - positionactu26 + go
				
			else:
				go -= positionactu26
			print("go is: " + str(go))

			going(go)
			""" 			for i in range(0,rep,1):
				going(go)
				if rep != 1:
					time.sleep(0.5) """

			print(positionzero)
			'''
			goback = input("Voulez-vous revenir a la position initial ? ")
			if goback == "y":
				moveSteps(0,3,512-positionzero)
			elif goback == "r":
				moveSteps(1,3,positionzero)
			'''
	except KeyboardInterrupt:
			destroy()