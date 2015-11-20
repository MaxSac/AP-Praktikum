import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#Einlesen der Daten
t, T1, pb, T2, pa, W = np.loadtxt('data.txt', unpack=True)
t = t*60

#Temperaturplot
plt.plot(t, T2, 'g.', label=r'$T2$')
plt.plot(t, T1, 'r.', label=r'$T1$')
plt.xlabel(r'Zeit / s')
plt.ylabel(r'Temperatur / K')
plt.legend()
plt.tight_layout()
plt.savefig('build/TVerlauf.pdf')
plt.close()


#Ausgleichsgraden Plot
z1 = np.polyfit(t, T1, 2)
z2 = np.polyfit(t, T2, 2)
print('Koefizienten zur Funktion von T1: ', z1)
print('Koefizienten zur Funktion von T2: ', z2)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp = np.linspace(0, 2000, 100)
plt.plot(xp, p1(xp), 'b-', label=r'T1')
plt.plot(xp, p2(xp), 'r-', label=r'T2')
plt.xlabel(r'Zeit / s')
plt.ylabel(r'Temperatur / K')
plt.legend()
plt.tight_layout()
plt.savefig('build/Ausgleichsgrade.pdf')
