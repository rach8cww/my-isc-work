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

forward = []
backward = []
values = ['a', 'b', 'c']

print "start"
for item in values:
	forward.append(item)
	backward.insert(0,item)

print "forward is ", forward
print "backward is ", backward
wrong = forward[::-1]
print "reverse forward is ", wrong



print
