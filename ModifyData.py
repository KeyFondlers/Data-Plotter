import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = np.loadtxt("VelocityData.txt")

dataLength = len(data)

tmp = []

np.set_printoptions(suppress=True)

#np array of the data
newData = np.array(tmp)

for i in range(1,dataLength):
    
    #Get the time difference between the current and next data point
    timeDifference = data[i,0] - data[i-1,0]
    
    #Get the mass difference between the current and next data point
    massAvg = (data[i,1] + data[i-1,1])/2
    
    #Add the velocity data point to the new data
    tmp.append([data[i,0], massAvg * timeDifference])

print(np.array(tmp, dtype=float))