print
print "Numpy Arrays Exercise"
print

import numpy as np # importing the numpy library, with shortcut of np

# part 1 - creating numpy arrays from lists

x = range(1, 11) # making a list with values 1 - 10
a1 = np.array(x) # turning the list into a 1D array
a2 = np.array(x, np.float) # turns x into a 1D array with floats rather than int.
print "a1 array: ", a1, a1.dtype # printing a1 array and data-type
print "a2 array: ", a2, a2.dtype # printing a2 array and data-type

# part 2 - creating different types of arrays
"""
In this section, we are essentially creating the shapes of the arrays we want,
but not inputting any values of data. This will be done later in exericses
"""

box = np.zeros((3,4)) # creates an array of zeros, 3 by 4 in size (2D)
print box 

print
boxes = np.ones((2,3,4)) 
# creates an array of ones, 3 by 4 (3D, which appears as 2 arrays)
print boxes 

boxed = np.arange((1000)) # creates an array with values of 0 - 1000
print boxed

# part 3 - indexing and slicing arrays

list = [2, 3.2, 5.5, -6.4, -2.2, 2.4] # a list with floats and integers
z = np.array(list) # creating an array from the list
print z 

print "z[1]: ", z[1] # finds the 2nd item (1D array only so no coordinates needed)
print "z[1:-2]: ", z[1:5] # slices the array up

m = np.array([[2 ,3.2, 5.5, -6., -2.2, 2.4], # creates a 2D array with this data
		[1, 22, 4, 0.1, 5.3, -9],
		[3, 1, 2.1, 21, 1.1, -2]])
print m

print "m[:, 3]= ", m[:, 3] # slices in all rows to give the 4th item in each

# gives row 2, first to 4th item, and then row 3, first to 4th item:
print "m[1:4, 0:4]= ", m[1:4, 0:4] 

print "m[1:, 2]= ", m[1:, 2] # gives 3rd item in 2nd and 3rd rows


print  


