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
g = 9.8257678973119135 * 10**(-7) #Gitterkonstante
'''
print('------------------------------------------------------------------')
print('Nr. a: Berechnung der Gitterkonstanten g')

Rad_H = np.sin((np.array([331.1, 331.7, 333.2, 334.6, 335.4, 335.6, 341.4, 347.3, 350.5]) - HM) * (math.pi/180))
Lambda = np.array([438.8, 447.1, 471.3, 492.2, 501.6, 504.8, 587.6, 667.8, 706.5]) * 10**(-9)

def Gitter(x, m, b):
    return x/m + b

model = Model(Gitter, independent_vars=['x'])

result = model.fit(Rad_H, x=Lambda, b=Parameter(value=0.1), m=Parameter(value=10**(-6)))
print(result.params)

x_Wert = np.linspace(400, 750, 10000) * 10**(-9)
plt.plot(Lambda * 10**(9), Rad_H, 'rx', label='Messwerte')
plt.plot(x_Wert * 10**(9), Gitter(x_Wert, **result.params), 'b-', label='Ausgleichsgerade')
plt.xlabel('$\lambda$ / $10^{-9}$ m')
plt.ylabel('$\sin(\phi)$')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Gitterkonstante.pdf')
plt.close()
'''
print('------------------------------------------------------------------')
print('Nr. c: Berechnung der Abschirmungszahl')
def Abschirm(Winkel):
    print('Winkel = ', Winkel)
    W = np.sin(Winkel) * g
    print('Lambda = ', W)
    E = (c.h * c.c * (1/W[0] - 1/W[1])) / c.e
    print('Energiedifferenz = ', E)
    S = z - ((2*E*n**3) / (c.Rydberg*c.alpha**2))**(1/4)
    print('Abschirmungszahl = ', S)
    print('----------')


print('---------------------------------')
print('Natrium-Dubletspektrum')
n = 3
z = 11
print('----------')
N_gg = (np.array([339.7, 339.9]) - HM) * (math.pi/180)
Abschirm(N_gg)
N_g  = (np.array([341.2, 341.5]) - HM) * (math.pi/180)
Abschirm(N_g)
N_r  = (np.array([343.2, 343.4]) - HM) * (math.pi/180)
Abschirm(N_r)

SN = np.array([10.8210, 10.8066, 10.8302])
ASN = ufloat(np.mean(SN), np.std(SN))
print('Mittelwert = ', ASN)

print('---------------------------------')
print('Kalium-Dubletspektrum')
n = 4
z = 19
print('----------')
K_gr1 = (np.array([335.5, 335.6]) - HM) * (math.pi/180)
Abschirm(K_gr1)
K_gr2 = (np.array([335.6, 335.7]) - HM) * (math.pi/180)
Abschirm(K_gr2)
K_g1  = (np.array([340.5, 340.6]) - HM) * (math.pi/180)
Abschirm(K_g1)
K_g2  = (np.array([340.7, 340.8]) - HM) * (math.pi/180)
Abschirm(K_g2)

SN = np.array([18.7998, 18.8001, 18.8154, 18.8160])
ASN = ufloat(np.mean(SN), np.std(SN))
print('Mittelwert = ', ASN)

print('---------------------------------')
print('Rubidium-Dubletspektrum')
n = 5
z = 37
print('----------')
R_r = (np.array([343.7, 344.5]) - HM) * (math.pi/180)
Abschirm(R_r)

print('------------------------------------------------------------------')
print('Nr. b: Berechnung der Eichgröße')
def Psi(Winkel):
    a = np.mean(Winkel)
    b = np.std(Winkel)
    c = ufloat(np.cos(a), np.sin(a)*b)
    t = (Winkel[0] - Winkel[1])
    lam = np.sin(Winkel) * g
    psi = (lam[0] - lam[1])/(c*t)
    print('Mittelwert = ', a, '+-', b)
    print('   cos     = ', c )
    print('Delta t = ', t)
    print('Eichgröße = ', psi)
    print('----------')

print('Beugungswinkel für Natrium')
Psi(N_gg)
Psi(N_g)
Psi(N_r)
print('Beugungswinkel für Kalium')
Psi(K_gr1)
Psi(K_gr2)
Psi(K_g1)
Psi(K_g2)
print('Beugungswinkel für Rubidium')
Psi(R_r)

print('Mittelwert der Eichgrößen')
a = ufloat(9.826, 0.012) * 10**(-7)
b = ufloat(9.826, 0.019) * 10**(-7)
c = ufloat(9.826, 0.014) * 10**(-7)
d = ufloat(9.826, 0.005) * 10**(-7)
e = ufloat(9.826, 0.005) * 10**(-7)
f = ufloat(9.826, 0.006) * 10**(-7)
g = ufloat(9.826, 0.006) * 10**(-7)
h = ufloat(9.83, 0.06)   * 10**(-7)
Eichgrößen = np.array([a, b, c, d, e, f, g, h])
Eich = np.mean(Eichgrößen)
print('Mittelwert = ', Eich)

print('------------------------------------------------------------------')
print('Nr. d: Distanz zwischen Dublettlinien')
ds = 1.25

print('----------')
print('Eichung')
r = (ds / 0.003)
print('r = ', r * 10**(-6))

print('----------')
print('Natrium')
print('rot = ', 0.08 / r)
print('gelb = ', 0.18 / r)
print('grüngelb = ', 0.24 / r)

print('----------')
print('Kalium')
print('gelb = ', 0.86 / r)
print('gelb = ', 0.81 / r)
print('grün = ', 0.89 / r)
print('grün = ', 0.67 / r)

print('----------')
print('Kalium')
print('rot = ', 2.92 / r)

print('------------------------------------------------------------------')
