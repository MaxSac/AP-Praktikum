import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from scipy import stats
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

B_250, B_300, B_350, B_400, B_450 = np.loadtxt('data/B-Feld.txt', unpack=True)
E_230, E_300, E_350, E_180, E_260 = np.loadtxt('data/E-Feld.txt', unpack=True)
L = 0.175; r=[]; e_m = const.e/const.m_e

def radius(d):
    return ((0.0254/4)*d)/(L**2+((0.0254/4)*d)**2)
def magfeld(I):
    return const.mu_0*8/np.sqrt(125)*20*I/0.282
def lin(k, a, b):
    return a * k + b

for x in range(9):
    r.append(radius(x))

#B_Feld mit 250 Volt Beschleunigungsspannung
params_B_250, cov_B_250 = curve_fit(lin, magfeld(B_250),r)
plt.plot(magfeld(B_250),r, 'x')
plt.plot(magfeld(B_250), lin(magfeld(B_250), *params_B_250), label=r'$U_\text{B} =250 \text{V}$')
zw_250 = ufloat(params_B_250[0], np.sqrt(np.diag(cov_B_250))[0])
e_m_250 = (np.sqrt(8*250)*zw_250)**2
print('Steigung des Graphens mit 250 V = ', zw_250)
print('Spezifische Ladung', e_m_250, 'Prozentuelle Abweichung vom Theoriewert', (e_m- e_m_250)/e_m)


#B_Feld mit 300 Volt Beschleunigungsspannung
params_B_300, cov_B_300 = curve_fit(lin, magfeld(B_300),r)
plt.plot(magfeld(B_300),r, 'x')
plt.plot(magfeld(B_300), lin(magfeld(B_300), *params_B_300), label=r'$U_\text{B} =300 \text{V}$')
zw_300 = ufloat(params_B_300[0], np.sqrt(np.diag(cov_B_300))[0])
e_m_300 = (np.sqrt(8*300)*zw_300)**2
print('Steigung des Graphens mit 300 V = ', zw_300)
print('Spezifische Ladung', e_m_300, 'Prozentuelle Abweichung vom Theoriewert', (e_m- e_m_300)/e_m)


#B_Feld mit 350 Volt Beschleunigungsspannung
params_B_350, cov_B_350 = curve_fit(lin, magfeld(B_350),r)
plt.plot(magfeld(B_350),r, 'x')
plt.plot(magfeld(B_350), lin(magfeld(B_350), *params_B_350), label=r'$U_\text{B} =350 \text{V}$')
zw_350 = ufloat(params_B_350[0], np.sqrt(np.diag(cov_B_350))[0])
e_m_350 = (np.sqrt(8*350)*zw_350)**2
print('Steigung des Graphens mit 350 V = ', zw_350)
print('Spezifische Ladung', e_m_350, 'Prozentuelle Abweichung vom Theoriewert', (e_m- e_m_350)/e_m)

r = np.delete(r,8)
B_400 = np.delete(B_400, 8)
B_450 = np.delete(B_450, 8)

#B_Feld mit 400 Volt Beschleunigungsspannung
params_B_400, cov_B_400 = curve_fit(lin, magfeld(B_400),r)
plt.plot(magfeld(B_400),r, 'x')
plt.plot(magfeld(B_400), lin(magfeld(B_400), *params_B_400), label=r'$U_\text{B}=400 \text{V}$')
zw_400 = ufloat(params_B_400[0], np.sqrt(np.diag(cov_B_400))[0])
e_m_400 = (np.sqrt(8*400)*zw_400)**2
print('Steigung des Graphens mit 400 V = ', zw_400)
print('Spezifische Ladung', e_m_400, 'Prozentuelle Abweichung vom Theoriewert', (e_m- e_m_400)/e_m)


#B_Feld mit 450 Volt Beschleunigungsspannung
params_B_450, cov_B_450 = curve_fit(lin, magfeld(B_450),r)
plt.plot(magfeld(B_450),r, 'x')
plt.plot(magfeld(B_450), lin(magfeld(B_450), *params_B_450), label=r'$U_\text{B} =450 \text{V}$')
zw_450 = ufloat(params_B_450[0], np.sqrt(np.diag(cov_B_450))[0])
e_m_450 = (np.sqrt(8*450)*zw_450)**2
print('Steigung des Graphens mit 450 V = ', zw_450)
print('Spezifische Ladung', e_m_450, 'Prozentuelle Abweichung vom Theoriewert', (e_m- e_m_450)/e_m)

plt.xlabel('B')
plt.ylabel('D/(L² + D²)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/B-Feld.pdf')
plt.close()

#Stärke des Erdmagnetfeldes
print('Stärke des Erdmagnetfeldes', magfeld(0.27)/np.cos(math.pi/180*(70+60+70)/3))

#Empfindlichkeit der Röhre
D = []
for x in range(9):
    D.append(x*0.0254/4)
Dn = []
for x in range(8):
    Dn.append(x*0.0254/4)
E_350 = np.delete(E_350,0)

def berechneEmpf(E, d, lab):
    params, cov = curve_fit(lin, E,d)
    plt.plot(E,d, 'x')
    plt.plot(E, lin(E, *params), label= lab)
    zw = params[0]
def berechneEmpf(E, d, lab):
    params, cov = curve_fit(lin, E,d)
    plt.plot(E,d, 'x')
    plt.plot(E, lin(E, *params), label= lab)
    zw = params[0]
    print('Steigung des Graphens = ', params[0], '+-', np.sqrt(np.diag(cov))[0])
    return zw

zw_E_180 = berechneEmpf(E_180, D, r'$U_\text{B} =180 \text{V}$')
zw_E_230 = berechneEmpf(E_230, D, r'$U_\text{B} =230 \text{V}$')
zw_E_260 = berechneEmpf(E_260, D, r'$U_\text{B} =260 \text{V}$')
zw_E_300 = berechneEmpf(E_300, D, r'$U_\text{B} =300 \text{V}$')
zw_E_350 = berechneEmpf(E_350, Dn, r'$U_\text{B} =350 \text{V}$')
plt.xlabel('$U_d$')
plt.ylabel('D')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/E-Feld.pdf')
plt.close()

x = [1/180, 1/230, 1/260, 1/300, 1/350]
#y = [1.67*10**(-3), 1.38*10**(-3), 1.22*10**(-3), 1.09*10**(-3), 0.92*10**(-3)]
y = [zw_E_180, zw_E_230, zw_E_260, zw_E_300,zw_E_350]

def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x_plot = np.linspace(1/380, 1/175)

plt.plot(x, y, 'rx', label="example data")
plt.plot(x_plot, f(x_plot, *params), label='linearer Fit', linewidth=3)
plt.xlim(1/380,1/175)
plt.close()

frequenz = [159.56/2, 79.75,39.87*2, 26.65*3]
print(np.mean(frequenz),stats.sem(frequenz))
