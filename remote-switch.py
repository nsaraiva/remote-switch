#!/usr/bin/python

'''
__date__ = "2014-07-15"
__author__ = "Nelson Saraiva" 
__version__ = "0.1"
'''

import serial   #Import the serial library
import json
import time
import urllib2

# Open the serial port
# Do not forget to check what port the Arduino is connected
ser = serial.Serial("COM23", 9600)

def arduino_is_ready():
    #Boolean variable that shows if arduino is ready
    ready = False
    
    #loop until the arduino tell us if is ready
    while not ready:
        print "Connecting..."
        serin = ser.readline()
        ready = True
        print "Connected"
    send_command()

def send_command():

	estado = "off"
	while True:
		action = json.load(urllib2.urlopen("your API URL here"))
		if "on" in action["action"][0]["command"] and estado != "on":
			print "on"
			led13("on")
			estado = "on"
		elif "off" in action["action"][0]["command"] and estado != "off":
			print "off"
			led13("0ff")
			estado = "off"
		time.sleep(1)
		
def led13(flag):
	ser.write(flag)
		
if __name__ == "__main__":
    arduino_is_ready()

    # Close the port and end the program
    ser.close() 
