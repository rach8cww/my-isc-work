print
print "Missing Values and Mased Numpy Arrays Exercise"
print

import numpy as np # importing the numpy library, with shortcut of np
import numpy.ma as MA # importing the masked array library

"""
Can be used in arrays where you have bad data. The fill value is what will be used if you export data and will replace the 'masked' value (so its not blanked out). This should be set to an easily recognisable number (e.g. -999) so that you can easily spot that that data point is bad in the exported file.
"""

# part 1 - creating a masked array

# creates an array with values 0-9, with a fill value of -999. 
marr = MA.masked_array(range(10), fill_value = -999)
print marr
print marr.fill_value

marr[2] = MA.masked # masks (blanks-out) the 3rd value in marr
print marr

# if you print the mask, then the "blanked-out" value is true, all else is false
print marr.mask 

# creates a new array the same as marr (so 3rd blanked out), but also where all values > 6 are also masked
ARR = MA.masked_where(marr > 6, marr) # "where marr > 6" meaning, mask all <7
print ARR
print ARR.fill_value # the fill value is still that of marr (-999)

# setting up an array (x) which will print the fill_value in the masked areas
x = MA.filled(ARR)
print x

# part 2 - creating a mask smaller than the array

m1 = MA.masked_array(range(1,9)) # making an array which has the mask feature
print m1 # nothing is yet masked

m2 = m1.reshape(2,4) # re-shaping m1 so that the array has a different format
print m2

m3 = MA.masked_greater(m2, 6) # masks everything greater than 6
print m3

print m3 * 100 # also seems to multiply the mask number, so all >600 are masked

m4 = m3 - np.ones((2,4)) # subtracting an array of 0s from m3
print m4 # this seems to give m1 but with floats rather than int.
print type(m4) # returns: <class 'numpy.ma.core.MaskedArray'>



print
