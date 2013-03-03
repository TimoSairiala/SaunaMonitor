import serial
from time import sleep

port = serial.Serial("/dev/ttyUSB0", 57600, timeout=0.5)

while True:
	data = port.read(9999)
	if len(data) > 0:
		print "tallasta: ", data

	sleep( 1 )

port.close()
