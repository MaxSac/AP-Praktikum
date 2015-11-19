import matplotlib.pyplot as plt
import numpy as np

t, T1, pb, T2, pa, W = np.loadtxt('data.txt', unpack=True)
plt.plot(t, T2, 'go', label=r'$T2$')
plt.plot(t, T1, 'ro', label=r'$T1$')
plt.xlabel(r'Zeit / s')
plt.ylabel(r'Temperatur / K')
plt.legend()
plt.tight_layout()
plt.savefig('build/TVerlauf.pdf')
