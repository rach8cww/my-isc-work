print
print "Scripts and Libraries Exercise"
print

# part 1 - sets

a = set([0, 1, 2, 3, 4, 5]) # creates a set, a
b = set([2, 4, 6, 8]) # creates a set, b

print a.union(b) # conjoins the two, but 2 and 4 don't appear twice as its a set

print a.intersection(b) # prints the numbers where the two sets are the same
print # just making a space in the output

# part 2 - dictionaries

band = ["Mel", "Geri", "Victoria", "Mel", "Emma"] # list
counts = {} # creates an empty dictionary

for member in band: # for every member in the band list:
	if member not in counts: # if member not in counts,
		counts[member] = 1 # add member name with the value "1"
	else: # if the member is already in counts
		counts[member] += 1 # increase the value of the member by 1

for member in counts: # for each member in the counts dictionary
	print member, counts[member] # print the member and the value

# part 3 - altering and calling dictionaries

UK = {"Edinburgh" : "Scotland", "Leeds" : "England"} # new dictionary
if{"Scotland"}: print "Haggis" # calls out whether there is a value or not

print "The items in UK dictionary: ", UK.items()
print "The keys in UK dictionary: ", UK.keys()
print "The values in UK dictionary: ", UK.values()

print UK.get("Edinburgh") # calls out the key and returns the value

UK["Reykjavik"] = "Yceland" # adds a new key and value to the dictionary
UK["Reykjavik"] = "Iceland" # changes the value of a key in the dictionary
print UK









print 
