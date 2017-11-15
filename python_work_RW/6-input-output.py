print
print "Input/Output Exercise" 
print

# part 1 - opening weather.csv file

with open ('weather.csv', 'r') as rain: # opens the file as 'read-only'
	data = rain.read() # calls out the file under variable rain and reads it
	print data # prints the data

# part 2 - reading the file line by line

with open ('weather.csv', 'r') as rainy:
	line  = rainy.readline() # uses .readline()
	while line: # while there is still data to read
		print line # print the line		
		line = rainy.readline() # need to re-iterate here so it goes beyond just line 1.
		
print "That's the end of the data"

# part 3 - using a loop and collecting just rainfall values

with open ('weather.csv', 'r') as rainfall:
	header = rainfall.readline() # this reads and discards the first line of the data (we dont want to use the header line with the text in it
	droplet = [] # creating an empty list to store rainfall data
	for line in rainfall.readlines(): 
# readlines reads the whole file, readline just takes the first line	
		r = line.strip() .split(',')[-1] # takes last variable, see below
		r = float(r) # make it a float (with decimals)
		droplet.append(r) # append r to droplet list (store the data)

print droplet # prints the data for rainfall

with open ('myrain.txt', 'w') as writing: # creates a text file with the result
	for r in droplet: # prints the rainfall results in the text file
		writing.write(str(r) + '\n')

"""
Explantation for r = line.strip() .split(',')[-1]

one line as example: 2014-01-01,00:00,2.34,4.45\n

line.strip() removes the \n, so takes just one line without the paragraphing

.split(',') splits the list by the comma, and takes each as a seperate item

.split(',')[-1] means, seperate out and then take the last item

"""

print
