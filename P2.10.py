import numpy as np
import matplotlib.pyplot as plt

a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2

def B_func(A, Z):
    a5 = 0
    if A%2 :
        a5 = 0
    elif Z%2:
        a5 = -12.0
    else:
        a5 = 12.0
    return a1*A - a2*A**(2/3) - a3*(Z**2)/(A**(1/3)) - a4*((A-2*Z)**2)/A + a5/(A**(1/2))

def Binding_energy_per_nucleon(A, Z):
    return B_func(A, Z)/A

def most_stable_A(Z):
    A = 0
    BEPN_max = 0
    for i in range(Z, 3*Z):
        BEPN = Binding_energy_per_nucleon(i, Z)
        if BEPN > BEPN_max:
            BEPN_max = BEPN
            A = i
    return BEPN_max

Z_max = 0
BEPN_maximum = 0
for i in range(1, 100):
    if most_stable_A(i) > BEPN_maximum:
        BEPN_maximum = most_stable_A(i)
        Z_max = i

print("Z = ", Z_max, "B/A = ", BEPN_maximum)