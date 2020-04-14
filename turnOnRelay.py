import RPi.GPIO as GPIO

#enter your relay pin here
relayPin = 23

#set GPIO mode
GPIO.setmode(GPIO.BCM)

#set relaypin to otuput mode
GPIO.setup(relayPin, GPIO.OUT)

#turn off the relay
GPIO.output(relayPin, 0)
