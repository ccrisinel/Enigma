from fmotor import rotor,destroy
import random


if __name__ == '__main__':     # Program entrance

	print ('Program is starting...')

	try:
		while True:
			
			rotor(1,int(random.randrange(1,4)))
			
			rotor(2,int(random.randrange(1,4)))
			
			rotor(3,int(random.randrange(1,4)))
			
			

	except KeyboardInterrupt:
			destroy()