import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def fit_quadratic_ac(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    
    A = np.vstack([x**2, np.ones(len(x))]).T
    a, c = np.linalg.lstsq(A, y, rcond=None)[0]
    
    return a, c

def plot_quadratic(a, b, c):
    
    x_vals = np.linspace(x.min(), x.max(), 100)
    y_vals = a * x_vals**2 + b * x_vals + c
    
    plt.plot(x_vals, y_vals, 'k-', label= "y = " + str(a) +"x^2")


# Example data files]
trial1 = np.loadtxt("stacked-data/Trial1.txt")
trial2 = np.loadtxt("stacked-data/Trial2.txt")
trial3 = np.loadtxt("stacked-data/Trial3.txt")
trial4 = np.loadtxt("stacked-data/Trial4.txt")
trial5 = np.loadtxt("stacked-data/Trial5.txt")
trial6 = np.loadtxt("stacked-data/Trial6.txt")

trial1[:, 1] = trial1[:, 1] - 0.28
trial2[:, 1] = trial2[:, 1] - 0.28
trial3[:, 1] = trial3[:, 1] - 0.28
trial4[:, 1] = trial4[:, 1] - 0.28
trial5[:, 1] = trial5[:, 1] - 0.28
trial6[:, 1] = trial6[:, 1] - 0.28

averageTrial = (trial1 + trial2 + trial3 + trial4 + trial5 + trial6) / 6

a, c = fit_quadratic_ac(averageTrial)

print(a, c)


# Plotting the data
x1, y1 = zip(*trial1)
x2, y2 = zip(*trial2)
x3, y3 = zip(*trial3)
x4, y4 = zip(*trial4)
x5, y5 = zip(*trial5)
x6, y6 = zip(*trial6)
xA, yA = zip(*averageTrial)

#Gravity Line
x = np.linspace(0, 0.6, num=1000)
y = -9.81 * x**2

plt.plot(x1, y1, 'ro-', label='Trial 1')
plt.plot(x2, y2, 'bo-', label='Trial 2')
plt.plot(x3, y3, 'go-', label='Trial 3')
plt.plot(x4, y4, 'yo-', label='Trial 4')
plt.plot(x5, y5, 'co-', label='Trial 5')
plt.plot(x6, y6, 'mo-', label='Trial 6')

plt.plot(x,y, 'k-', label='y=-9.81x^2')

plot_quadratic(a, 0, 0)

plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')

plt.title('6 Falling Tennis Ball Trials')

plt.legend()
plt.show()
