import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

#--------------------------------------------------------------------
b = 0.00001666666666 #Umrechnungsfaktor von L/min in m^3/s
cL = 1800 #m/s
cP = 2700 #m/s
c = 343.2 #m/s
alpha1 = 1.40 #80.06° #Dopplerwinkel fü 15°
alpha2 = 1.23 #70.53° #Dopplerwinkel fü 30°
alpha3 = 0.96 #54.74° #Dopplerwinkel fü 60°

#--------------------------------------------------------------------
def v(Q, d):
    return Q / (math.pi * (d/2)**2)

def df(f, a):
    return (f*c) / (4*10**6*math.cos(a))

#--------------------------------------------------------------------
print('------------------------------------------------------------')
Q, f1, f2, f3 = np.loadtxt('data1_1.txt', unpack=True)
Q = Q / 10 * b
d = 0.007 #Durchmesser in m

print(f1/math.cos(alpha1))
print(df(f1,alpha1))

plt.plot(f1/math.cos(alpha1), df(f1,alpha1), 'rx')
plt.xlabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / Hz')
plt.ylabel(r'v / $\frac{\text{m}}{\text{s}}')
plt.tight_layout()
plt.savefig('build/plot.pdf')
plt.close()

print('------------------------------------------------------------')
Q, f1, f2, f3 = np.loadtxt('data1_2.txt', unpack=True)
Q = Q / 10 * b
d = 0.010 #Durchmesser in m
print('v =', v, 'm/s')

print('------------------------------------------------------------')
Q, f1, f2, f3 = np.loadtxt('data1_3.txt', unpack=True)
Q = Q / 10 * b
d = 0.016 #Durchmesser in m
print('v =', v, 'm/s')

























print('------------------------------------------------------------')
