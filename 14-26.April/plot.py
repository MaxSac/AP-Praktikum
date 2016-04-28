import matplotlib.pyplot as plt
import numpy as np

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

