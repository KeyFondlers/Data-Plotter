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

trend_lines = [
    LinearRegression().fit(trial1[:,0][1:].reshape(-1,1), trial1Velocity).predict(trial1[:,0][1:].reshape(-1,1)),
    LinearRegression().fit(trial2[:,0][1:].reshape(-1,1), trial2Velocity).predict(trial2[:,0][1:].reshape(-1,1)),
    LinearRegression().fit(trial3[:,0][1:].reshape(-1,1), trial3Velocity).predict(trial3[:,0][1:].reshape(-1,1)),
    LinearRegression().fit(trial4[:,0][1:].reshape(-1,1), trial4Velocity).predict(trial4[:,0][1:].reshape(-1,1)),
    LinearRegression().fit(trial5[:,0][1:].reshape(-1,1), trial5Velocity).predict(trial5[:,0][1:].reshape(-1,1)),
    LinearRegression().fit(trial6[:,0][1:].reshape(-1,1), trial6Velocity).predict(trial6[:,0][1:].reshape(-1,1))
]

trend_line = np.mean(trend_lines, axis=0)

m, b = np.polyfit(trial1[:,0][1:], trend_line, 1)

print("y = " + str(m) + "x + " + str(b))

plt.plot(trial1[:,0][1:], trial1Velocity, 'ro', label='Trial 1')
plt.plot(trial2[:,0][1:], trial2Velocity, 'bo', label='Trial 2')
plt.plot(trial3[:,0][1:], trial3Velocity, 'go', label='Trial 3')
plt.plot(trial4[:,0][1:], trial4Velocity, 'yo', label='Trial 4')
plt.plot(trial5[:,0][1:], trial5Velocity, 'co', label='Trial 5')
plt.plot(trial6[:,0][1:], trial6Velocity, 'mo', label='Trial 6')

plt.plot(trial1[:,0][1:], trend_line, 'k-', label = "Trend Line")


plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s^2)')

plt.title('6 Falling Tennis Ball Trials')

plt.legend()

plt.show()
