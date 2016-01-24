import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math
"""
t, U = np.loadtxt('data2.txt', unpack=True)
t *= 10000

#Sucht nach Maxima
#maxs = find_peaks_cwt(U, np.linspace(1, 5, 3000), min_snr=1, noise_perc=100)
#mins = find_peaks_cwt(-U, np.linspace(1, 5, 3000), min_snr=1,  noise_perc=100)
#for x in range(30):
#    print('Maxima',t[mins[x]],U[mins[x]])

maxsU = [ 52, 48.8, 45.6, 41.6, 38.4, 36.6, 34.2, 33.3 , 32, 31.4, 29.6, 28.8]
maxst = [ 0.182, 0.544, 0.926, 1.3, 1.69, 2.086, 2.46, 2.82 , 3.2, 3.59, 3.96, 4.32]
minsU = [-9.6, -4.8, -0.8, 2.4, 4.8, 7, 9.3, 11.8, 12.8, 14.5, 14.5, 15.4, 16.0]
minst = [0.002, 0.37, 0.75, 1.116, 1.494, 1.876, 2.25, 2.62, 3.0, 3.4, 3.76, 4.15, 4.514]

#Funktion des Fittes
x = np.linspace(0, 5, 50)
def e(x, a, b, c):
    return a * np.exp(-b * x) + c

#Fittet Kurve durch Extrema
params, covariance = curve_fit(e, maxst, maxsU)
print(params, np.sqrt(np.diag(covariance)), sep='\n')

#Plotet Messwerte
plt.plot(t, U, 'b-', label='Gedämpfte Schwingung')
plt.plot(maxst, maxsU, 'go', label='Maxima')
plt.plot(minst, minsU, 'ro', label='Minima')
plt.plot(x, e(x, 30.63, 0.43, 24.20), 'g-', label='Obere Einhüllende')
#Der Fehler ist 0.95 0.04 1.17
plt.plot(x, e(x, -29.49, 0.46, 19.91), 'y-', label='Untere Einhüllende')
#Der Fehler ist 0.60, 0.03, 0.68
plt.legend(loc="best")
plt.xlabel('t / 100 µs')
plt.ylabel('U / in Volt')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
plt.close()
print("--------------------------------------------------------")

f = ufloat(680, 60)
L = ufloat(0.01678,0.00009)
print('effektiver Dämpfungswiederstand', f*L*np.pi*4)
print('Abklingdauer', 1/(np.pi*2*f))
print("--------------------------------------------------------")

L1 = ufloat(0.00353,0.00003)
C1 = ufloat(5.075*10**(-6),0.01*10**(-6))
R_ap_2 = ((4*L1)/C1)
R2 = ufloat(682, 1)
print("R_ap = ", R_ap_2**0.5)
print("--------------------------------------------------------")
"""
f, UC, phi = np.loadtxt("data.txt", unpack=True)
w = f * 2 * math.pi
L = 16.78 * 10**(-3)
C = 2.066 * 10**(-9)
R = 682
U0 = 7

U = U0 / ((1-L*C*(w**2))**2 + (w**2)*(R**2)*(C**2))**(0.5)

def Uso(x, a, b, c):
    return  c / (((1-a*(x**2))**2 + (x**2)*(b**2))**(0.5))

params, cov = curve_fit(Uso, w, UC)

print("Paramter: ",params, "Werte: ", Uso(w, *params))

plt.xscale('log')
plt.errorbar(w, UC, yerr=0.1, fmt='x', label='Messwerte')
plt.plot(w, U, 'r-', label='theo Wert')
plt.plot(w, Uso(w, *params), 'b-', label='Fit')
plt.ylabel('U / V')
plt.xlabel('$\omega$ / Hz')
plt.xlim(8, 400000)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot1.pdf')
plt.close()
"""
print("--------------------------------------------------------")

def FOO(x):
  return (1/(2**0.5))*(x/x)
fx = np.linspace( 8, 56000, 100)

plt.plot(f, UC, 'x', label='Messwerte')
plt.plot(f, 28.4*FOO(f), 'r--', label=r'$ U_{max}\frac{1}{\sqrt{2}} $')
plt.plot([22470,22470], [0, 30], 'g--', lw=1, label=r'Halbwertsbreite')
plt.plot([29200,29200], [0, 30], 'g--', lw=1)
plt.ylabel('U / V')
plt.xlabel('f / Hz')
plt.xlim(15000, 35000)
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/plot2.pdf')
plt.close()
print("--------------------------------------------------------")

L2 = ufloat(0.01678,0.00009)
C2 = ufloat(2.066*(10**(-9)), 0.006*(10**(-9)))
R2 = ufloat(682,1)
print("Theoretische Güte", 1/(((1/(L2*C2))**(-0.5))*R2*C2))
print("--------------------------------------------------------")

for x in range(36):
    phi[x] = (phi[x]*(10**(-6)))/(1/f[x])*2*np.pi
    print('Frequenz: ', f[x], 'phi', phi[x])

plt.xscale('log')
plt.plot(f, phi, 'x', label='Messwerte')
plt.ylabel(r'$\Phi$ / rad')
plt.xlabel('f / Hz')
plt.xlim(8, 55500)
plt.ylim(-0.1, 3.5)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot3.pdf')
plt.close()
print("--------------------------------------------------------")

plt.plot(f, phi, 'x', label='Messwerte')
plt.ylabel(r'$\Phi$ / rad')
plt.xlabel('f / Hz')
plt.plot([26800,26800], [0, 3.3], 'g--', lw=1, label=r'q_{\text{Resonanz}}')
plt.plot([23700,23700], [0, 3.3], 'y--', lw=1, label=r'$f_1$ und $f_2$')
plt.plot([29970,29970], [0, 3.3], 'y--', lw=1)
plt.xlim(10000, 40000)
plt.ylim(0, 3.2)
plt.yticks([0, 0.25*np.pi, 0.5 * np.pi, (3/4) * np.pi  ,np.pi ],[r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/plot4.pdf')
plt.close()

C3 = ufloat(2.066,0.006)*10**(-9)
R3 = ufloat(682,1)
w0 = 26300*(np.pi*2)
print("Güte experimentell = ", 1/(w0*R3*C3))
"""
