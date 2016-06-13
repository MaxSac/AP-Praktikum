import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model
from scipy import stats

def w(T):
    T += 273
    return 0.0029*10**(-2)/((10**7*5.5)*math.exp((-6876/T)))

print('Mittelere freie Wellenlänge T = 27 ', w(27), 0.01/w(27))
print('Mittelere freie Wellenlänge T = 105 ', w(105), 0.01/w(105))
print('Mittelere freie Wellenlänge T = 140 ', w(140), 0.01/w(140))
print('Mittelere freie Wellenlänge T = 180 ', w(180), 0.01/w(180))
print('Mittelere freie Wellenlänge T = 190 ', w(190), 0.01/w(190))
print('---------------------------------------------------------')

x1, y1, x2, y2 = np.loadtxt('data.txt', unpack=True)

plt.plot(x1, y1, 'rx')
plt.xlabel(r'Bremsspannung $U_\text{A}$ / V')
plt.xlim(0,10.2)
plt.ylim(0,10)
plt.ylabel(r'$\Delta x / \Delta y$')
plt.tight_layout()
plt.savefig('build/20Grad.pdf')
plt.close()

plt.plot(x2, y2, 'rx')
plt.xlabel(r'Bremsspannung $U_\text{A}$ / V')
plt.xlim(0,10)
plt.ylim(0,2)
plt.ylabel(r'$\Delta x / \Delta y$')
plt.tight_layout()
plt.savefig('build/140Grad.pdf')
plt.close()

U = [4.62,4.37,4.62,4.62,4.86,4.86,4.86,5.34]
print('Sem ( U ):',stats.sem(U))
