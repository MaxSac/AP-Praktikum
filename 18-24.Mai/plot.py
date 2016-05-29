import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import scipy.constants as c
import math
from lmfit import minimize, Parameter, Model

def w(T):
    T += 273
    return 0.0029*10**(-2)/((10**7*5.5)*math.exp((-6876/T)))

print('Mittelere freie Wellenlänge T = 27 ', w(27), 0.01/w(27))
print('Mittelere freie Wellenlänge T = 105 ', w(105), 0.01/w(105))
print('Mittelere freie Wellenlänge T = 140 ', w(140), 0.01/w(140))
print('Mittelere freie Wellenlänge T = 180 ', w(180), 0.01/w(180))
print('Mittelere freie Wellenlänge T = 190 ', w(190), 0.01/w(190))
