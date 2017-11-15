
print
print "Tuples Exercise" # tuples are 
print

# part 1

t = (1,) # creates a tuple with 1 variable (have to put a comma to make it a 'list'
print t[-1] # uses indexing to print the last value of the tuple (same as first)
numbers = range(100,201) # creates a list of numbers from 100 - 200
tuple(numbers) # tuple(numbers) converts the numbers list to a tuple
print numbers[:1], numbers[-1] # prints the first and last numbers of the tuple

# part 2 - using enumerate function

zoo = ["bear", "panda", "zebra"] # creating a list of animals
# (i,name) is just calling the enumerate, can be anything.
for (i,name) in enumerate(zoo): 
	print i, name

# e.g.
market = ("apples", "pear", "orange") # tuple using () 
for (fruit, stall) in enumerate(market):
	print fruit, stall

# part 3 - multiple values from a list to a tuple

(first, middle, last) = zoo  # tuple with multiple variables assigned to zoo tuple
print first, middle, last # calls out the items in zoo in a set order
print middle, last, first # this allows the order to be re-arranged easily
(first, middle, last) = (middle, last, first) # can re-assign attributes too
print first, middle, last # this is now not the original order


(a, b, c,) = market # can also be used with any character, as long as is a tuple
print a, b, c # the only thing is that the number of variables has to BALANCE!!


print
