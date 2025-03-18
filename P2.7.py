import matplotlib.pyplot as plt
import numpy as np

M = 1.989e30
G = 6.674e-11

l1 = float(input("Enter the perihelion distance of the planet in meters: "))
v1 = float(input("Enter the velocity of the planet at perihelion in m/s: "))

coeff_1 = G*M / (v1*l1)
coeff_2 = 2*G*M/l1 - v1**2

v2 = coeff_1 - np.sqrt(coeff_1**2 - coeff_2)
l2 = l1*v1/v2

a = (l1 + l2)/2
e = (l2 - l1)/(l2 + l1)
b = np.sqrt(l1*l2)
T_sec = 2*np.pi*a*b/(l1*v1)
T_year = T/(60*60*24*365.25)

print("The aphelion distance of the planet is: ", l2)
print("The semi-major axis of the orbit is: ", a)
print("The eccentricity of the orbit is: ", e)
print("The period of the orbit is(s): ", T_sec)
print("The period of the orbit is(years): ", T_year)