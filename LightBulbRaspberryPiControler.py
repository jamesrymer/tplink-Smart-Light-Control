
import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

HU = 16
HD = 7
SU = 32
SD = 11
BU = 36
BD = 15

sleepTime = 1.5

GPIO.setup(HU,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SU,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BU,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(HD,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SD,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BD,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

hue = 180
saturation = 100
brightness = 100

def changeLightSettings():
	call(["tplight", "hsb", "[Light Bulb IP Here]",str(hue), str(saturation), str(brightness)])

#arr = [["99","100","100"],["210", "100", "100"],["360", "100", "100"], ["60", "100", "100"]]
##arrlength = len(arr)
call(["tplight", "hsb", "[Light Bulb IP Here]","99", "100", "100"])
count = 0

while True:
	inputStateHU = GPIO.input(HU)
	inputStateHD = GPIO.input(HD)
	inputStateSU = GPIO.input(SU)
	inputStateSD = GPIO.input(SD)
	inputStateBU = GPIO.input(BU)
	inputStateBD = GPIO.input(BD)

	
	if inputStateHU == 1:
		#print("tplight ip hsb " + arr[count % arrlength][0] + arr[count % arrlength][1] + arr[count % arrlength][2])
		hue += 36
		changeLightSettings()
		print( hue)
		time.sleep(sleepTime)

	elif inputStateHD == 1:
		hue -= 36
		changeLightSettings()
		print( hue)
		time.sleep(sleepTime)

	elif inputStateSU == 1:
		saturation += 10
		changeLightSettings()
		print(saturation)
		time.sleep(sleepTime)	

	elif inputStateSD == 1:
		saturation -= 10
		changeLightSettings()
		print(saturation)
		time.sleep(sleepTime)	

	elif inputStateBU == 1:
		brightness += 10
		changeLightSettings()
		print(brightness)
		time.sleep(sleepTime)	

	elif inputStateBD == 1:
		brightness -= 10
		changeLightSettings()
		print(brightness)
		time.sleep(sleepTime)











