#Imports
import numpy as np
import matplotlib.pyplot as plt

#Iterate through each data line
data = []
with open("data.txt") as file:
    #Iterate through each data line
    for line in file:
        #Split data line into a list [x,y]
        dataPoint = line[:-1].split(" ")
        #Converts a data point to numbers and adds it to the overall data list
        data.append([float(i) for i in dataPoint])

#Covert Python list to numpy array
data = np.array(data);

#Get line parameters with the equation y=ax+b that fit the data
a, b = np.polyfit(data[:, 0], data[:, 1], 1)

#Generate red scatterplot from data
plt.scatter(data[:, 0], data[:, 1], c='r')

#Plot a blue dotted trend line from polyfit parameters
plt.plot(data[:, 0], a * data[:, 0] + b, "--", color='blue', label = ("p ≈ " + str(round(a,4)) + "t + " + str(round(b,4))))

#Move the trend line legend
plt.legend(bbox_to_anchor=(0.3, 0.95), loc='upper left', borderaxespad=0)

#Set axis labels and plot title
plt.xlabel("time(t)")
plt.ylabel("meters(p)")
plt.title("Position Plot")

#Export plot to file
plt.savefig("images/Normal Plot.png")