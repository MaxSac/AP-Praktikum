import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

U_1 = [6.5, 5.5, 2.5, 0.5, -3.5, -6.0, -7.0, -5.5, -2.5, 0.5, 3.5, 6.0]
P_1 = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
gain_1 = 200

U_1t = (2/np.pi)*0.052
for x in range(12):
    U_1[x] /= gain_1
    P_1[x] *= (np.pi / 180)
    print("Phase = ", P_1[x], " U_out = ", U_1t*np.cos(P_1[x]), "Praktisch = ", U_1[x])

k= np.linspace(0, 5.76)
plt.plot(k, U_1t*np.cos(k), label=r'theoretisch')
plt.plot(P_1, U_1, 'rx', label=r'praktisch')
plt.legend(loc='best')
plt.xlabel(r'Phase in rad')
plt.ylabel(r'Spannung / V')
plt.tight_layout()
plt.savefig('build/Spannungsverlauf.pdf')
plt.close()

print("---------------------------------------------------------------")

U_2 = [6.5, 5.5, 2.0, 0.0, -3.5, -6.0, -6.5, -6.0, -3.0, 0.5, 3.5, 6.0]
gain_2 = 200
for x in range(12):
        U_2[x] /= gain_2
        print("Phase = ", P_1[x], "Praktisch = ", U_2[x])

k= np.linspace(0, 5.76)
plt.plot(k, U_1t*np.cos(k), label=r'theoretisch')
plt.plot(P_1, U_2, 'rx', label=r'praktisch')
plt.legend(loc='best')
plt.xlabel(r'Phase in rad')
plt.ylabel(r'Spannung / V')
plt.tight_layout()
plt.savefig('build/Spannungsverlauf2.pdf')
plt.close()
               
print("---------------------------------------------------------------")

r = [0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4,1.5, 1.6, 1.7, 1.8]
U_3 = [4,5.5,2,2,2,1,1,6.5,5.0,4.0,3.0,2.5,2,3,2.5,2,5.5,5.0,4.5]
gain_3 = [500, 1000, 500, 1000, 1000, 1000, 2000, 10000, 10000, 10000, 10000, 10000, 10000, 20000, 20000, 20000, 50000, 50000, 50000]
U_null = -1/1000 
for x in range(19):
    r[x] *= 100
    U_3[x] /= gain_3[x]
    U_3[x] -= U_null
def f(x, a, b):
    return a * x + b
params, covariance = curve_fit(f, np.log(r), np.log(U_3))
U_ber = (np.exp(1)**params[1])*(r**params[0])

plt.plot(np.log(r), np.log(U_ber), 'b-', label='linearer Fit')
plt.plot(np.log(r), np.log(U_3), 'rx', label=r'Messungen')
plt.legend(loc='best')
plt.xlabel(r'ln(r) in cm')
plt.ylabel(r'ln(U) in V')
plt.tight_layout()
plt.savefig('build/Abstand.pdf')
plt.close()
errors = np.sqrt(np.diag(covariance))
print('Steigung der Ausgleichsgrade', params[0], '±', errors[0], 'y-achsen Abschnitt ', params[1], '±', errors[1])

print("---------------------------------------------------------------")
