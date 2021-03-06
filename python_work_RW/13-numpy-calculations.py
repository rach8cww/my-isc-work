print
print "Calculations and Operations on Numpy Arrays Exercise"
print

import numpy as np # importing the numpy library, with shortcut of np

# part 1 - array calculations

a = np.array([range(4), range(10,14)]) # creating an array 2x4 with ranges
b = np.array([2, -1, 1, 0]) # creating an array from a list

# multiples the array by each other, 1st line of a * b, then the 2nd line of a * b
multiply = a * b 

b1 = b * 1000 # creates a new array with every item in b * 1000
b2 = b * 1000.0 # creates new array similar to b1 but with floats rather than int
b2 == b1 # yes, this is True. b2 is a float but they are the same
print b1.dtype, b2.dtype # how to print the type of each

# part 2 - array comparisons

arr = np.array([range(10)]) # creates an array with items 0 to 9
print arr < 3 # prints true and false values in the array where item is <3
print np.less(arr, 3) # exactly the same as above, just different format of asking

# sets a condition to call true or false based on two parameters, <3 OR > 8
condition = np.logical_or(arr < 3, arr > 8)
print "condition: ", condition

# uses "where" function to create new array where value is arr*5 if "condition" is true, and arr*-5 where "condition" is false
new_arr = np.where(condition, arr * 5, arr * -5)

# part 3 - mathematical functions working on arrays

"""
Calculating magnitudes of wind, where a minimum acceptable value is 0.1, and all values below this are set to 0.1. Magnitude of wind is calculated by the square-root of the sum of the squares of u and v (which are east-west and north-south wind magnitudes)
"""

def calcMagnitude(u, v, minmag = 0.1): # these are the argument criteria
	mag = ((u**2) + (v**2))**0.5 # the calculation
# sets a where function so that minmag is adopted where values are less than 0.1:
	output = np.where(mag > minmag, mag, minmag) 
	return output

u = np.array([[4, 5, 6],[2, 3, 4]]) # the east-west winds
v = np.array([[2, 2, 2],[1, 1, 1]]) # the north-south winds
print calcMagnitude(u,v) # calls the argument with the u and v arrays

# testing on different wind values, these values use the minmag clause
u = np.array([[4, 5, 0.01],[2, 3, 4]]) # the east-west winds
v = np.array([[2, 2, 0.03],[1, 1, 1]]) # the north-south winds
print calcMagnitude(u,v) # calls the argument with the u and v arrays


print
