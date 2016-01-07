import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat

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
#Der Fehler ist 0.60 0.03 0.68
plt.legend(loc="best")
plt.xlabel('t / 100 µs')
plt.ylabel('U / in Volt')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

f = ufloat(680, 60)
L = ufloat(0.01678,0.00009)
print('effektiver Dämpfungswiederstand', f*L*np.pi*4)
print('Abklingdauer', 1/(np.pi*2*f))
