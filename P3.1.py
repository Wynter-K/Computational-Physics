import numpy as np
import matplotlib.pyplot as plt


def running_avg(data, window_size):
    avg_data = np.zeros(len(data) - window_size + 1)
    for i in range(len(data) - window_size + 1):
        avg_data[i] = np.mean(data[i:i+window_size])
    return avg_data

data = np.loadtxt('sunspots.txt')

month = data[:,0]
sunspots = data[:,1]
running_avg_sunspots = running_avg(sunspots, 5)

plt.plot(month, sunspots)
plt.plot(month[2:-2], running_avg_sunspots)

plt.xlim(0, 1000)
plt.xlabel("Months since Jan 1749")
plt.ylabel("Number of Sunspots")
plt.title("Sunspots over time")
plt.show()