import RPi.GPIO as GPIO

#enter your relay pin here
relayPin = 23

#setup pin numbering
GPIO.setmode(GPIO.BCM)
#setup the relay pin as output
GPIO.setup(relayPin, GPIO.OUT)
