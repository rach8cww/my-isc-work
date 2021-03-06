print
print "Multiple Plots/Axes Exercise"
print

import matplotlib.pyplot as plt # imports pyplot as plt

# part 1 - multiple axes:

fig, ax1 = plt.subplots() # sets up the idea of x2 axes
time = (range(7)) # sets the time
co2 = (250, 265, 272, 260, 300, 320, 389) # sets data for co2
ax1.plot(time,co2, 'b--') # plots data on axes 1
ax1.set_ylabel('CO2 Concentration (ppm)') # sets axes 1 label
ax1.set_xlabel('Time (Decades)') # sets x axes
ax2 = ax1.twinx() # gets a second axes
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2] # sets temp data
ax2.plot(time,temp,'r*-') # plots 2nd axes
ax2.set_ylabel('Temperature (C)') # sets 2nd axes label
plt.title('Temperature and CO2') # sets title
plt.pause(10) # plt.plot()

# part 2 - subplots

# defines that this plot will be on line 1 with 3 plots and this is the first one:
plt.subplot(1, 3, 1) 
x = range(0, 10, 1) # the data to be plotted
plt.title('Plot 1')
plt.ylabel('Temperature (C)') 
plt.xlabel('Time (Decades)') # sets x axes
plt.plot(x) # plots the data x

# defines that this plot will be on line 1 with 3 plots and this is the 2nd one:
plt.subplot(1, 3, 2)
y = range(10, 0, -1)# the data to be plotted
plt.title('Plot 2')
plt.ylabel('CO2')
plt.xlabel('Time (Decades)') # sets x axes
plt.plot(y)# plots the data y

# defines that this plot will be on line 1 with 3 plots and this is the 3rd one:
plt.subplot(1, 3, 3)
z = [4] * 10# the data to be plotted
plt.title('Plot 3')
plt.ylabel('H2S')
plt.xlabel('Time (Decades)') # sets x axes
plt.plot(z)# plots the data z
plt.pause(10) # shows all of the plots

print

"""
NOTES:


plt.figure # multiple plots
plt.plot(times, [0,1,5,3], 'g--', label = "same data")
plt.plot(times, [1,2,5,6], 'r', label = "other data")
plt.ylabel("Concentration (%)")
plt.xlabel('Time (s)')
plt.title('Concentration of Chlorine vs. Time')
plt.legend()
plt.savefig("Plot 1.png")
plt.figure(figsize = (10,10))
#plt.pause(5)
"""
