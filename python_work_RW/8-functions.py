print
print "Functions Exercise"
print

# part 1

def double_it(number): # a definition with 1 argument
	print 2 * number # prints the argument * 2

double_it(5) # calling and testing the defintion with an intiger
double_it(3.0) # calling and testing the definition with a float
double_it("Smile") # calling and testing the definition with a string

# part 2 - calculating the hypotenuse

def calc_hypo (a, b): # a defintion with two arguments
	hypo = (a**2 + b**2)**0.5 # the calculation for the hypotenuse
	return hypo # returns the answer

print "hypotenuse: ", calc_hypo(3,4) # calls out the function with arguments

# part 3 - checks on the def function to make sure the arguments are good

def calc_hypo (a, b): # a defintion with two arguments
	if type(a) not in (int, float) or type(b) not in (int, float):
# checks that a and b arguments are integers/floats and not strings
		print "Bad Argument" # if string, returns "bad argument"
		return False
	elif a <= 0 or b <= 0: # checks that a and b are > 0
		print "Bad Argument" # if <=0, returns "bad argument"
		return False
	else: # otherwise, goes through the system and calculates the hypo.
		hypo = (a**2 + b**2)**0.5 # the calculation for the hypotenuse
		return hypo # returns the answer

print "hypotenuse: ", calc_hypo(-8,2)























print
