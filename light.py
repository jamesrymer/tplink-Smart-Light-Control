from subprocess import call
import subprocess as sub
import os
import time
#Functions to change the light bulb to different colors
def changeToGreen():
    call(["tplight", "hsb", "[Light Bulb IP Here]","99", "100", "100"])
def changeToBlue():
    call(["tplight", "hsb", "[Light Bulb IP Here]","210", "100", "100"])
def changeToRed():
    call(["tplight", "hsb", "[Light Bulb IP Here]","360", "100", "100"])
def changeToYellow():
    call(["tplight", "hsb", "[Light Bulb IP Here]","60", "100", "100"])
def changeToPink():
    call(["tplight", "hsb", "[Light Bulb IP Here]","330", "100", "100"])
def changeToPurple():
    call(["tplight", "hsb", "[Light Bulb IP Here]","270", "100", "100"])


changeToBlue()
time.sleep(2)
changeToGreen()
time.sleep(2)
changeToPink()
time.sleep(2)
changeToRed()
time.sleep(2)
changeToYellow()
time.sleep(2)
changeToPurple()
time.sleep(2)

call(["tplight", "hsb", "[Light Bulb IP Here]"])
while True:
    call(["tplight", "on", "[Light Bulb IP Here]"])
    time.sleep(2)
    call(["tplight", "off", "[Light Bulb IP Here]"])
    time.sleep(2)



