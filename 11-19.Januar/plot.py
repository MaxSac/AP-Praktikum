import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

#Kenngrößen
L = 23.954*10**(-3)
C = 0.7932*10**(-9)
C_Sp = 0.028*10**(-9)
C_K_A = [12*10**(-9), 9.99*10**(-9), 8.18*10**(-9), 6.86*10**(-9), 4.74*10**(-9), 2.86*10**(-9), 2.19*10**(-9), 0.997*10**(-9)]
C_K_err = [0.06*10**(-9), 0.04*10**(-9), 0.04*10**(-9), 0.03*10**(-9), 0.02*10**(-9), 0.01*10**(-9), 0.01*10**(-9), 0.005*10**(-9)]
C_K = unp.uarray(C_K_A, C_K_err)

vtp = 1/(2*np.pi*np.sqrt(L*(C + C_Sp)))
print("vtp = ", vtp)
def vtm(CK):
    return 1/(2*np.pi*((L*((1/C + 2/CK)**(-1) + C_Sp))**(0.5)))
for x in range(8):
    print("v_t^- für den Kodensator ", C_K[x], " = ", vtm(C_K[x]))
    print("n_t", (vtp + vtm(C_K[x]))/(2*(vtm(C_K[x]) - vtp)))
print("-----------------------------------------------------------------")

startf = ufloat(30.12*10**3, 0.01*10**3)
endf = ufloat(60.98*10**3, 0.01*10**3)
beepf = endf - startf
vtm2 = unp.uarray((0.176,0.168,0.160,0.176,0.160,0.176,0.176,0.176),0.002) 
vtp2 = unp.uarray((0.240,0.256,0.264,0.312,0.328,0.432,0.512,0.816),0.002)
def beeptofreq(vt):
    return startf + vt*beepf
for x in range(8):
    print("v_t^- für den Kodensator ", C_K[x], " = ", beeptofreq(vtm2[x]))
print(" ")
for x in range(8):
    print("v_t^- für den Kodensator ", C_K[x], " = ", beeptofreq(vtp2[x]))

