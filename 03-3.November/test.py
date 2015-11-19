from scipy import stats
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

x = [0.04, 0.065,0.09, 0.115, 0.14, 0.165, 0.19, 0.215, 0.24, 0.265]
y = [12.69, 14.72, 17.52, 19.95,22.95,26.10, 29.50, 32.76, 35.56, 39.24] 
for a in range(10):
	x[a] = x[a]**2
	y[a] = (y[a]/5)**2
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("Steigung = ", slope)
slope_err = ufloat(slope, std_err)
D = 8*(np.pi**2)*0.2217/slope_err
print("Winkelrichtgröße = " , D ,std_err)

print("Eigenträgheitsmoment der Drillachse")
print("Y-Achsen" , intercept)
