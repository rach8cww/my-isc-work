print
print "Loops and Slicing Exercise"
print

# part 1

mylist = [1,2,3,4,5]
print mylist[1] # prints 2nd item in the list
print mylist[-2] # prints the 2nd to last item in the list
print mylist[:] # list slicing to select the whole list
print mylist[1:-1] # ist slicing to select 2nd to 4th items

# part 2

one_to_ten = range(1,11) # uses range to create list from 1-10
one_to_ten[0] = 10 # insets 10 at the first item in the list
one_to_ten.append(11) # appends 11 to the end of the list
one_to_ten.extend([12,13,14]) # extends the list to include other items
print one_to_ten

# part 3

forward = [] # empty list
backward = [] # empty list
values = ['a', 'b', 'c'] # list called values

for item in values: # for loop for items in values list
	forward.append(item) # assign items to the forward list
	backward.insert(0,item) # assign items in reverse to backward list

print "forward is ", forward # prints forward list
print "backward is ", backward # prints backward list
wrong = forward[::-1] # reverses the order of forward using slicing
print "reverse forward is ", wrong # prints the reversed forward, "wrong"

# part 4 - not completed...
"""
countries = ['uk', 'usa', ' uk', 'uae']
dir(countries)
help(countries.count)
count countries(uk)
"""
print
















