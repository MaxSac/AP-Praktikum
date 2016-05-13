import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy import stats

b_A, e_A, V_A = np.loadtxt('data/abbe.txt', unpack=True)
g_b, b_b = np.loadtxt('data/bekannt.txt', unpack=True)
b_u, g_u = np.loadtxt('data/unbekannt.txt', unpack=True)
b1_bw, b2_bw, e_bw = np.loadtxt('data/besselweiss.txt', unpack=True)
b1_bb, b2_bb, e_bb = np.loadtxt('data/besselblau.txt', unpack=True)
b1_br, b2_br, e_br = np.loadtxt('data/besselrot.txt', unpack=True)

x = np.linspace(0, 25, 100)
y = x ** np.sin(x)
null = [0] * 11

def linear(x,g,b):
    return b - (b/g)  * x

#Bekannnte Linse
plt.plot(g_b, null, 'x', label='Messwerte')
plt.plot(null, b_b, 'x')
for i in range(11):
    plt.plot(x, linear(x,g_b[i],b_b[i]))
plt.plot(10.15,9.4, 'ro', label='Brennweite der Linse')
plt.xlim(0,26)
plt.ylim(0,32)
plt.xlabel(r'Bildweite / cm')
plt.ylabel(r'Gegenstandsweite / cm ')
plt.legend(loc='best')
plt.savefig('build/bekannt.pdf')
plt.close()

#Unbekannte Linse

plt.plot(g_u, null, 'x', label='Messwerte')
plt.plot(null, b_u, 'x')
for i in range(11):
    plt.plot(x, linear(x,g_u[i],b_u[i]))
plt.plot(9.6,14.2, 'ro', label='Brennweite der Linse')
plt.xlim(0,19.4)
plt.ylim(0,41)
plt.xlabel(r'Bildweite / cm')
plt.ylabel(r'Gegenstandsweite / cm ')
plt.legend(loc='best')
plt.savefig('build/unbekannt.pdf')
plt.close()

#Besselmethode Weißes Licht

def bessel(a, ebw, bw1, bw2):
    g1 = [0]*a
    g2 = [0]*a
    d1 = [0]*a
    d2 = [0]*a
    f1 = [0]*a
    f2 = [0]*a
    for x in range(a):
        g1[x] = ebw[x] - bw1[x]
        d1[x] = g1[x] - bw1[x]
        g2[x] = ebw[x] - bw2[x]
        d2[x] = g2[x] - bw2[x]
        f1[x] = round((ebw[x]**2 - d1[x]**2)/(4*ebw[x]),2)
        f2[x] = round((ebw[x]**2 - d2[x]**2)/(4*ebw[x]),2)
        print(x, ' = ', round(f1[x], 2) , " , ", round(f2[x],2) )
    f1_m = [np.mean(f1), np.mean(f2)]
    print('f1 Mittelwert', round(np.mean(f1),2), '+-', round(stats.sem(f1),2))
    print('f2 Mittelwert', round(np.mean(f2),2), '+-', round(stats.sem(f2),2))
    fg = np.append(f1,f2)
    print('f Mittelwert', round(np.mean([f1,f2]),2), '+-', round(stats.sem(fg),2))
    print('f dummer Mittelwert' , round(np.mean(f1_m),2), '+-', round(stats.sem(f1_m),2))
print("Bessel Methode weißes Licht")
bessel(10, e_bw, b1_bw, b2_bw)
print("-")
print("Bessel Methode rotes Licht")
bessel(5, e_br, b1_br, b2_br)
print("-")
print("Bessel Methode blaues Licht")
bessel(5, e_bb, b1_bb, b2_bb)
print("-")

#Abbemethode 

def lin(x,a,b):
        return b + a * x


for x in range (10):
    V_A[x] = V_A[x]/3
g_A = e_A - b_A
params1, cov1 = curve_fit(lin, (1+V_A),b_A)
cov1 = np.sqrt(np.diag(cov1))
print('Abbe Methode f_1 = ', params1[0], '+-', cov1[0], ', h* = ', params1[1], '+-', cov1[1])
plt.plot((1 + V_A), lin((1+V_A), *params1), label='Fit')
plt.plot((1 + V_A), b_A, 'x', label='Messdaten')
plt.xlabel(r'(1+V)')
plt.ylabel(r'Bildweite / cm ')
plt.legend(loc='best')
plt.savefig('build/Abbe1.pdf')
plt.close()

params2, cov2 = curve_fit(lin, (1+1/V_A), g_A)
cov2 = np.sqrt(np.diag(cov2))
print('Abbe Methode f_2 = ', params2[0], '+-', cov2[0], ', h= ', params2[1], '+-', cov2[1])
plt.plot((1 + 1/V_A),lin((1 + 1/V_A), *params2), label='Fit')
plt.plot((1 + 1/V_A), g_A , 'x', label='Messdaten')
plt.xlabel(r'(1 + 1/V)')
plt.ylabel(r'Gegenstandsweite / cm ')
plt.legend(loc='best')
plt.savefig('build/Abbe2.pdf')
plt.close()

print("-------------------------------------------------------")
f_bekannt = [10.4, 10.2, 10.3, 10.2, 10.2, 10.2, 10.1, 10.2, 10.2, 10.2, 10.1]
print("Mittelwert f bekannt = ",np.mean(f_bekannt),"+-", stats.sem(f_bekannt))

V_relativ = [6.6, 3.0, 0, 3.8, 2.3, 7.2, 4.7, 4.2, 3.7, 0.6, 2.1]
print("realtiver Fehler Vergrößerung = ", np.mean(V_relativ), "+-", stats.sem(V_relativ))

f_unbekannt = [9.2, 9.2, 9.2, 9.2, 9.1, 9.0, 9.0, 9.0, 8.9, 8.8, 8.8]
print("Mittelwert f unbekannt", np.mean(f_unbekannt), "+-", stats.sem(f_unbekannt))

f_ab_be = [10.15,9.4]
print("Abgelesen bekannte Brennweitet =", np.mean(f_ab_be), "+-", stats.sem(f_ab_be))
f_ab_ube = [9.6, 14.2]
print("Abgelesen unbekannte Brennweitet =", np.mean(f_ab_ube), "+-", stats.sem(f_ab_ube))
