import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

U_1, I1, I2 = np.loadtxt('Diode1.txt', unpack=True)
U_2, I3, I4, I5 = np.loadtxt('Diode2.txt', unpack=True)
U1 = 6.2 #V
U2 = 6.0 #V
U3 = 5.0 #V
U4 = 4.4 #V
U5 = 4.0 #V

'''
plt.plot(U_1, I1, 'rx', label='$I_1$')
plt.plot(U_1, I2, 'gx', label='$I_2$')
plt.ylabel('I / mA')
plt.xlabel('U / V')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Diode1.pdf')
plt.close()

plt.plot(U_2, I3, 'bx', label='$I_3$')
plt.plot(U_2, I4, 'kx', label='$I_4$')
plt.plot(U_2, I5, 'yx', label='$I_5$')
plt.ylabel('I / mA')
plt.xlabel('U / V')
plt.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('build/Diode2.pdf')
plt.close()
'''
