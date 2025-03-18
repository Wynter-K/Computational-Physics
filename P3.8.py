import numpy as np
import matplotlib.pyplot as plt

file = np.loadtxt('millikan.txt')

X = file[:,0]
Y = file[:,1]

E_x = 0
E_xx = 0
E_y = 0
E_xy = 0
N = len(X)

for i in range(0, len(X)):
 E_x += X[i] / N
 E_xx += X[i]**2 / N
 E_y += Y[i] / N
 E_xy += X[i]*Y[i] / N

m = (E_xy - E_x*E_y)/(E_xx - E_x**2)
c = (E_xx*E_y - E_x*E_xy)/(E_xx - E_x**2)

plt.plot(X, Y, 'ro', label='Real Data')
plt.plot(X, m*X + c, label='Fit line mX + c')
plt.text(0.05, 0.835, f'm = {m:.2f}\nc = {c:.2f}', transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top')
plt.grid(True)
plt.title('Millikan\'s Oil Drop Data')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Voltage(Volts)')
plt.legend()
plt.show()

e = 1.602e-19
h = m*e
print("Planck's const = ", h)