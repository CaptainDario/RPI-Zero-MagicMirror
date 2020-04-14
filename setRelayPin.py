import RPi.GPIO as GPIO

#enter your relay pin here
relayPin = 23

#setup pin numbering
GPIO.setmode(GPIO.BCM)
#setup the relay pin as output
GPIO.setup(relayPin, GPIO.OUT)
#turn on the relay to see the boot up process
GPIO.output(relayPin, GPIO.HIGH)
