import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Example data files]
trial1 = np.loadtxt("data.txt")

trial1Velocity = np.diff(trial1[:,1]) / np.diff(trial1[:,0])

trend_lines = [
    LinearRegression().fit(trial1[:,0][1:].reshape(-1,1), trial1Velocity).predict(trial1[:,0][1:].reshape(-1,1))
]

trend_line = np.mean(trend_lines, axis=0)

m, b = np.polyfit(trial1[:,0][1:], trend_line, 1)

print("y = " + str(m) + "x + " + str(b))

plt.plot(trial1[:,0][1:], trial1Velocity, 'ro--', label='Trial 1')

plt.plot(trial1[:,0][1:], trend_line, 'k-', label = "Trend Line")


plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s^2)')

plt.title('6 Falling Tennis Ball Trials')

plt.legend()

plt.show()
