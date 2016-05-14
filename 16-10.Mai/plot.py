import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
from uncertainties import ufloat
import math

B_250, B_300, B_350, B_400, B_450 = np.loadtxt('data/B-Feld.txt', unpack=True)
E_230, E_300, E_350, E_180, E_260 = np.loadtxt('data/E-Feld.txt', unpack=True)
