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
alpha1 = 1.40 #80.06°, Dopplerwinkel fü 15°
alpha2 = 1.23 #70.53°, Dopplerwinkel fü 30°
alpha3 = 0.96 #54.74°, Dopplerwinkel fü 60°

#--------------------------------------------------------------------
def v(Q, d):
    return (Q * b) / (10 * math.pi * (d/2)**2)

def FitFunktion(v, m, b):
    return m * v + b
#--------------------------------------------------------------------

print('------------------------------------------------------------')
Q, f1, f2, f3 = np.loadtxt('data1_1.txt', unpack=True)
d = 0.007 #Durchmesser in m
v = v(Q, d) #Geschwindigkeit in m/s

params1, covariance = curve_fit(FitFunktion, v, f1/np.cos(alpha1))
print(params1)
params2, covariance = curve_fit(FitFunktion, v, f2/np.cos(alpha2))
print(params2)
params3, covariance = curve_fit(FitFunktion, v, f3/np.cos(alpha3))
print(params3)

plt.plot(v, f1/math.cos(alpha1), 'rx', label='15°')
plt.plot(v, FitFunktion(v, *params1), 'r-', label='$Fit_{15°}$')
plt.plot(v, f2/math.cos(alpha2), 'gx', label='30°')
plt.plot(v, FitFunktion(v, *params2), 'g-', label='$Fit_{30°}$')
plt.plot(v, f3/math.cos(alpha3), 'bx', label='60°')
plt.plot(v, FitFunktion(v, *params3), 'b-', label='$Fit_{60°}$')
plt.xlabel(r'$v\ /\ 10^{-5} \cdot \frac{\text{m}}{\text{s}}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / Hz')
plt.legend(loc="best", fontsize = 'small')
plt.grid()
plt.tight_layout()
plt.savefig('build/Doppler1.pdf')
plt.close()

print('------------------------------------------------------------')
def v(Q, d):
    return (Q * b) / (10 * math.pi * (d/2)**2)
Q, f1, f2, f3 = np.loadtxt('data1_2.txt', unpack=True)
d = 0.010 #Durchmesser in m
v = v(Q, d) #Geschwindigkeit in m/s

params1, covariance = curve_fit(FitFunktion, v, f1/np.cos(alpha1))
print(params1)
params2, covariance = curve_fit(FitFunktion, v, f2/np.cos(alpha2))
print(params2)
params3, covariance = curve_fit(FitFunktion, v, f3/np.cos(alpha3))
print(params3)

plt.plot(v, f1/math.cos(alpha1), 'rx', label='15°')
plt.plot(v, FitFunktion(v, *params1), 'r-', label='$Fit_{15°}$')
plt.plot(v, f2/math.cos(alpha2), 'gx', label='30°')
plt.plot(v, FitFunktion(v, *params2), 'g-', label='$Fit_{30°}$')
plt.plot(v, f3/math.cos(alpha3), 'bx', label='60°')
plt.plot(v, FitFunktion(v, *params3), 'b-', label='$Fit_{60°}$')
plt.xlabel(r'$v\ /\ 10^{-5} \cdot \frac{\text{m}}{\text{s}}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / Hz')
plt.legend(loc="best", fontsize = 'small')
plt.grid()
plt.tight_layout()
plt.savefig('build/Doppler2.pdf')
plt.close()

print('------------------------------------------------------------')
def v(Q, d):
    return (Q * b) / (10 * math.pi * (d/2)**2)
Q, f1, f2, f3 = np.loadtxt('data1_3.txt', unpack=True)
d = 0.016 #Durchmesser in m
v = v(Q, d) #Geschwindigkeit in m/s

params1, covariance = curve_fit(FitFunktion, v, f1/np.cos(alpha1))
print(params1)
params2, covariance = curve_fit(FitFunktion, v, f2/np.cos(alpha2))
print(params2)
params3, covariance = curve_fit(FitFunktion, v, f3/np.cos(alpha3))
print(params3)

plt.plot(v, f1/math.cos(alpha1), 'rx', label='15°')
plt.plot(v, FitFunktion(v, *params1), 'r-', label='$Fit_{15°}$')
plt.plot(v, f2/math.cos(alpha2), 'gx', label='30°')
plt.plot(v, FitFunktion(v, *params2), 'g-', label='$Fit_{30°}$')
plt.plot(v, f3/math.cos(alpha3), 'bx', label='60°')
plt.plot(v, FitFunktion(v, *params3), 'b-', label='$Fit_{60°}$')
plt.xlabel(r'$v\ /\ 10^{-5} \cdot \frac{\text{m}}{\text{s}}$')
plt.ylabel(r'$\frac{\Delta\nu}{\cos(\alpha)}$ / Hz')
plt.legend(loc="best", fontsize = 'small')
plt.grid()
plt.tight_layout()
plt.savefig('build/Doppler3.pdf')
plt.close()

print('------------------------------------------------------------')
T, f1, I1, f2, I2 = np.loadtxt('data2.txt', unpack=True)

plt.plot(T, I1, 'rx', label='I bei 45\%')
plt.plot(T, I2, 'gx', label='I bei 70\%')
plt.xlabel(r'Tiefe / $\mu$s')
plt.ylabel(r'$I\ /\ \frac{\text{W}^2}{\text{m}}$')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Intensitaet.pdf')
plt.close()

v1 = (f1 * c)/(4 * 10**6 * np.cos(alpha1))
v2 = (f2 * c)/(4 * 10**6 * np.cos(alpha1))
plt.plot(T, v1, 'rx', label='v bei 45\%')
plt.plot(T, v2, 'gx', label='v bei 70\%')
plt.xlabel(r'Tiefe / $\mu$s')
plt.ylabel(r'$v\ /\ \frac{\text{m}}{\text{s}}$')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Geschwindigkeit.pdf')
plt.close()

















print('------------------------------------------------------------')
'''
\begin{table}[H] %Frequenzänderung für unterschiedliche Rohrdurchmesser
  \centering
  \begin{tabular}{c|c||c|c|c}
    & Strömungsgeschwindigkeit / \% & $\Delta \nu_1$ / Hz & $\Delta \nu_2$ / Hz & $\Delta \nu_3$ / Hz \\
    \hline
    \multirow{5}*{7\,mm \O}  & 20 & 116 & 146 & 250  \\
                             & 25 & 190 & 300 & 1000 \\
                             & 30 & 300 & 480 & 800  \\
                             & 35 & 340 & 600 & 930  \\
                             & 40 & 460 & 730 & 1050 \\
    \hline
    \multirow{5}*{10\,mm \O} & 30 & 122 & 208 & 360  \\
                             & 35 & 180 & 290 & 530  \\
                             & 40 & 220 & 360 & 700  \\
                             & 45 & 280 & 460 & 900  \\
                             & 50 & 330 & 590 & 1100 \\
    \hline
    \multirow{5}*{16\,mm \O} & 30 & 61  & 85  & 145  \\
                             & 35 & 73  & 134 & 220  \\
                             & 40 & 100 & 180 & 280  \\
                             & 45 & 122 & 220 & 370  \\
                             & 50 & 140 & 250 & 430  \\
    \hline
  \end{tabular}
  \caption{Messwerte der Frequenzänderung bei dem Dopplereffekt für verschiedene Dopplerwinkel und Rohrdurchmesser.}
  \label{tab:Mess1}
\end{table}
'''
'''
\begin{table}[H] %Frequenzänderung für unterschiedliche Eindringtiefen
  \centering
  \begin{tabular}{c||c c||c c}
    & \multicolumn{2}{c||}{Pumpenleistung 70\,\%} & \multicolumn{2}{c}{Pumpenleistung 45\,\%} \\
    \hline
    Eindringtiefe / $\mu s$ & $\Delta \nu_1$ / Hz & Intensität & $\Delta \nu_2$ & Intensität \\
    \hline
    4.0  & 700 & 23000 & 400 & 14000 \\
    4.5  & 700 & 24000 & 360 & 13000 \\
    5.0  & 700 & 24000 & 360 & 13000 \\
    5.5  & 700 & 24500 & 340 & 10500 \\
    6.0  & 705 & 25000 & 340 & 10000 \\
    6.5  & 700 & 26000 & 340 & 10500 \\
    7.0  & 700 & 26000 & 350 & 10000 \\
    7.5  & 700 & 26000 & 340 & 9000  \\
    8.0  & 650 & 26000 & 330 & 9000  \\
    8.5  & 610 & 23000 & 340 & 8500  \\
    9.0  & 610 & 23000 & 330 & 8500  \\
    9.5  & 610 & 19000 & 330 & 8500  \\
    10.0 & 600 & 17500 & 340 & 8000  \\
    10.5 & 600 & 17500 & 340 & 8500  \\
    11.0 & 600 & 17000 & 340 & 8000  \\
    11.5 & 590 & 17000 & 340 & 7500  \\
    12.0 & 610 & 17000 & 330 & 7500  \\
    12.5 & 600 & 17500 & 330 & 7500  \\
    13.0 & 600 & 19000 & 330 & 7000  \\
    13.5 & 600 & 18500 & 340 & 6500  \\
    14.0 & 610 & 18500 & 330 & 6500  \\
    14.5 & 610 & 18500 & 330 & 6500  \\
    15.0 & 620 & 19000 & 330 & 6000  \\
    15.5 & 610 & 19000 & 330 & 6000  \\
    16.0 & 610 & 19000 & 330 & 5500  \\
    16.5 & 610 & 19500 & 330 & 6000  \\
    17.0 & 610 & 19000 & 330 & 6000  \\
    17.5 & 610 & 19000 & 330 & 5500  \\
    18.0 & 620 & 19000 & 330 & 5500  \\
    18.5 & 610 & 19500 & 320 & 5500  \\
    19.0 & 620 & 17000 & 320 & 5000  \\
    19.5 & 630 & 15000 & 330 & 4700  \\
    \hline
  \end{tabular}
  \caption{Messwerte der Frequenzänderung bei dem Dopplereffekt für verschiedene Eindringtiefen.}
  \label{tab:Mess2}
\end{table}
'''
