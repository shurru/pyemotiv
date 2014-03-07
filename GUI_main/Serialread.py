import serial 


ser= serial.Serial(6, baudrate= 56000, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)

for t in xrange (0, 1000):
	x= ser.read(size=17) #17 bytes transmit the the data carried by the 6 channels. need to focus on bytes 5-8
	print "Serial: %r" %x

	# print len(x)

	

ser.close()