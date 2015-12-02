import matplotlib.pyplot as plt
import numpy as np

U_1 = [6.5, 5.5, 2.5, 0.5, -3.5, -6.0, -7.0, -5.5, -2.5, 0.5, 3.5, 6.0]
P_1 = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
gain_1 = 200

U_1t = (2/np.pi)*0.052
for x in range(12):
    U_1[x] /= gain_1
    P_1[x] *= (np.pi / 180)
    print("Phase = ", P_1[x], " U_out = ", U_1t*np.cos(P_1[x]), "Praktisch = ", U_1[x]/gain_1)

k= np.linspace(0, 5.76)
plt.plot(k, U_1t*np.cos(k), label=r'theoretisch')
plt.plot(P_1, U_1, 'rx', label=r'praktisch')
plt.legend(loc='best')
plt.xlabel(r'Phase in rad')
plt.ylabel(r'Spannung / V')
plt.tight_layout()
plt.savefig('build/Spannungsverlauf.pdf')
plt.close()
