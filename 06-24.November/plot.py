import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy import stats

#Wichtige Werte
SB = 5.67 * 10**(-8)
offs = ((0.013 + 0.006)/2) * 10**(-3)
T_0 = 294.26

#Einlesen der Daten und auf SI-Einheit bringen
T, W, M, S, G = np.genfromtxt('ThermoTemperatur.txt', unpack=True)
T[0] = 95
T = T + 273.15
W = W * 10**(-3) - offs
M = M * 10**(-3) - offs
S = S * 10**(-3) - offs
G = G * 10**(-3) - offs
x = T**4 - T_0**4


def f(x, a, b):
    return a * x + b


print('-----------------------------------------------------------------------')

#Thermospannung gegen Temperatur(Schwarz)
params, covariance = curve_fit(f, x, S)
errors = np.sqrt(np.diag(covariance))
print('Steigung Schwarz =', params[0], '±', errors[0])
plt.plot(x, S*1000, 'rx', label="Messwerte")
plt.plot(x, f(x, *params)*1000, 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'$U_3 - U_0$ / mV')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/ThermoS.pdf')
plt.close()
ES = ufloat(params[0], errors[0])
print('Epsilon Schwarz = 1')

print('-----------------------------------------------------------------------')

#Thermospannung gegen Temperatur(Weiß)
params, covariance = curve_fit(f, x, W)
errors = np.sqrt(np.diag(covariance))
print('Steigung Weiß =', params[0], '±', errors[0])
plt.plot(x, W*1000, 'rx', label="Messwerte")
plt.plot(x, f(x, *params)*1000, 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'$U_1 - U_0$ / mV')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/ThermoW.pdf')
plt.close()
EW = ufloat(params[0], errors[0])
print('Epsilon Weiß = ', EW / ES)
print('-----------------------------------------------------------------------')

#Thermospannung gegen Temperatur(Messing)
params, covariance = curve_fit(f, x, M)
errors = np.sqrt(np.diag(covariance))
print('Steigung Messing =', params[0], '±', errors[0])
plt.plot(x, M*1000, 'rx', label="Messwerte")
plt.plot(x, f(x, *params)*1000, 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'$U_2 - U_0$ / mV')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/ThermoM.pdf')
plt.close()
EM = ufloat(params[0], errors[0])
print('Epsilon Weiß = ', EM / ES)

print('-----------------------------------------------------------------------')

#Thermospannung gegen Temperatur(Glänzend)
params, covariance = curve_fit(f, x, G)
errors = np.sqrt(np.diag(covariance))
print('Steigung Glänzend =', params[0], '±', errors[0])
plt.plot(x, G*1000, 'rx', label="Messwerte")
plt.plot(x, f(x, *params)*1000, 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'$U_4 - U_0$ / mV')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/ThermoG.pdf')
plt.close()
EG = ufloat(params[0], errors[0])
print('Epsilon Weiß = ', EG / ES)

print('-----------------------------------------------------------------------')

#Thermospannung gegen 1/A^2(weiß)
x, y = np.genfromtxt('ThermoAbstand.txt', unpack=True)
x = 1 / (x * 10**(-2))**2
y = (y * 10**(-3) - offs) * 1000
def f(x, a, b):
    return a * x + b
params, covariance = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
plt.plot(x, y, 'rx', label="Messwerte")
plt.plot(x, f(x, *params), 'b-', label='Ausgleichskurve')
plt.xlabel(r'$\frac{1}{A^2}$ / $\frac{1}{\text{m}^2}$')
plt.ylabel(r'$U_\text{weiß} - U_0$ / mV')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/ThermoAbstand.pdf')
plt.close()

print('-----------------------------------------------------------------------')
