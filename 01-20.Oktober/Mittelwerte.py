from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

x = [10,10,10,10,10,10,10,10,10,10]
err = [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
x_err = unp.uarray(x, err)
print ('Mittelwert',x_err)
