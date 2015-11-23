import numpy as np
from scipy import stats
from scipy.stats import sem
from uncertainties import ufloat
import uncertainties.unumpy as unp
import math




#Bestimmung der Winkelrichtgöße D
a = [91.10, 90.80, 90.10]
print("Die werte sind: ", a)
	#Mittelwert
average = sum(a)/len(a)
variance = np.var(a)
devitation = np.sqrt(variance)
a = ufloat(average, devitation)
a /= 1000
print("Mittelwert Strecke für D:", a)
def wg (F, phi):
	D = F * a / phi
	return D
WinkelG = [15,30,45,50,60,75,90,105,120,135]
WinkelB = np.zeros(10)
for i in range(10):
	WinkelB[i] = math.radians(WinkelG[i])
	print(WinkelB[i])
	#Ableseunsicherheit des Winkels
Unsicherheit = np.ones(10)
Unsicherheit = Unsicherheit/(2*np.pi)
Winkel = unp.uarray(WinkelB, Unsicherheit)
	#Ableseunsicherheit der Kraft
U2= np.ones(10)
U2= U2/50
Kraft = [0.06, 0.12, 0.15, 0.22, 0.28, 0.34, 0.37, 0.44, 0.51, 0.56]
F = unp.uarray(Kraft, U2)
#Winkelrichtgröße
hilfe = ufloat(0,0)
for x in range(10):
	hilfe += wg(F[x],Winkel[x])
D = hilfe/10
print("Die Winkelrichtgröße D ist :", D)






#Mittelwert Durchmesser Masseloser Stab
M_S = unp.uarray([5.00, 4.62, 5.00, 5.00, 5.00],[0.02,0.02,0.02,0.02,0.02])
M_S = sum(M_S)/len(M_S)
print("Mittelwert Masseloser Stab", M_S)
	# Mittelwert kleiner Zylinder
kZ = unp.uarray([34.92,35,34.94,34.98],0.02)
kZ = sum(kZ)/(len(kZ)*1000)
kZR = kZ/2000
kZL = unp.uarray([29.92,29.90,29.90,30],0.02)
kZL = sum(kZL)/(len(kZL)*1000)
	#abstand von drehachse
a_w = unp.uarray([25+15,50+15,75+15,100+15,125+15,150+15,175+15,200+15,225+15,250+15],30)
a_w /= 1000
print("Abstände: ", a_w)
	#Trägheitsmoment Gewichte
I_G = unp.uarray([0,0,0,0,0,0,0,0,0,0],0)
for x in range(10):
	print("Abstand: ", a_w[x], "Radius Kreis:", kZR, "Länge des Zylinders ", kZ)
	I_G[x] = 0.22174*((kZR**2)/4 + (kZ**2)/12)+0.22174*(a_w[x]**2)
	print("Das Trägheitsmoment des", x, " Zylindermir Abstand ",a_w[x],": ", I_G[x])




#Trägheitsmoment Drillachse
T = [12.69, 14.73, 17.52, 19.95, 22.95, 26.10, 29.50, 32.76, 35.56, 39.24]
for x in range(10):
	T[x] = T[x] / 5
I_Di = unp.uarray([0,0,0,0,0,0,0,0,0,0],0)
I_S = 2.85*10**(-3)
print("D =", D," T: ", T[0]," I_G[0] ", I_G[0], "I_S", I_S)
for x in range(10):
	I_Di[x] = ((D * ((T[x] / (2*np.pi))**2)) -  (2*I_G[x]))
	# I_Di[x] = I_Di[x]
	print(x,"Trägheitsmoment der Drillachse: ", I_Di[x])
I_D = sum(I_Di)/10
print("Mittelwert des Trägheitsmoment: ", I_D)
#Trägheitsmoment mittels linerarer Regression
T2 = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
	 T2[x] = T[x]*T[x]
a_w2 = a_w**2
slope, intercept, r_value, p_value, std_err = stats.linregress(a_w2.n,T2)
print("Steigung der Regressionsgraden:", slope)








#Kugel
R_K = unp.uarray([137.2,136.9,137.6,138,137.5],0.05)
average = sum(R_K)/(len(R_K)*2000)
print("Mittelwert des Radiuses der Kugel:",average)
I_K = ufloat(0,0)
I_K = 2/5*0.8126*(average**2)
print("Trägheitsmoment der Kugel", I_K)
T_K = [8.52,8.64,8.58,8.6,8.6]
average = sum(T_K)/len(T_K)
variance = np.sqrt(np.var(T_K))
T_K = ufloat(average, variance)
T_K /= 5
print("Periodendauer: ", T_K)
I_K_P = ((T_K/(2*np.pi))**2)*D
print("Praktische Trägheitsmoment ", I_K_P)




#Zylinder
R_Z = unp.uarray([80,80,80,80],0.02)
average = sum(R_Z)/(len(R_Z)*2000)
print("Mittelwert des Radiuses der :Zylinders",average)
I_Z = ufloat(0,0)
I_Z = 1/2*1.974*(average**2)
print("Trägheitsmoment des Zylinders", I_Z)
T_Z = [8.4,8.32,8.49,8.30,8.35]
average = sum(T_Z)/len(T_Z)
variance = np.sqrt(np.var(T_Z))
T_Z = ufloat(average, variance)
T_Z /= 5
print("Periodendauer: ", T_Z)
I_Z_P = ((T_Z/(2*np.pi))**2)*D
print("Praktische Trägheitsmoment Zylinder ", I_Z_P)



#Puppe
def vol(h , d):
	h /= 1000
	d /= 1000
	k = np.pi/4*h
	l = d**2
	return k*l

def ave(x):
	xm = sum(x)/len(x)
	xv = np.sqrt(np.var(x))
	return ufloat(xm, xv)

z1_h = [56.38,56.29,55.30]
z1_d = [29.42,30.4,27.92,23.34,11.20]
z2_h = [98.6, 100.1, 96.9, 92.68, 97.82]
z2_d = [41.3, 39.82, 35.54, 25.36, 26, 35.02, 37.34, 39.74]
z3_h = [146.98, 155.0, 145.98, 147.04, 154.76]
z3_d = [12.1, 20.7, 16.00, 12.92, 16.36, 14.72]
z5_h = [138.54, 140.68, 139.02, 140.00]
z5_d = [16.06, 16.32, 12.96, 11.00, 14.72, 7.46]
print("Höhe Z1_h",ave(z1_h))
print("RAdius Z1",ave(z1_d))
print("Volumen z1!",vol(ave(z1_h),ave(z1_d)))
print("Höhe Z2_h",ave(z2_h))
print("RAdius Z2",ave(z2_d))
print("Volumen z2!",vol(ave(z2_h),ave(z2_d)))
print("Höhe Z3_h",ave(z3_h))
print("RAdius Z3",ave(z3_d))
print("Volumen z3!",vol(ave(z3_h),ave(z3_d)))
print("Höhe Z5_h",ave(z5_h))
print("RAdius Z5",ave(z5_d))
print("Volumen z5!",vol(ave(z5_h),ave(z5_d)))
volg = ( vol(ave(z1_h),ave(z1_d)) + vol(ave(z2_h),ave(z2_d)) + 2*vol(ave(z3_h),ave(z3_d)) + 2*vol(ave(z5_h),ave(z5_d)))
print("Gesamtvolumen", volg)
M = 0.1627
rho = M / volg
m1= rho*vol(ave(z1_h),ave(z1_d))
m2= rho*vol(ave(z2_h),ave(z2_d))
m3= rho*vol(ave(z3_h),ave(z3_d))
m5= rho*vol(ave(z5_h),ave(z5_d))
print("m1 ",m1,"m2 ",m2,"m3 ",m3,"m5 ",m5)

#Trägheitsmoment einzelner Zylinder
z1= 0.125*m1*(ave(z1_d)**2)
z2= 0.125*m2*(ave(z2_d)**2)
z3= 0.125*m3*(ave(z3_d)**2) + 0.25*m3*(ave(z3_d)**2)
z5= 0.125*m5*(ave(z5_d)**2) + 0.25*m5*(ave(z5_d)**2) + 0.25*m5*(ave(z2_d)**2)
z5_= m5*((ave(z5_d)**2)/16+ ((ave(z5_h)**2)/48)) +m5*0.25*((ave(z5_h)+ave(z2_d))**2)
zges = (z1 + z2 + 2*z3 + 2*z5)*(10**(-6))
zges_= (z1 + z2 + 2*z3 + 2*z5_)*(10**(-6))
print( z1, z2, z3, z5, zges)
print( z1, z2, z3, z5_, zges_)




T_Pau = [3.84,3.64,3.87,3.83,3.84]
T_Pan = [2.80, 3.0, 3.01, 2.9, 2.87]
print("Mittelwert Schwingungsdauer Puppe ausgestreckte ARme", ave(T_Pau)/5)
print("Mittelwert Schwingungsdauer Puppe angelegte Arme!", ave(T_Pan)/5)
I_PmaA = D*((ave(T_Pan)/(5*2*np.pi))**2)
print("Experimentelles Trägheitsomoment I_PmaA", I_PmaA)
I_PmauA = D*((ave(T_Pau)/(5*2*np.pi))**2)
print("Experimentelles Trägheitsomoment I_PmauA", I_PmauA)
