import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy import stats
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

print('Dicke des Vermewendeten Leiterplätchen berechnen')
#Spezifischer Wiederstand
spRK = 0.018*10**(-6); spRZ = 0.06*10**(-6)

#liest die Spannung und Wiederstand ein zur Berechnung des Wiederstandes
AK, VK = np.loadtxt('data/widerstand.txt', unpack=True)
AZ, VZ = np.loadtxt('data/widerstandZink.txt', unpack=True)
RK = [0]*10; RZ = [0]*16; VK *= 10**(-3); VZ *= 10**(-3)

#liest die Hallspannung ein
AHK, VHK = np.loadtxt('data/hallK.txt', unpack=True)
AHZ, VHZ = np.loadtxt('data/hallZ.txt', unpack=True)
VHK *= 10**(-3); VHZ *= 10**(-3)


AB, HB, ZB = np.loadtxt('data/hysterese.txt', unpack=True)
HB /= 1000; ZB /= 1000

#Berechnung des Widerstandes
def widerstand(R,V,A,a):
    print('Einzelwiederstände:')
    for x in range(a):
        R[x] = V[x]/A[x]
        #print(x, ' = ', R[x])
    print('Mittelwert = ', np.mean(R),' +- ', stats.sem(R))
    return ufloat(np.mean(R), stats.sem(R))

#Berechnung der Dicke des Plätchens
def dicke(R,b,l,sp):
    k = (l*sp)/(R*b)
    print('Dicke des Plättchens: ', k)
    return k

#Berechnet die Ladungsträgerdichte
def laddichte(I,U,d,a):
    n = [0]*a
    for x in range(a):
        #print(I[x], U[x],d,a, c.e)
        n[x] = -1.194*I[x]/(U[x]*d*c.e)
        print(x, 'Ladungsdichte', n[x])
    print('Die gemittelte Ladungsträgerdichte beträgt: ', np.mean(n),' +-', stats.sem(n))
    return np.mean(n)

#Berechnet mittlere Flugzeit
def tau(n, spR):
    t = 2*c.m_e/((c.e**2)*n*spR)
    print('Mittlere Flugzeit: ', t)
    return t

#mittlere Driftgeschwidigkeit
def mv(n):
    v = -1000*1000/(n*c.e)
    print('Mittlere Driftgeschwindigkeit', v)
    return v

#Betrag der Geschwindigkeit der Elektronen im Festkörper
def bv(n):
    Ef = c.h**2/(2*c.m_e)*((3*n/(8*np.pi))**(2))**(1/3)
    print('Ef', Ef)
    v = np.sqrt(2*Ef/c.m_e)
    print('Betrag der Geschwindigkeit', v)
    return v

# Mittlere freie Weglänge
def l(tau, v):
    l = tau*v
    print('Mittlere Freie Weglänge', l)
    return l

#Berechnet beweglickeit
def my(tau):
    print('Berechnet Beweglichkeit')
    print(tau, c.e)
    my = -c.e*tau/(2*c.m_e)
    print(my)

print('Kupfer: ')
rK = widerstand(RK,VK,AK,10)
dK = dicke(rK, 0.02575, 0.0358, spRK)
nK = laddichte(AHK, VHK, dK.n, 19)
tK = tau(nK, spRK)
mvK = mv(nK)
bvK = bv(nK)
lK = l(tK, bvK)
myK = my(tK)
print('-------------------------------------------------------------')

print('Zink: ')
rZ = widerstand(RZ,VZ,AZ,16)
dZ = dicke(rZ, 0.02525, 0.0257, spRZ)
nZ = laddichte(AHZ, VHZ, dZ.n, 16)
tZ = tau(nZ, spRZ)
mvZ = mv(nZ)
bvZ = bv(nZ)
lZ = l(tZ, bvZ)
myZ = my(tZ)

print('-------------------------------------------------------------')

plt.plot(AB, HB, 'rx', label='Messwerte')
plt.plot(AB, ZB, 'rx')
plt.xlabel(r'Spulenstrom / A')
plt.ylabel(r'Feldstärke / T')
plt.legend(loc="best")
plt.tight_layout()
plt.grid()
plt.savefig('build/Hysterese.pdf')
plt.close()
