
with open ('/tmp/serial-temperature.tsv', 'r') as temp:
	line  = temp.readline() # uses .readline()
	while line: # while there is still data to read
		print line # print the line		
		line = temp.readline() # need to re-iterate here so it goes beyond
