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

#Berechnung des Wiederstandes
def widerstand(R,V,A,a):
    print('Einzelwiederstände:')
    for x in range(a):
        R[x] = V[x]/A[x]
        print(x, ' = ', R[x])
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
        print(I[x], U[x],d,a, c.e)
        n[x] = -5*I[x]/(U[x]*d*c.e)
    d= ufloat(np.mean(n), stats.sem(n))
    print('Die gemittelte Ladungsträgerdichte beträgt: ',d)
    return d

#Berechnet mittlere Driftgeschwindigkeit
def mv(b,d,n):
    print('Mittlere Driftgeschwindigkeit: ', -5/(b*d*n*c.e))
    return

print('Kupfer: ')
rK = widerstand(RK,VK,AK,9)
dK = dicke(rK, 0.02575, 0.0358, spRK)
nK = laddichte(AHK, VHK, dK.n, 20)
vK = mv(0.02575, dK, nK)

print('Zink: ')
rZ = widerstand(RZ,VZ,AZ,15)
dZ = dicke(rZ, 0.02525, 0.0257, spRZ)
nZ = laddichte(AHZ, VHZ, dZ.n, 16)
vZ = mv(0.02525, dZ, nZ)

