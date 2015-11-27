import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy import stats

#Einlesen der Daten und auf SI-Einheit bringen
T, W, M, S, G = np.genfromtxt('data.txt', unpack=True)
T[0] = 95
T = T + 273.15

#Wichtige Werte
SB = 5.67 * 10**(-8)
offs = ((0.013 + 0.006)/2) * 10**(-3)
T_0 = 294.26
x = T**4 - T_0**4

#Thermospannung gegen Temperatur(Weiß)
zW = np.polyfit(x, W, 1)
print('Koeffizienten zu Weiß: ', zW)
pW = np.poly1d(zW)
plt.plot(x, W, 'g.', label='Messwerte')
plt.plot(x, pW(x), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'U / $10^{-3}$ V')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('build/ThermoW.pdf')
plt.close()

#Thermospannung gegen Temperatur(Messing)
zM = np.polyfit(x, M, 1)
print('Koefizienten zu Messing: ', zM)
pM = np.poly1d(zM)
plt.plot(x, M, 'g.', label='Messwerte')
plt.plot(x, pM(x), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'U / $10^{-3}$ V')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('build/ThermoM.pdf')
plt.close()

#Thermospannung gegen Temperatur(Schwarz)
zS = np.polyfit(x, S, 1)
print('Koefizienten zu Schwarz: ', zS)
pS = np.poly1d(zS)
plt.plot(x, S, 'g.', label='Messwerte')
plt.plot(x, pS(x), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'U / $10^{-3}$ V')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('build/ThermoS.pdf')
plt.close()

#Thermospannung gegen Temperatur(Glänzend)
zG = np.polyfit(x, G, 1)
print('Koefizienten zu Glänzend: ', zG)
pG = np.poly1d(zG)
plt.plot(x, G, 'g.', label='Messwerte')
plt.plot(x, pG(x), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$T^4 - T_0^4$ / K$^4$')
plt.ylabel(r'U / $10^{-3}$ V')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('build/ThermoG.pdf')
plt.close()
