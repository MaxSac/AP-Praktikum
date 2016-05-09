import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

print('-----------------------------------------------------------------------')

U_1, I1, I2 = np.loadtxt('Diode1.txt', unpack=True)
U_2, I3, I4, I5 = np.loadtxt('Diode2.txt', unpack=True)
U_heiz = np.array([6.2, 6.0, 5.0, 4.4, 4.0])
I_heiz = np.array([2.5, 2.4, 2.0, 1.9, 1.8])
f1 = 0.32 / 10000 #m^2 emittierende Fläche
f2 = 0.35 / 10000 #m^2 emittierende Fläche



print('-----------------------------------------------------------------------')
print('Kennlinienschar und Sättigungsstrom')

plt.plot(U_1, I1, 'rx', label='$I_1 = 2.5$ A')
plt.plot(U_1, I2, 'gx', label='$I_2 = 2.4$ A')
plt.ylabel('I / mA')
plt.xlabel('U / V')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Kenn1.pdf')
plt.close()

plt.plot(U_2, I3, 'bx', label='$I_3 = 2.0$ A')
plt.plot(U_2, I4, 'kx', label='$I_4 = 1.9$ A')
plt.plot(U_2, I5, 'yx', label='$I_5 = 1.8$ A')
plt.ylabel('I / mA')
plt.xlabel('U / V')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Kenn2.pdf')
plt.close()

print('-----------------------------------------------------------------------')
print('Exponenten des Raumladungsgesetzes')

a = 0.0002176
konst = 4/9 * c.epsilon_0 * (2*c.e/c.m_e)**(0.5) * f1 / a**2

def Raumladungsgesetz(V, x):
    return konst * (V**x)

model = Model(Raumladungsgesetz, independent_vars=['V'])

result1 = model.fit(I1, V=U_1, x=Parameter(value=1.5))
print('I1 = ', result1.params)
print('--------------------')

result2 = model.fit(I2, V=U_1, x=Parameter(value=1.5))
print('I2 = ', result2.params)
print('--------------------')

plt.plot(U_1, Raumladungsgesetz(U_1, 1.378684), 'r-', label='$I_1 = 2.5$ A')
plt.plot(U_1, Raumladungsgesetz(U_1, 1.344863), 'g-', label='$I_2 = 2.4$ A')
plt.ylabel('I / mA')
plt.xlabel('U / V')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Raum.pdf')
plt.close()

print('-----------------------------------------------------------------------')
print('Anlaufstromgebiet und Kathodentemperatur')

R = 1000000 #Ohm
U, I = np.loadtxt('Anlauf.txt', unpack=True)
I *= 10**(-9)
U_korr = U - R*I

def Kathodentemperatur(V, T, j):
    return j * np.exp(-(c.e*V) / (c.k*T))

model = Model(Kathodentemperatur, independent_vars=['V'])
result = model.fit(I, V=U_korr, T=Parameter(value=2000), j=Parameter(value=1))
print('T = ', result.params)

plt.plot(U_korr, I * 10**9, 'rx', label='Messwerte')
plt.plot(U_korr, Kathodentemperatur(U_korr, 2702.2142, 8.6817), 'g-', label='gefittete Kurve')
plt.ylabel('I / nA')
plt.xlabel('U / V')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Anlauf.pdf')
plt.close()




print('-----------------------------------------------------------------------')
print('Kathodentemperatur aus der Leistungsbilanz des Heizstromfadens')
T = ((I_heiz*U_heiz-0.95)/(f1*10000*0.28*5.7*10**(-12)))**(1/4)
print(T)

print('-----------------------------------------------------------------------')
print('Austrittsarbeit für Wolfram')
T = np.array([2051.71, 1951.86, 1870.36])
I_s = np.array([175, 75, 35])* 10**(-6)
Phi = -(c.k*T)/c.e*np.log((I_s*c.h**3) / (4*math.pi*f2*c.e*c.m_e*c.k**2*T**2))
print(Phi)

asd = np.mean(Phi)
asf = np.var(Phi)
print(asd, asf)























print('-----------------------------------------------------------------------')
