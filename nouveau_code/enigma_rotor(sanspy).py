#Enigma Encoder - www.101computing.net/enigma-encoder/

# ----------------- Enigma Settings -----------------
#from fmotor import rotor,cran,destroy
import random

rotors = ("I","II","III")
reflector = "UKW-B"
ringSettings ="ABC"
#ringPositions = "TAB"
ringPositions = input("position initiale : ")
ringPositions = ringPositions.upper()
if ringPositions == "":
	ringPositions = "TAB"
#rotor(1,ord(ringPositions[0])-65)
#rotor(2,ord(ringPositions[1])-65)
#rotor(3,ord(ringPositions[2])-65)


plugboard = "AT BS DE FM IR KN LZ OW PV XY"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor1Notch = "Q"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor2Notch = "E"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor3Notch = "V"
rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor4Notch = "J"
rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
rotor5Notch = "Z"

rotorDict = {"I":rotor1,"II":rotor2,"III":rotor3,"IV":rotor4,"V":rotor5}
rotorNotchDict = {"I":rotor1Notch,"II":rotor2Notch,"III":rotor3Notch,"IV":rotor4Notch,"V":rotor5Notch}

reflectorB = {"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
reflectorC = {"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}
# ---------------------------------------------------

def caesarShift(str, amount):
	output = ""

	for i in range(0,len(str)):
		c = str[i]
		code = ord(c)
		if ((code >= 65) and (code <= 90)):
			c = chr(((code - 65 + amount) % 26) + 65)
		output = output + c

	return output

def initialize():
	global rotors, reflector,ringSettings,ringPositions,plugboard,alphabet,rotor1,rotor2,rotor3,rotor4,rotor5,rotor1Notch,rotor2Notch,rotor3Notch,rotor4Notch,rotor5Notch,reflectorB,reflectorC
	global rotorALetter,rotorBLetter,rotorCLetter,rotorA,rotorB,rotorC,rotorASetting,rotorBSetting,rotorCSetting,rotorANotch,rotorBNotch,rotorCNotch
	global reflectorDict
	#Enigma Rotors and reflectors

	rotorANotch = False
	rotorBNotch = False
	rotorCNotch = False

	if reflector=="UKW-B":
		reflectorDict = reflectorB
	else:
		reflectorDict = reflectorC

	#A = Left,  B = Mid,  C=Right
	rotorA = rotorDict[rotors[0]]
	rotorB = rotorDict[rotors[1]]
	rotorC = rotorDict[rotors[2]]
	rotorANotch = rotorNotchDict[rotors[0]]
	rotorBNotch = rotorNotchDict[rotors[1]]
	rotorCNotch = rotorNotchDict[rotors[2]]

	rotorALetter = ringPositions[0]
	rotorBLetter = ringPositions[1]
	rotorCLetter = ringPositions[2]

	rotorASetting = ringSettings[0]
	offsetASetting = alphabet.index(rotorASetting)
	rotorBSetting = ringSettings[1]
	offsetBSetting = alphabet.index(rotorBSetting)
	rotorCSetting = ringSettings[2]
	offsetCSetting = alphabet.index(rotorCSetting)

	rotorA = caesarShift(rotorA,offsetASetting)
	rotorB = caesarShift(rotorB,offsetBSetting)
	rotorC = caesarShift(rotorC,offsetCSetting)

	if offsetASetting>0:
		rotorA = rotorA[26-offsetASetting:] + rotorA[0:26-offsetASetting]
	if offsetBSetting>0:
		rotorB = rotorB[26-offsetBSetting:] + rotorB[0:26-offsetBSetting]
	if offsetCSetting>0:
		rotorC = rotorC[26-offsetCSetting:] + rotorC[0:26-offsetCSetting]





def encode(plaintext):
	global rotors, reflector,ringSettings,ringPositions,plugboard,alphabet,rotor1,rotor2,rotor3,rotor4,rotor5,rotor1Notch,rotor2Notch,rotor3Notch,rotor4Notch,rotor5Notch,reflectorB,reflectorC
	global rotorALetter,rotorBLetter,rotorCLetter,rotorA,rotorB,rotorC,rotorASetting,rotorBSetting,rotorCSetting,rotorANotch,rotorBNotch,rotorCNotch
	global reflectorDict

	ciphertext = ""

	#Converplugboard settings into a dictionary
	plugboardConnections = plugboard.upper().split(" ")
	plugboardDict = {}

	for pair in plugboardConnections:
		if len(pair)==2:
			plugboardDict[pair[0]] = pair[1]
			plugboardDict[pair[1]] = pair[0]

	plaintext = plaintext.upper()
	for letter in plaintext:
		encryptedLetter = letter

		if letter in alphabet:
			#Rotate Rotors - This happens as soon as a key is pressed, before encrypting the letter!
			rotorTrigger = False
			print("rotor 3/C bouge et")
			#cran(1)
			#Third rotor rotates by 1 for every key being pressed
			if rotorCLetter == rotorCNotch:
				rotorTrigger = True

			rotorCLetter = alphabet[(alphabet.index(rotorCLetter) + 1) % 26]



			#Check if rotorB needs to rotate
			if rotorTrigger:
				rotorTrigger = False
				print("rotor 2/B bouge et")
				#cran(2)
				if rotorBLetter == rotorBNotch:
					rotorTrigger = True
					print("rotor 2/B bouge et")
					#cran(2)
				rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]

				#Check if rotorA needs to rotate
				if (rotorTrigger):
					rotorTrigger = False
					print("rotor 1/A bouge et")
					#cran(3)
					rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]

			else:
					#Check for double step sequence!
				if rotorBLetter == rotorBNotch:
					print("rotor 2/B bouge et")
					#cran(2)
					rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
					print("rotor 1/A bouge et")
					#cran(3)
					rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]

			#Implement plugboard encryption!
			if letter in plugboardDict.keys():
				if plugboardDict[letter]!="":
					encryptedLetter = plugboardDict[letter]

			#Rotors & Reflector Encryption
			offsetA = alphabet.index(rotorALetter)
			offsetB = alphabet.index(rotorBLetter)
			offsetC = alphabet.index(rotorCLetter)

			# Wheel 3 Encryption
			pos = alphabet.index(encryptedLetter)
			let = rotorC[(pos + offsetC)%26]
			pos = alphabet.index(let)
			encryptedLetter = alphabet[(pos - offsetC +26)%26]

			# Wheel 2 Encryption
			pos = alphabet.index(encryptedLetter)
			let = rotorB[(pos + offsetB)%26]
			pos = alphabet.index(let)
			encryptedLetter = alphabet[(pos - offsetB +26)%26]

			# Wheel 1 Encryption
			pos = alphabet.index(encryptedLetter)
			let = rotorA[(pos + offsetA)%26]
			pos = alphabet.index(let)
			encryptedLetter = alphabet[(pos - offsetA +26)%26]

			# Reflector encryption!
			if encryptedLetter in reflectorDict.keys():
				if reflectorDict[encryptedLetter]!="":
					encryptedLetter = reflectorDict[encryptedLetter]

			#Back through the rotors
			# Wheel 1 Encryption
			pos = alphabet.index(encryptedLetter)
			let = alphabet[(pos + offsetA)%26]
			pos = rotorA.index(let)
			encryptedLetter = alphabet[(pos - offsetA +26)%26]

			# Wheel 2 Encryption
			pos = alphabet.index(encryptedLetter)
			let = alphabet[(pos + offsetB)%26]
			pos = rotorB.index(let)
			encryptedLetter = alphabet[(pos - offsetB +26)%26]

			# Wheel 3 Encryption
			pos = alphabet.index(encryptedLetter)
			let = alphabet[(pos + offsetC)%26]
			pos = rotorC.index(let)
			encryptedLetter = alphabet[(pos - offsetC +26)%26]

			#Implement plugboard encryption!
			if encryptedLetter in plugboardDict.keys():
				if plugboardDict[encryptedLetter]!="":
					encryptedLetter = plugboardDict[encryptedLetter]

		ciphertext = ciphertext + encryptedLetter

	return ciphertext

def getchar():
	#Returns a single character from standard input
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch



#Main Program Starts Here

print("  ##### Enigma Encoder #####")
print("appuyer sur espace pour quitter\n")
initialize()
""" 
plaintext = input("Enter text to encode or decode:\n")
ciphertext = encode(plaintext)
print("\nEncoded text: \n " + ciphertext) """


while 1:
	plaintext = getchar()
	ciphertext = encode(plaintext)
	if plaintext.strip() == '':
		print('bye!')
		#destroy()
		break
	else:
		print(plaintext+ " devient :" + "\n" + ciphertext +"\n")