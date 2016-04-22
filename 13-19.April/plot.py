import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

Id = 0.1 * 10**(-9) #Dunkelstrom
L = 0.93 #Abstand zwischen Spalt und Schirm
lam = 633 * 10**(-9) #Wellenlänge des Lasers

def func(a, b):
    return ((lam/(math.pi*b*np.sin(a/L))) * (np.sin((math.pi*b*np.sin(a/L))/lam)))**2

print('-----------------------------------------------------------------------')
print('Einzelspalt b = 0.075mm')
a1, i1 = np.loadtxt('data1.txt', unpack=True)
i1 = i1 * 10**(-6) - Id
a1 = a1 * 10**(-3)
b1 = 0.075 * 10**(-3)

params, cov = curve_fit(func, a1, i1)
print('b = ', params,'+/-', cov)

plt.plot(a1, i1, 'gx', label='Messwerte')
plt.plot(a1, func(a1, *params), 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / µA')
plt.xlabel('a / mm')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot1.pdf')
plt.close()

print('-----------------------------------------------------------------------')
'''
print('Einzelspalt b = 0.15mm')
a2, i2 = np.loadtxt('data2.txt', unpack=True)
i2 = i2 * 10**(-6) - Id
b2 = 0.15 * 10**(-3)

plt.plot(a2, i2, 'gx', label='Interferenzmuster mit $b$ = 0.15 mm')
plt.ylabel('Intensität / µA')
plt.xlabel('a / mm')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot2.pdf')
plt.close()

print('-----------------------------------------------------------------------')
print('Einzelspalt b = 0.4mm')
a3, i3 = np.loadtxt('data3.txt', unpack=True)
i3 = i3 * 10**(-6) - Id
b3 = 0.4 * 10**(-3)

plt.plot(a3, i3, 'gx', label='Interferenzmuster mit $b$ = 0.4 mm')
plt.ylabel('Intensität / µA')
plt.xlabel('a / mm')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot3.pdf')
plt.close()

print('-----------------------------------------------------------------------')
print('Doppelspalt b = 0.1mm, g = 0.4mm')
a4, i4 = np.loadtxt('data4.txt', unpack=True)
i4 = i4 * 10**(-6) - Id
b4 = 0.1 * 10**(-3)
g = 0.4 * 10**(-3)

plt.plot(a4, i4, 'gx', label='Interferenzmuster mit $b$ = 0.15mm')
plt.ylabel('Intensität / µA')
plt.xlabel('a / mm')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot4.pdf')
plt.close()
'''
