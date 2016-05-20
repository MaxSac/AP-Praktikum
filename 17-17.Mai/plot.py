import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

print('------------------------------------------------------------------')
HM = 305.0 #Hauptmaximum

print('------------------------------------------------------------------')
print('Helium Spektrum')
Grad_H = np.sin((np.array([331.7, 333.2, 334.6, 335.4, 335.6, 341.4, 347.3, 350.5]) - HM) * (math.pi/180))
Lambda = np.array([447.1, 471.3, 492.2, 501.6, 504.8, 587.6, 667.8, 706.5]) * 10**(-9)

def g(x, m, b):
    return x/m + b

model = Model(g, independent_vars=['x'])

result = model.fit(Grad_H, x=Lambda, b=Parameter(value=0.1), m=Parameter(value=10**(-6)))
print(result.params)

x_Wert = np.linspace(400, 750, 10000) * 10**(-9)
plt.plot(Lambda * 10**(9), Grad_H, 'rx', label='g')
plt.plot(x_Wert * 10**(9), g(x_Wert, **result.params), 'r-', label='g')
plt.xlabel('$\lambda$ / nm')
plt.ylabel('$\sin(\phi)')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Spaltbreite.pdf')
plt.close()

print('---------------------------------')
print('Rubidium-Dubletspektrum')
R_r = np.array([343.7, 344.5]) - HM

print('---------------------------------')
print('Natrium-Dubletspektrum')
N_r  = np.array([343.2, 343.4]) - HM
N_g  = np.array([341.2, 341.5]) - HM
N_gg = np.array([339.7, 339.9]) - HM

print('---------------------------------')
print('Kalium-Dubletspektrum')
K_g1  = np.array([340.5, 340.6]) - HM
K_g2  = np.array([340.7, 340.8]) - HM
K_gr1 = np.array([335.5, 335.6]) - HM
K_gr2 = np.array([335.6, 335.7]) - HM

print('------------------------------------------------------------------')


print('------------------------------------------------------------------')
