import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Einlesen der Daten
t, T1, pb, T2, pa, W = np.loadtxt('data.txt', unpack=True)
t = t*60
#pb = ufloat(pb, 10)
#pa = ufloat(pa, 10)

#Temperaturplot
def f(x, a, b, c):
        return a*(x**2) + b*x + c
ppot1, pcov1 = curve_fit( f, t, T1)
ppot2, pcov2 = curve_fit( f, t, T2)
plt.plot(t, T2, 'g.', label=r'$T2$')
plt.plot(t, T1, 'r.', label=r'$T1$')
plt.xlabel(r'Zeit / s')
plt.ylabel(r'Temperatur / K')
plt.legend(loc="best")
plt.plot(t, f(t, *ppot1), 'b-', label='Fit T1')
plt.plot(t, f(t, *ppot2), 'r-', label='Fit T2')
plt.tight_layout()
plt.savefig('build/Ausgleichsgrade.pdf')
plt.close()

#Koeffizienten werden berechnet
errors1 = np.sqrt(np.diag(pcov1))
errors2 = np.sqrt(np.diag(pcov2))
a1 = ufloat(ppot1[0],errors1[0])
a2 = ufloat(ppot2[0],errors2[0])
b1 = ufloat(ppot1[1],errors1[1])
b2 = ufloat(ppot2[1],errors2[1])
c1 = ufloat(ppot1[2],errors1[2])
c2 = ufloat(ppot2[2],errors2[2])
print('Koeffizienten T1: a=', a1, ' b= ', b1, ' c= ', c1)
print('Koeffizienten T2: a=', a2, ' b= ', b2, ' c= ', c2)

print("-----------------------------------------------------------")

#Differentialquotient
def q1(t):
    return 2*a1*t + b1
def q2(t):
    return 2*a2*t + b2
print('DiffQ T1', '60: T', q1(60), ', 420:', q1(420), ', 1020:', q1(1020), ', 1500:', q1(1500))
print('DiffQ T2', '60: T', q2(60), ', 420:', q2(420), ', 1020:', q2(1020), ', 1500:', q2(1500))

print("-----------------------------------------------------------")

#Bestimmung der Theoretischen Güte
T60_1   = ufloat(294.7,0.05)
T60_2   = ufloat(294.3,0.05)
T420_1  = ufloat(302.0,0.05)
T420_2  = ufloat(288.5,0.05)
T1020_1 = ufloat(312.5,0.05)
T1020_2 = ufloat(281.5,0.05)
T1500_1 = ufloat(319.0,0.05)
T1500_2 = ufloat(277.9,0.05)
def tg(t1,t2):
    return t1/(t1-t2)
print('Theoretische Güte nach 60', tg(T60_1, T60_2), ' 420', tg(T420_1,T420_2), ' 1020', tg(T1020_1, T1020_2), ' 1500', tg(T1500_1,T1500_2))

#Bestimmung der Güte
mw = ufloat(4, 0.0016)
cw = 4186.8
qr = ufloat(750, 10)
qg = mw*cw + qr
wk = ufloat(np.mean(W), np.std(W))
wk = wk*100
print('Leistung des Kompressors', wk)
print("Güte nach 60 sec : ", qg*q1(60)*(1/wk),", Güte nach 420 sec : ", qg*q1(420)*(1/wk),", Güte nach 1020 sec : ", qg*q1(1020)*(1/wk), "Güte nach 1500 sec : ", qg*q1(1500)*(1/wk))

print("----------------------------------------------------------")

#Dampfdruckkurve
bar = [1,2,3,4,5,6,7,8,9,10]
T = [-30,-12,-1,8,15,23,28,33,39,42]
for b in range(10):
    T[b] += 273.2
    T[b] = 1/T[b]
def f(x, a, b):
    return a * x + b
params, covariance = curve_fit(f, T, np.log(bar))
errors = np.sqrt(np.diag(covariance))
print('Steigung: ', params[0], ' +- ', errors[0])
print('Steigung: ', params[1], ' +- ', errors[1])
L = ufloat(params[0], errors[0])
L *= 8.314
plt.plot(T, np.log(bar), 'rx')
x_plot = np.linspace(0.0031, 0.0042)
plt.xlabel(r'1/T')
plt.ylabel(r'log(p/p$_0$)')
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.tight_layout()
plt.savefig('build/Dampfdruck.pdf')
plt.close()

print("----------------------------------------------------------")

#Dichte der Stoffe
pa1  = ufloat(pa[1],10)
pa7  = ufloat(pa[7],10)
pa17 = ufloat(pa[17],10)
pa25 = ufloat(pa[25],10)
pb1  = ufloat(pb[1],10)
pb7  = ufloat(pb[7],10)
pb17 = ufloat(pb[17],10)
pb25 = ufloat(pb[25],10)

def rho(pa,t):
    return (5.51*273.15*pa)/(t*100)
rho1 = rho(pa[1],T60_2) 
rho2 = rho(pa[7],T420_2)
rho3 = rho(pa[17],T1020_2)
rho4 = rho(pa[25],T1500_2)
print('Dichte: ',rho1,rho2,rho3,rho4)

print("----------------------------------------------------------")

#Massendurchsatz
def dm(t):
    return qg*q2(t)*(1/L)
print("Massendurchsatz nach 60 sec : ", dm(60),", nach 420 sec : ", dm(420),", nach 1020 sec : ", dm(1020), " nach 1500 sec : ", dm(1500))

print("----------------------------------------------------------")

#Leistung

def N(pa,pb,r,d):
    return (1/0.14)*(1/r)*((d*120.91)/1000)*(pb*1000*((pa/pb)**(1/1.14))-pa*1000)

print('Leistung ',N(pa1,pb1,rho1,dm(60)), N(pa7,pb7,rho2,dm(420)), N(pa17,pb17,rho3,dm(1020)), N(pa25,pb25,rho4,dm(1500)))

