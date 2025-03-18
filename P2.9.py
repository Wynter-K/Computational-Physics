import numpy as np
import matplotlib.pyplot as plt

def func1(i,j,k):
    result = -1/np.sqrt(i**2 + j**2 + k**2)
    factor = (-1)**(i+j+k)
    return factor*result

def get_Madelung_constant(L):
    result = 0
    for i in range(-L,L):
        for j in range(-L,L):
            for k in range(-L,L):
                if i==0 and j==0 and k==0:
                    continue
                result += func1(i,j,k)
    return result


L_max = 10
Maedlungs = [get_Madelung_constant(L) for L in range(1,L_max+1)]
plt.plot(range(1,L_max+1), Maedlungs)
plt.xlabel("L")
plt.ylabel("Madelung constant")
plt.show()