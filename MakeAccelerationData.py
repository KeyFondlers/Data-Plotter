import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

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

trial1Velocity = np.diff(trial1[:,1]) / np.diff(trial1[:,0])
trial2Velocity = np.diff(trial2[:,1]) / np.diff(trial2[:,0])
trial3Velocity = np.diff(trial3[:,1]) / np.diff(trial3[:,0])
trial4Velocity = np.diff(trial4[:,1]) / np.diff(trial4[:,0])
trial5Velocity = np.diff(trial5[:,1]) / np.diff(trial5[:,0])
trial6Velocity = np.diff(trial6[:,1]) / np.diff(trial6[:,0])


trial1Acceleration = np.diff(trial1Velocity) / np.diff(trial1[:,0][1:])
trial2Acceleration = np.diff(trial2Velocity) / np.diff(trial2[:,0][1:])
trial3Acceleration = np.diff(trial3Velocity) / np.diff(trial3[:,0][1:])
trial4Acceleration = np.diff(trial4Velocity) / np.diff(trial4[:,0][1:])
trial5Acceleration = np.diff(trial5Velocity) / np.diff(trial5[:,0][1:])
trial6Acceleration = np.diff(trial6Velocity) / np.diff(trial6[:,0][1:])

trend_lines = [
    LinearRegression().fit(trial1[:,0][2:].reshape(-1,1), trial1Acceleration).predict(trial1[:,0][2:].reshape(-1,1)),
    LinearRegression().fit(trial2[:,0][2:].reshape(-1,1), trial2Acceleration).predict(trial2[:,0][2:].reshape(-1,1)),
    LinearRegression().fit(trial3[:,0][2:].reshape(-1,1), trial3Acceleration).predict(trial3[:,0][2:].reshape(-1,1)),
    LinearRegression().fit(trial4[:,0][2:].reshape(-1,1), trial4Acceleration).predict(trial4[:,0][2:].reshape(-1,1)),
    LinearRegression().fit(trial5[:,0][2:].reshape(-1,1), trial5Acceleration).predict(trial5[:,0][2:].reshape(-1,1)),
    LinearRegression().fit(trial6[:,0][2:].reshape(-1,1), trial6Acceleration).predict(trial6[:,0][2:].reshape(-1,1))
]

trend_line = np.mean(trend_lines, axis=0)

plt.plot(trial1[:,0][2:], trial1Acceleration, 'ro', label='Trial 1')
plt.plot(trial2[:,0][2:], trial2Acceleration, 'bo', label='Trial 2')
plt.plot(trial3[:,0][2:], trial3Acceleration, 'go', label='Trial 3')
plt.plot(trial4[:,0][2:], trial4Acceleration, 'yo', label='Trial 4')
plt.plot(trial5[:,0][2:], trial5Acceleration, 'co', label='Trial 5')
plt.plot(trial6[:,0][2:], trial6Acceleration, 'mo', label='Trial 6')

plt.plot(trial1[:,0][2:], trend_line, 'k-', label = "Trend Line")


plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^3)')

plt.title('6 Falling Tennis Ball Trials')

plt.legend(fontsize=8)

plt.show()
