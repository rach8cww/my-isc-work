
print
print "Temperature Test 1"
print


import serial, io # imports the library needed to run the serial_port (plug in)
from datetime import datetime
#import io

# these are the device parameters which need to be set correctly
ser = serial.Serial( 
	port = '/dev/ttyUSB0', # the name of the port (USB port 1)
	baudrate = 9600, # rate at which info is transferred
	bytesize = serial.EIGHTBITS, # the amount of data being sent
	parity = serial.PARITY_NONE, # error checks on the data (none here)
	stopbits = serial.STOPBITS_ONE) # gap in data being sent (about 10 s)

# this is to read the data and print, 8 is specific to the instrument
#print ser.read(size=8) 

# reading the data with the time input as well.
#date_time = datetime.utcnow().isoformat(),ser.read(size=8)
#print date_time

#  different time-format (easier to read)
#date_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),ser.read(size=8)
#print date_time

# part 4 - difference between data and time-stamp

# time stamp seperate from instrument - can be a lag between both
#date_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
#print date_time
#print ser.read(size=8) 

# part 5 - adding a loop to continuously read the data

#while ser.isOpen(): # while loop
#	datastring = ser.read(size=8) # sets the data-string
#	print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),datastring
# (above): sets to print the time and the data string while the loop runs.

# part 6 - using readline()

# sets the parameters 
#sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1), encoding='ascii',newline='\r')

#while ser.isOpen(): # while loop using the sio function
	#datastring = sio.readline() # sets the data-string
	#print datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),datastring

# part 7 - reading out into a file

outfile = '/tmp/serial-temperature-trial1.tsv'

sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1), encoding='ascii',newline='\r')

with open(outfile, 'a') as f: # appends to existing file
	while ser.isOpen(): # runs the loop to keep putting the record in the file
		datastring = sio.readline() # sets the data input
		f.write(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + '\t' + datastring + '\n') # records the date/time and the data at the same time
		f.flush() # included to force the system to write to the file

ser.close()


print
