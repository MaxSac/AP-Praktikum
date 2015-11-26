import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy import stats

#Einlesen der Daten und auf SI-Einheit bringen
T, W, M, S, G = np.genfromtxt('data.txt', unpack=True)
T = T + 273.15

#Stefan-Boltzmann-Konstante
SB = 5.67 * 10**(-8)

#Offsetspannung "gemittel"
offs = ((0.013 + 0.006)/2) * 10**(-3)

#T_0 bestimmen
T_0 = 294.26
print("T0:", 294.26)
print("T:", T[0], T[1], T[2], T[3], T[4], T[5], T[6], T[7], T[8], T[9], T[10], T[11], T[12])


#Thermospannung gegen Temperatur
x = T**4 - T_0**4
plt.plot(x, W)
plt.xlabel(r'T**4 - T0**4 / K')
plt.ylabel(r'U1 / mV')
plt.legend()
plt.tight_layout()
plt.savefig('build/ThermospannungW.pdf')
plt.close()

#lineare Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, W)
print('Steigung: ', slope, intercept, r_value, p_value, std_err)
