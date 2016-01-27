import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

print('-----------------------------------------------------------------------')
print('Konstanten des Drahtes')
#Radius
R = ufloat(0.10300, 0.00022) / 1000
print('R =', R)
#Länge
L = ufloat(0.5983, 0.0008)
print('L =', L)

print('-----------------------------------')
print('Konstanten der Kugel')
#Kugelmasse
mK = ufloat(0.5122, 0.0002)
print('mK =', mK)
#Kugelradius
RK = ufloat(0.02538, 0.00001)
print('RK =', RK)
#Trägheitsmoment der Kugelhalterung
IH = 2.25 * 10**(-6)
print('IH =', IH)
#Gesamtträgheitsmoment, Kugel + Halterung
IK = 2/5 * mK * RK**2
Ig = IK + IH
print('IK =', IK)
print('Ig =', Ig)

print('-----------------------------------')
print('Konstanten der Helmholzspule')
#Windungszahl
N = 390
print('N =', N)
#Radius
RH = 0.078
print('RH =', RH)

print('-----------------------------------------------------------------------')
print('Schubmodul G bestimmen')
#Schwingungsdauer ohne Magnet
T = np.array([18.798, 18.800, 18.800, 18.751, 18.794, 18.799, 18.798, 18.795,
18.797, 18.800])
T = ufloat(np.mean(T), np.std(T))
print('T =', T)

G = (16 * math.pi * mK * RK**2 * L) / (5 * T**2 * R**4)
print('G =', G)

print('-----------------------------------------------------------------------')
print('Bestimmung des magnetischen Momentes m')
a = np.array([17.184, 17.166, 17.378, 17.333, 17.336])
a = ufloat(np.mean(a), np.std(a))
print('I(0.2A) =', a)
b = np.array([16.027, 15.992, 16.005, 16.006, 15.992])
b = ufloat(np.mean(b), np.std(b))
print('I(0.4A) =', b)
c = np.array([15.081, 15.048, 15.052, 15.041, 15.026])
c = ufloat(np.mean(c), np.std(c))
print('I(0.6A) =', c)
d = np.array([14.152, 14.104, 14.142, 14.109, 14.104])
d = ufloat(np.mean(d), np.std(d))
print('I(0.8A) =', d)
e = np.array([13.197, 13.251, 13.163, 13.244, 13.174])
e = ufloat(np.mean(e), np.std(e))
print('I(1.0A) =', e)

print(' ')

Tm = np.array([a, b, c, d, e])
I = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
mu = 4 * math.pi * 10**(-7) #Magnetische Feldkonstante

B = (8 * mu * N * I) / (125**(0.5) * R)
print('B =', B)

print(' ')

Therm = (4 * math.pi**2 * Ig) / (Tm**2)
print('Therm =', Therm)

B = np.array([B[0].n, B[1].n, B[2].n, B[3].n, B[4].n])
Therm = np.array([Therm[0].n, Therm[1].n, Therm[2].n, Therm[3].n, Therm[4].n])
def f(x, a, b):
    return a * x + b
params, covariance = curve_fit(f, B, Therm)
"""
plt.plot(B, Therm * 10**4, 'rx', label='Messwerte')
plt.plot(B, f(B, *params) * 10**4, 'b-', label='linearer Fit')
plt.xlabel(r'B / $10^{-3}$ T')
plt.ylabel(r'$\frac{4 \pi^2 \theta}{T_\text{m}^2}$ / $10^{-4}$ Nm')
plt.grid()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/MagnetischesMoment.pdf')
plt.close()
"""
errors = np.sqrt(np.diag(covariance))
m = ufloat(params[0], errors[0]) * 10**3
print('m =', m)


print('-----------------------------------------------------------------------')
print('Bestimmung der Horizontalkomponente des Erdmagnetfelds')
#Schwingungsdauer mit Magnet
Tmit = np.array([18.638, 18.607, 18.582, 18.592, 18.625, 18.629, 18.613, 18.588, 18.599, 18.620])
Tmit = ufloat(np.mean(Tmit), np.std(Tmit))
print('Tmit =', Tmit)

BH = ((4 * math.pi**2 * Ig) / (m)) * (1/Tmit**2 - 1/T**2)
print('BH =', BH)
print('-----------------------------------------------------------------------')















print('-----------------------------------------------------------------------')
