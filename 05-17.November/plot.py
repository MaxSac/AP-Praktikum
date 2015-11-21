import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Einlesen der Daten
t, T1, pb, T2, pa, W = np.loadtxt('data.txt', unpack=True)
t = t*60

#Temperaturplot
plt.plot(t, T2, 'g.', label=r'$T2$')
plt.plot(t, T1, 'r.', label=r'$T1$')
plt.xlabel(r'Zeit / s')
plt.ylabel(r'Temperatur / K')
plt.legend()
plt.tight_layout()
plt.savefig('build/TVerlauf.pdf')
plt.close()


#Ausgleichsgraden Plot
z1 = np.polyfit(t, T1, 2)
z2 = np.polyfit(t, T2, 2)
print('Koefizienten zur Funktion von T1: ', z1)
print('Koefizienten zur Funktion von T2: ', z2)
p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
xp = np.linspace(0, 2000, 100)
plt.plot(xp, p1(xp), 'b-', label=r'T1')
plt.plot(xp, p2(xp), 'r-', label=r'T2')
plt.xlabel(r'Zeit / s')
plt.ylabel(r'Temperatur / K')
plt.legend()
plt.tight_layout()
plt.savefig('build/Ausgleichsgrade.pdf')
plt.close()

print("-----------------------------------------------------------")

#Differentialquotient
def q1(t):
    return 2*z1[0]*t + z1[1]
def q2(t):
    return 2*z2[0]*t + z2[1]
print('DiffQ T1', '60: T', p1(60),' dq 60', q1(60), ', 400:', p1(400),' dq 400', q1(400), ', 1000:', p1(1000), 'dq 1000', q1(1000), ', 1500:', p1(1500),'dq 1500 ', q1(1500))
print('DiffQ T2', '60: T', p2(60),' dq 60', q2(60), ', 400:', p2(400),' dq 400', q2(400), ', 1000:', p2(1000), 'dq 1000', q2(1000), ', 1500:', p2(1500),'dq 1500 ', q2(1500))

print("-----------------------------------------------------------")

#Bestimmung der Güte
mw = ufloat(4, 0.0016)
cw = 4200
qr = ufloat(750, 10)
qg = mw*cw + qr
wk = ufloat(np.mean(W), np.std(W))
wk = wk*100
print("Güte nach 60 sec : ", qg*q1(60)*(1/wk),", Güte nach 400 sec : ", qg*q1(400)*(1/wk),", Güte nach 1000 sec : ", qg*q1(1000)*(1/wk), "Güte nach 1500 sec : ", qg*q1(1500)*(1/wk))

print("----------------------------------------------------------")

#Dampfdruckkurve
bar = [4,5,6,7,8,9,10]
T = [8,14,23,28,33,39,42]
for b in range(7):
    T[b] += 273.2
def f(x, a, b):
    return a * x + b
params, covariance = curve_fit(f, T, (1/np.log(bar)))
errors = np.sqrt(np.diag(covariance))
print('Steigung: ', params[0], ' +- ', errors[0])
print('Steigung: ', params[1], ' +- ', errors[1])
plt.plot(T, 1/np.log(bar), 'rx')
x_plot = np.linspace(280, 330)
plt.plot(x_plot, f(x_plot, *params), 'b-', label='linearer Fit')
plt.tight_layout()
plt.savefig('build/Dampfdruck.pdf')
plt.close()
