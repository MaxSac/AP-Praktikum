import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

Id = 0.1 * 10**(-9) #Dunkelstrom
L = 0.93 #Abstand zwischen Spalt und Schirm
lam = 633 * 10**(-9) #Wellenlänge des Lasers

def func(x, y):
    return ((lam/(math.pi*np.sin(x/L))) * (np.sin(y**(0.5)*(math.pi*np.sin(x/L)/lam)))**(-1))

print('-----------------------------------------------------------------------')
print('Einzelspalt b = 0.075mm')
a1, i1 = np.loadtxt('data1.txt', unpack=True)
i1 = i1 * 10**(-3) - Id
a1 = a1 * 10**(-3)
B1 = 0.075 * 10**(-3)

b1 = func(a1, i1)
M = np.mean(b1)
V = np.var(b1)
print('Mittelwert von b = ', M, ' +/- ', V)

plt.plot(a1, i1, 'gx', label='Messwerte')
plt.plot(a1, i1, 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / µA')
plt.xlabel('a / mm')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/plot1.pdf')
plt.close()

print('-----------------------------------------------------------------------')

print('Einzelspalt b = 0.15mm')
a2, i2 = np.loadtxt('data2.txt', unpack=True)
i2 = i2 * 10**(-6) - Id
a2 = a2 * 10**(-3)
B2 = 0.15 * 10**(-3)

b2 = func(a2, i2)
M = np.mean(b2)
V = np.var(b2)
print('Mittelwert von b = ', M, ' +/- ', V)

plt.plot(a2, i2, 'gx', label='Messwerte')
plt.plot(a2, i2, 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / µA')
plt.xlabel('a / mm')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/plot2.pdf')
plt.close()

print('-----------------------------------------------------------------------')
