#imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#function defining the curve fit format.
def objective(x, a, b, c):
    return a * x + b * x**2 + c

#Iterate through each data line
data = []
with open("data.txt") as file:
    #Iterate through each data line
    for line in file:
        #Split data line into a list [x,y]
        dataPoint = line[:-1].split(" ")
        #Converts the data point to floats
        dataPoint = [float(i) for i in dataPoint]
        #Square the y value of the data point
        dataPoint[1] = np.power(dataPoint[1], 2)
        #Add data point to the greater list
        data.append(dataPoint)    

#Covert Python list to numpy array
data = np.array(data)

#Parameter optimization for a quadratic curve based on the scatterplot data
popt, _ = curve_fit(objective, data[:, 0], data[:, 1])

#Split parameter optimization into individual parameters.
a, b, c = popt

#Domain
x_line = np.arange(min(data[:, 0]), max(data[:, 0]), 1)

#Range
y_line = objective(x_line, a, b, c)

#Plot spotted blue trend line from parameter optimization
plt.plot(x_line, y_line, '--', color='blue', label = ("p ≈ " + str(round(a,4)) + "t + " + str(round(b,4)) + "t^2 + " + str(round(c, 4))))

#Generate Scatterplot from squared data
plt.scatter(data[:, 0], data[:, 1], c='r')

#Move trend line legend.
plt.legend(bbox_to_anchor=(0.025, 0.95), loc='upper left', borderaxespad=0)

#Set axis labels and plot title
plt.xlabel("time(t)")
plt.ylabel("meters(p)")
plt.title("Position Squared Plot")

#Export plot to file
plt.savefig("images/Squared Plot.png")