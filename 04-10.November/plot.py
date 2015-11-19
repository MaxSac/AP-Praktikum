import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import math
from uncertainties import ufloat
# 1 mm sind 0.238 Kelvin
x = 0.03
rhoM = 8520 
rhoA = 2800
cM = 285
cA = 830
xM = 0.238
xA = 0.208
# 1 mm sin in sec
y = 4.348
MA1 = [12, 21, 19, 19, 18, 18, 17, 17, 17, 16]
MA2 = [13, 11, 10, 9, 9, 9, 9, 8, 8, 8]
MA = [0] * 10
PM = np.array([2,2,2,2,2,3,3,3,3,4])
PM *= y
AA2 = [17, 14, 13, 11, 11, 11, 10, 10, 10, 10]
AA1 = [32, 34, 33, 31, 32, 31, 31, 30, 30, 30]
AA = [0]*10
PA = np.array([1, 1, 2, 2, 2, 2, 2, 1, 2, 2])
PA *= y
for a in range(10):
	MA1[a] = MA1[a] * xM
	print(a," Temperatur T1: ", MA1[a])
	MA2[a] = MA2[a] * xM
	print(a," Temperatur T2: ", MA2[a])
	MA[a] = math.log((MA1[a]/MA2[a]))
	print(a, " ln A1/A2 = ", MA[a])
	print(a, " Phasenverschiebung: ", PM[a])
print("---------------------------------------------------------------------")
for a in range(10):
        AA1[a] = AA1[a] * xA
        print(a," Temperatur T1: ", AA1[a])
        AA2[a] = AA2[a] * xA
        print(a," Temperatur T2: ", AA2[a])
        AA[a] = math.log((AA1[a]/AA2[a]))
        print(a," ln A1/A2 = ", AA[a])
for a in range(10):
	print(a," Phasenverschiebung: ", PA[a])
print("---------------------------------------------------------------------")
lnM = ufloat(np.mean(MA),np.std(MA))
lnA = ufloat(np.mean(AA),np.std(AA)) 
print("lnA: ", lnA, "lnM: ", lnM)
tM = ufloat(np.mean(PM), np.std(PM))
tA = ufloat(np.mean(PA), np.std(PA))
print("delta t M: ", tM, " delta t A: ", tA) 
print("---------------------------------------------------------------------")
kM = (rhoM*cM*(x**2))/(2*tM*lnM)
print("Wärmeleitfähigkeit von Messing: ", kM)
kA = (rhoA*cA*(x**2))/(2*tA*lnA)
print("Wärmeleitfähigkeit von Aluminium: ", kA)
print("---------------------------------------------------------------------")
