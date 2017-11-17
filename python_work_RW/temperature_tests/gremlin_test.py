#!/usr/bin/python2.7

import serial,io
from datetime import datetime

outfile='/home/user01/my-isc-work/python_work_RW/temperature_tests/temps.tsv'

ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE
)

sio=io.TextIOWrapper(
	io.BufferedRWPair(ser,ser,1),
	encoding='ascii',newline='\r'
)

with open(outfile,'a') as f:
	while ser.isOpen():
		datastring=sio.readline()
		#temp=ser.read(8)
		timestamp=datetime.utcnow().isoformat().replace('T',' ')
		f.write(timestamp+'\t'+datastring+'\n')
		f.flush()
	
	#print datetime.datetime.now('%Y-%m-%d %H:%M:%s'),temp
ser.close()
