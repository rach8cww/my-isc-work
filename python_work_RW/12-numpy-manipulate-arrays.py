print
print "Manipulating Numpy Arrays Exercise"
print

import numpy as np # importing the numpy library, with shortcut of np

# part 1 - interrogating arrays to discover properties

# create array with ranges, will have a 2x4 shape (due to number of ranges and range of the ranges)
arr = np.array([range(4), range(10,14)])
print arr

print "shape of arr: ", arr.shape
print "size of arr: ", arr.size # which is the total items in the array
print "max of arr: ", arr.max()
print "min of arr: ", arr.min()

# part 2 - generate new arrays by modifying original arrays

print arr.reshape(2,2,2) # arr re-shaped to 2x2x2 (3D array with 2x2 size)
print np.transpose(arr) # think this just turns from horizontal to vertical
print np.ravel(arr) # flatten array to 1D
print arr.astype(float) # prints the array with floats rather than int)


print 
