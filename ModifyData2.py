import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = np.loadtxt("data5.txt")

dataLength = len(data)

tmp = []

np.set_printoptions(suppress=True)

#np array of the data
newData = np.array(tmp)

sum = 0

for i in range(0,dataLength):

    sum += data[i,1]

    print(data[i,1])

    tmp.append([data[i,0], sum])

print(np.array(tmp, dtype=float))