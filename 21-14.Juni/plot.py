import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

#Messwerte
U = np.array([350, 375, 400, 450, 500, 550, 600, 625, 650]) #Spannung in V
A = np.array([5437, 5384, 5368, 5405, 5447, 5552, 5485, 5598, 5745]) #Impulsrate
I = np.array([0.4, 0.6, 0.8, 1.2, 1.8, 2.4, 3.0, 3.6, 3.7, 4.0]) #Stromstärke in mikroA

print('---------------------------------------------------------------------')
i = 0
Af = np.array([ufloat(0.0, 0.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
while i < 9:
    Af[i] = math.sqrt(A[i])/10
    i += 1
print(Af)

print('---------------------------------------------------------------------')
def Fit(x, m, b):
    return x * m + b
model = Model(Fit, independent_vars=['x'])
result = model.fit(A/10, x=U, b=Parameter(value=1), m=Parameter(value=0.1))
print('Steigung =', 0.090864197530844279, '+-', 0.0222)
print('y-Achse =', 503.69013096345441, '+-', 11.4)
Stei = (ufloat(0.090864197530844279, 0.0222)*100) / 545
print('Steigung in Prozent =', Stei*100)
print('---------------------------------------------------------------------')
'''
xWert = np.linspace(300, 750, 1000)
plt.errorbar(U, A/10, xerr=Af, fmt='o', ecolor='b', label='Messwerte')
plt.plot(xWert, Fit(xWert, **result.params), 'r-', label='gefittete Plateaugerade')
plt.xlabel('$U$ / V')
plt.ylabel('Zählrate / 1/s')
plt.legend(loc="lower right")
plt.grid()
plt.tight_layout()
plt.savefig('build/Plateau.pdf')
plt.close()
'''


print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
