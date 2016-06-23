import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

DA, ErrDA, IA, MA = np.loadtxt('data/Aluminium.txt', unpack=True)
DB, IB, MB = np.loadtxt('data/Blei.txt', unpack=True)
DK, IK, MK = np.loadtxt('data/Kupfer.txt', unpack=True)

NullGamma = int(804/900); NullBeta = int(248/900)
DA *= (10**(-6)*2760); DB *= 0.001; DK *= 0.001;

#Berechnet bereinigte Zählrate
def berechneZaehlrate(Impulszahl, Zeit, Null, laenge):
	Z = [0]*laenge	
	for x in range(laenge):
	  Z[x] = Impulszahl[x]/Zeit[x] - Null
	return np.array(Z)

# Berechnet den Fehler der Zählrate
def calcerr(Z, A):
        Zerr= [0]*A
        for x in range(A):
            Zerr[x] = np.sqrt(Z[x])
        return Zerr

#lineraer Fit
def f(x, a, b):
    return np.exp(-a*x + b)

#Fitte durch die Punkte x,y
def fitfunc(x,y,xdeff):
    fx, ferr = curve_fit(f, x, y)
    #fx = np.exp(fx)
    ferr = np.sqrt(np.diag(ferr))
    plt.plot(xdeff, f(xdeff, *fx))
    m = ufloat(fx[0],ferr[0]) 
    b = ufloat(fx[1],ferr[0])
    print('Steigung', m, 'y-Achseschnitt', b)
    return m, b


print('--------------Aluminium-------------')
#Berechnet Zählrate mit Fehler
ZA = berechneZaehlrate(IA,MA,NullBeta, 11)
ZAerr = calcerr(ZA,11)
print(ZA, ZAerr)
plt.semilogy(DA,ZA,'bx', label='Messwerte')
plt.errorbar(DA, ZA, yerr=ZAerr, fmt='bx')
xdeff = np.linspace(0,2,50)
m1, b1 = fitfunc(DA[:5],ZA[:5],xdeff)
m2, b2 = fitfunc(DA[5:],ZA[5:],xdeff)
s = (b1-b2)/(m1-m2)
Emax = 1.92*(((s*0.10)**2+0.22*(s*0.10))**0.5)
print('Schnittpunkt = ', s, "und Maximale Energie von: ", Emax)
plt.xlim(0.2,1.4)
plt.xlabel(r'Massenbelegung / $\frac{kg}{m^2}$')
plt.ylim(10**(-1),10**2)
plt.ylabel(r'Zählrate / $cps$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/Aluminium.pdf')
plt.close()

print('--------------Blei------------------')
ZB = berechneZaehlrate(IB,MB,NullGamma, 15)
ZBerr = calcerr(ZB, 15)
#print(ZB, ZBerr)
plt.semilogy(DB,ZB,'rx')
plt.errorbar(DB,ZB, yerr=ZBerr, fmt='rx')
xdeff = np.linspace(0, 0.065, 50)
fitfunc(DB,ZB,xdeff)
plt.xlim(0,0.065)
plt.xlabel(r'Dicke / $\frac{1}{m}$')
plt.ylabel(r'Zaehlrate / $cps$')
plt.tight_layout()
plt.savefig('build/Blei.pdf')
plt.close()

print('--------------Kupfer----------------')
ZK = berechneZaehlrate(IK,MK,NullGamma, 22)
ZKerr = calcerr(ZK,22)
#print(ZK, ZKerr)
plt.semilogy(DK,ZK,'rx')
plt.errorbar(DK, ZK, yerr=ZKerr, fmt='rx')
xdeff= np.linspace(0, 0.065, 50)
fitfunc(DK,ZK, xdeff)
plt.xlim(0,0.065)
plt.xlabel(r'Dicke / $\frac{1}{m}$')
plt.ylabel(r'Zaehlrate / $cps$')
plt.tight_layout()
plt.savefig('build/Kupfer.pdf')
plt.close()

