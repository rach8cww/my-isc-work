print
print "NetCDF4 Exercise"
print

import netCDF4

# part 1

ds = netCDF4.Dataset("ggas2014121200_00-18.nc") # loading the file (in same directory)

for v in ds.variables: # loop through file and print the IDs (the values of dictionary)
	print v

sst = ds.variables["SSTK"] # assigning SSTK to the ID values
print sst

for d in sst.dimensions: # finding the variable dimensions
	print d, len(ds.variables[d])

print "SST-shape: ", sst.shape # printing the array shape
print "SST-size: ", sst.size # printing the size

for attr in sst.ncattrs(): # getting the names of the attributes
	print attr, "=", getattr(sst, attr)

# part 2

arr = sst[1, 0, 10:20, 30:35] # takes a slice of sst and assigns to arr
print type(arr) # returns <class 'numpy.ma.core.MaskedArray'>

dims = sst.dimensions # dimensions of sst into dims
print "dimensions: ", dims

vars = ds.variables # assigns a variables to vars dictionary
arr_time = vars['time'][1] # sets time variables within vars dictionary
arr_level = vars['surface'][0] # sets level variables within vars dictionary
arr_lats = vars['latitude'][10:20] # sets lat variables within vars dictionary
arr_lons = vars['longitude'][30:35] # sets lon variables within vars dictionary

metadata = {} # empty dictionary - "metadata"

# loops through the netCDF variables sst and prints to the metadata dictionary:
for attr in sst.ncattrs(): 
	metadata[attr] = getattr(sst, attr)

print metadata

print
