import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Angehangenes Gewicht
Masse = 1900

#Kraft auf den Stab
f=Masse*9.81







# Datenfile erzeugen
Abstand, mit_Gewicht, ohne_Gewicht = np.genfromtxt('Einseitig_Eckig.txt',unpack=True)

Abstand /=1000

#Durchbiegung des Stabes
durchbiegung = mit_Gewicht - ohne_Gewicht

durchbiegung /= 1000

print ('Ausschlag ohne Gewicht', ohne_Gewicht)

print('')
print('Ausschlag mit Gewicht', mit_Gewicht)

print('')
print ('Durchbiegung: ', durchbiegung)

print('')
print (Abstand)

def EModul(L, x):
	return (L*(x**2)-x**3/3)

#erstellt Ausgleichsgerade
def func(m, x, b):
	return  m * x + b

#dies dient zum testen der curve_fit Funktion
BspEM = EModul(0.51 ,Abstand)

parameters, pcov = curve_fit(func, durchbiegung, BspEM)


print('')
print ('L*x**2-x**3/3: ', BspEM)


d=0
for x in Abstand:
	print(d)
	print('Abstand: ',Abstand[d],' Auslenkung o Ge: ', ohne_Gewicht[d], ' Auslenkung m Ge: ',  mit_Gewicht[d], ' Differenz m-o: ', durchbiegung[d], ' f(x): ', BspEM[d] )
	d +=1

print('')
print (parameters)
#plt.errorbar(durchbiegung, BspEM, xerr=0.1, yerr=0.01, fmt='x')
plt.plot(durchbiegung, BspEM, 'x')
plt.plot(durchbiegung, func(durchbiegung, *parameters))
plt.xlabel(r'Durchbiegung in [1/m]')
plt.ylabel(r'Lx² - x³/3in [1/m]')
plt.show()
