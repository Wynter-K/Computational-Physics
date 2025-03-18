import numpy as np
import matplotlib.pyplot as plt

file = np.loadtxt('stm.txt') # Load the data from the file
print(file.shape)
plt.imshow(file)
plt.colorbar()
plt.show()