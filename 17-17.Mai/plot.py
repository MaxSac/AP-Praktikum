import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

#------------------------------------------------------------------
HM = 305.0 #Hauptmaximum
g = 9.81462761080996 * 10**(-7) #Gitterkonstante

#------------------------------------------------------------------
#Messwerte
#Auslenkung in Grad für Helium
H_g = (np.array([335.4, 335.6]) - HM) * (math.pi/180)
tH_g = 1.25
#Auslenkung in Grad für Natrium
N_gg = (np.array([339.7, 339.9]) - HM) * (math.pi/180)
tN_gg = 0.24
N_g  = (np.array([341.2, 341.5]) - HM) * (math.pi/180)
tN_g = 0.18
N_r  = (np.array([343.2, 343.4]) - HM) * (math.pi/180)
tN_r = 0.08
#Auslenkung in Grad für Kalium
K_gr1 = (np.array([335.5, 335.6]) - HM) * (math.pi/180)
tK_gr1 = 0.89
K_gr2 = (np.array([335.6, 335.7]) - HM) * (math.pi/180)
tK_gr2 = 0.67
K_g1  = (np.array([340.5, 340.6]) - HM) * (math.pi/180)
tK_g1 = 0.86
K_g2  = (np.array([340.7, 340.8]) - HM) * (math.pi/180)
tK_g2 = 0.81
#Auslenkung in Grad für Rubidium
R_r = (np.array([343.7, 344.5]) - HM) * (math.pi/180)
tR_r = 2.92
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
print('Nr. b: Berechnung der Eichgröße')
def Psi(Winkel):
    a = np.mean(Winkel)
    b = np.std(Winkel)
    cos = ufloat(np.cos(a), np.sin(a)*b)
    lam = np.sin(Winkel) * g
    psi = -(lam[0] - lam[1])/(cos*1.25)
    print('Mittelwert =', a, '+-', b)
    print('   cos     =', cos )
    print('Eichgröße  =', psi)
    print('--------------------')
    return psi

psi = np.array([ufloat(1.0, 1.0), 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

print('Eichgröße für Helium')
psi[0] = Psi(H_g)
print('Eichgröße für Natrium')
psi[1] = Psi(N_gg)
psi[2] = Psi(N_g)
psi[3] = Psi(N_r)
print('Mittelwert der Eichgrößen', np.mean([psi[1], psi[2], psi[3]]))
print('--------------------')
print('Eichgröße für Kalium')
psi[4] = Psi(K_gr1)
psi[5] = Psi(K_gr2)
psi[6] = Psi(K_g1)
psi[7] = Psi(K_g2)
print('Mittelwert der Eichgrößen', np.mean([psi[4], psi[5], psi[6], psi[7]]))
print('--------------------')
print('Eichgröße für Rubidium')
psi[8] = Psi(R_r)

print(np.mean(psi))
Mpsi = 3.198 * 10**(-9)

print('------------------------------------------------------------------')
print('Nr. c: Berechnung der Abschirmungszahl')

def Abschirm(Winkel, t, psi):
    cos = np.cos(np.mean(Winkel))
    psi = 3.198 * 10**(-9)
    dLam = cos * t * psi
    qLam = np.mean(np.sin(Winkel) * g)**2
    E = (c.h * c.c * dLam / qLam)
    S = z - (E * (2*137.06**2 * n**3)/(13.6*1.6022*10**(-19)))**(1/4)
    print('Delta E =', E*6.242*10**18)
    print('Abschirmungszahl =', S)
    print('----------')
    return S

print('---------------------------------')
print('Natrium-Dubletspektrum')
n = 3
z = 11
SN = np.array([1.0, 1.0, 1.0])
print('----------')
SN[0] = Abschirm(N_gg, tN_gg, 2.7408*10**(-9))
SN[1] = Abschirm(N_g, tN_g, 2.7408*10**(-9))
SN[2] = Abschirm(N_r, tN_r, 4.111*10**(-9))
SN = ufloat(np.mean(SN), np.std(SN))
print('Mittelwert =', SN)

print('---------------------------------')
print('Kalium-Dubletspektrum')
n = 4
z = 19
SN = np.array([1.0, 1.0, 1.0, 1.0])
print('----------')
SN[0] = Abschirm(K_gr1, tK_gr1, 1.3704*10**(-9))
SN[1] = Abschirm(K_gr2, tK_gr2, 1.3704*10**(-9))
SN[2] = Abschirm(K_g1, tK_g1, 1.3704*10**(-9))
SN[3] = Abschirm(K_g2, tK_g2, 1.3704*10**(-9))
SN = ufloat(np.mean(SN), np.std(SN))
print('Mittelwert =', SN)

print('---------------------------------')
print('Rubidium-Dubletspektrum')
n = 5
z = 37
Abschirm(R_r, tR_r, 10.96*10**(-9))
'''
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
'''
print('------------------------------------------------------------------')

'''
def Abschirm(Winkel):
    print('Winkel = ', Winkel)
    W = np.sin(Winkel) * g
    print('Lambda = ', W)
    E = (c.h * c.c * (1/W[0] - 1/W[1])) / c.e
    print('Energiedifferenz = ', E)
    S = z - ( (2*E*n**3) / (13.6*c.alpha**2) )**(1/4)
    print('Abschirmungszahl = ', S)
    print('----------')
    return S
'''
