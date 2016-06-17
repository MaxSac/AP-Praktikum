import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

#Messwerte
U = np.array([310, 315, 325, 350, 375, 400, 450, 500, 550, 600, 625, 650, 675, 700, 705]) #Spannung in V
A = np.array([4634, 5059, 5223, 5437, 5384, 5368, 5405, 5447, 5552, 5485, 5598, 5745, 6028, 6264, 6443]) #Impulsrate
I = np.array([0.4, 0.6, 0.8, 1.2, 1.8, 2.4, 3.0, 3.6, 3.7, 4.0]) #Stromstärke in mikroA

print('---------------------------------------------------------------------')
i = 0
As = A[3:12]
Af = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
while i < 9:
    Af[i] = math.sqrt(As[i])/10
    i += 1
print(Af)

print('---------------------------------------------------------------------')
Ux = U[3:12]
Ax = A[3:12]
def Fit(x, m, b):
    return x * m + b
model = Model(Fit, independent_vars=['x'])
result = model.fit(Ax/10, x=Ux, b=Parameter(value=1), m=Parameter(value=0.1))
print('Steigung =', 0.090864197530844279, '+-', 0.0222)
print('y-Achse =', 503.69013096345441, '+-', 11.4)
Stei = (ufloat(0.090864197530844279, 0.0222)*100) / 545
print('Steigung in Prozent =', Stei*100)
print('---------------------------------------------------------------------')
'''
xWert = np.linspace(300, 750, 1000)
plt.errorbar(Ux, Ax/10, yerr=Af, fmt='x', ecolor='b', label='relevante Messwerte')
plt.plot(U[0:2], A[0:2]/10, 'gx')
plt.plot(U[13:16], A[13:16]/10, 'gx')
plt.plot(xWert, Fit(xWert, **result.params), 'r-', label='gefittete Messwerte')
plt.plot((340, 340), (450, 700), 'g-')
plt.plot((660, 660), (450, 700), 'g-')
plt.xlabel('$U$ / V')
plt.ylabel('Zählrate / 1/s')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Plateau.pdf')
plt.close()
'''
print('---------------------------------------------------------------------')
T = np.array([ufloat(50, 2), ufloat(70, 2)])
T = np.mean(T)
print(T)
print('---------------------------------------------------------------------')
print('N1  =', ufloat(4250, math.sqrt(4250)/4250))
print('N2  =', ufloat(3363, math.sqrt(3363)/3363))
print('N12 =', ufloat(7035, math.sqrt(7035)/7035))
N1  = ufloat(4250, math.sqrt(4250)/4250)
N2  = ufloat(3363, math.sqrt(3363)/3363)
N12 = ufloat(7035, math.sqrt(7035)/7035)
T = (N1+N2-N12) / (2*N1*N2)
print(T)
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
