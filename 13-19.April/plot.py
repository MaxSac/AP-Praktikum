import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

Id = 0.1 * 10**(-9) #Dunkelstrom
L = 0.93 #Abstand zwischen Spalt und Schirm
lam = 635 * 10**(-9) #Wellenlänge des Lasers

def Einzel(x, b, A):
    return ((A*lam)/(math.pi*np.sin(x/L)))**2 * (np.sin((math.pi*b*np.sin(x/L))/lam))**2

def Doppel(x, b, s):
    return 4*(np.cos((math.pi*s*np.sin(x/L))/lam))**2 * ((lam)/(math.pi*np.sin(x/L)))**2 * (np.sin((math.pi*b*np.sin(x/L))/lam))**2

print('-----------------------------------------------------------------------')
print('Einzelspalt b = 0.075mm')

a1, i1 = np.loadtxt('data1.txt', unpack=True)
i1 = i1 * 10**(-6) - Id
a1 = a1 * 10**(-3)
B1 = 0.075 * 10**(-3)

params, cov = curve_fit(Einzel, a1, i1)
print('b = ', params[0], cov[0])
print('A = ', params[1], cov[1])

xwerte = np.linspace(-0.025, 0.025, 100)

plt.plot(a1, i1, 'gx', label='Messwerte')
plt.plot(xwerte, Einzel(xwerte, *params), 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / A')
plt.xlabel('a / m')
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

params, cov = curve_fit(Einzel, a2, i2)
print('b = ', params[0], cov[0])
print('A = ', params[1], cov[1])

xwerte = np.linspace(-0.025, 0.025, 100)

plt.plot(a2, i2, 'gx', label='Messwerte')
plt.plot(xwerte, Einzel(xwerte, *params), 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / A')
plt.xlabel('a / m')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/plot2.pdf')
plt.close()

print('-----------------------------------------------------------------------')
print('Einzelspalt b = 0.40mm')

a3, i3 = np.loadtxt('data3.txt', unpack=True)
i3 = i3 * 10**(-6) - Id
a3 = a3 * 10**(-3)
B3 = 0.15 * 10**(-3)

params, cov = curve_fit(Einzel, a3, i3)
print('b = ', params[0], cov[0])
print('A = ', params[1], cov[1])

xwerte = np.linspace(-0.025, 0.025, 100)

plt.plot(a3, i3, 'gx', label='Messwerte')
plt.plot(xwerte, Einzel(xwerte, *params), 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / A')
plt.xlabel('a / m')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/plot3.pdf')
plt.close()

print('-----------------------------------------------------------------------')
print('Doppelspalt b = 0.1mm, g = 0.4mm')

a4, i4 = np.loadtxt('data4.txt', unpack=True)
i4 = i4 * 10**(-6) - Id
a4 = a4 * 10**(-3)
B4 = 0.1 * 10**(-3)

params, cov = curve_fit(Doppel, a4, i4)
print('b = ', params[0], cov[0])
print('s = ', params[1], cov[1])

xwerte = np.linspace(-0.025, 0.025, 100)

plt.plot(a4, i4, 'gx', label='Messwerte')
plt.plot(xwerte, Doppel(xwerte, *params), 'r-', label='gefittete Kurve')
plt.ylabel('Intensität / A')
plt.xlabel('a / m')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/plot4.pdf')
plt.close()

print('-----------------------------------------------------------------------')
