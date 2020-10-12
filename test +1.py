from fmotor import rotor,cran,destroy
import time


if __name__ == '__main__':     # Program entrance

	print ('Program is starting...')

	try:
		while True:
			go=input("bouger ?")

			cran(1)
			time.sleep(0.5)
			cran(2)
			time.sleep(0.5)
			cran(3)
			time.sleep(0.5)


	except KeyboardInterrupt:
			destroy()