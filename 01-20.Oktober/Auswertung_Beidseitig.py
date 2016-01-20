import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Datenfile erzeugen
x, d_o_1, d_m_1, d_o_2, d_m_2 = np.genfromtxt('Beidseitig.txt',unpack=True)

#Länge des Balkens
L = 0.58

#rechnet von mm in m um
x /=1000
x = L/2 + x

#Mittelwert der beiden Messwerte
d_o = (d_o_1 + d_o_2)/2
d_m = (d_m_1 + d_m_2)/2

#Durchbiegung des Stabes
du = d_m_1 - d_o_1
du /= 1000

#berechnet f(x)
def EModul(L, x):
	return (4*x**3-12*L*x**2+9*L**2*x-L**3)

#erstellt Ausgleichsgerade
def func(m, x, b):
	return  m * x + b

#dies dient zum testen der curve_fit Funktion
BspEM = EModul(L ,x)

parameters, pcov = curve_fit(func, du, BspEM)

#Textausgabe:
d=0
for z in x:
	print(d)
	print('Abstand: ',x[d],' Auslenkung gemittelt o Ge: ', d_o[d], ' Auslenkung m Ge: ', d_m[d], ' Differenz m-o: ', du[d], ' f(x): ', BspEM[d] )
	d +=1

print('')
print (parameters)
#plt.errorbar(durchbiegung, BspEM, xerr=0.1, yerr=0.01, fmt='x')
plt.plot(du, BspEM, 'x')
plt.plot(du, func(du, *parameters))
plt.xlabel(r'Durchbiegung in [1/m]')
plt.ylabel(r'Lx² - x³/3in [1/m]')
plt.show()
