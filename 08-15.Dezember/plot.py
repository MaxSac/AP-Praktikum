import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy import stats
import pylab
import math

print('------------------------------------------------------------------------')
print('Nr. a, Rx = Wert13')
#1
aR2 = ufloat(332 , 332 * 0.002)
aR3 = 493
aR4 = aR3 / (1000 - aR3)
aR4 = ufloat(aR4, aR4 * 0.005)
aR1x = aR2 * aR4

#2
aR2 = ufloat(500 , 500 * 0.002)
aR3 = 391
aR4 = aR3 / (1000 - aR3)
aR4 = ufloat(aR4, aR4 * 0.005)
aR2x = aR2 * aR4

#3
aR2 = ufloat(664 , 664 * 0.002)
aR3 = 336
aR4 = aR3 / (1000 - aR3)
aR4 = ufloat(aR4, aR4 * 0.005)
aR3x = aR2 * aR4

aRx = (aR1x + aR2x + aR3x) / 3
print('aR1x =', aR1x, ' aR2x =', aR2x, ' aR3x =', aR3x, ' aRx =', aRx)

print('--------------------')
print('Nr. a, Rx = Wert14')
#1
aR2 = ufloat(332 , 332 * 0.002)
aR3 = 735
aR4 = aR3 / (1000 - aR3)
aR4 = ufloat(aR4, aR4 * 0.005)
aR1x = aR2 * aR4

#2
aR2 = ufloat(500 , 500 * 0.002)
aR3 = 648
aR4 = aR3 / (1000 - aR3)
aR4 = ufloat(aR4, aR4 * 0.005)
aR2x = aR2 * aR4

#3
aR2 = ufloat(664 , 664 * 0.002)
aR3 = 582
aR4 = aR3 / (1000 - aR3)
aR4 = ufloat(aR4, aR4 * 0.005)
aR3x = aR2 * aR4

aRx = (aR1x + aR2x + aR3x) / 3
print('aR1x =', aR1x, ' aR2x =', aR2x, ' aR3x =', aR3x, ' aRx =', aRx)

print('------------------------------------------------------------------------')
print('Nr. b, Cx = Wert2')
#1
bC2 = ufloat(597 * 10**(-9) , (597 * 10**(-9)) * 0.002)
bR3 = 285
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC1x = bC2 * bR4
#2
bC2 = ufloat(750 * 10**(-9) , (750 * 10**(-9)) * 0.002)
bR3 = 329
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC2x = bC2 * bR4
#3
bC2 = ufloat(994 * 10**(-9) , (994 * 10**(-9)) * 0.002)
bR3 = 395
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC3x = bC2 * bR4

bCx = (bC1x + bC2x + bC3x) / 3
print('bC1x =', bC1x, ' bC2x =', bC2x, ' bC3x =', bC3x, ' bCx =', bCx)

print('--------------------')
print('Nr. b, Cx = Wert3')
#1
bC2 = ufloat(597 * 10**(-9) , (597 * 10**(-9)) * 0.002)
bR3 = 593
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC1x = bC2 * bR4
#2
bC2 = ufloat(750 * 10**(-9) , (750 * 10**(-9)) * 0.002)
bR3 = 639
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC2x = bC2 * bR4
#3
bC2 = ufloat(994 * 10**(-9) , (994 * 10**(-9)) * 0.002)
bR3 = 705
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC3x = bC2 * bR4

bCx = (bC1x + bC2x + bC3x) / 3
Wert3 = bCx
print('bC1x =', bC1x, ' bC2x =', bC2x, ' bC3x =', bC3x, ' bCx =', bCx)

print('--------------------')
print('Nr. b, Rx,Cx = Wert8')
#1
bC2 = ufloat(597 * 10**(-9) , (597 * 10**(-9)) * 0.002)
bR3 = 671
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC1x = bC2 * bR4

bR2 = ufloat(304, 304 * 0.03)
bR1x = bR2 * bR4
#2
bC2 = ufloat(750 * 10**(-9) , (750 * 10**(-9)) * 0.002)
bR3 = 722
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC2x = bC2 * bR4

bR2 = ufloat(228, 228 * 0.03)
bR2x = bR2 * bR4
#3
bC2 = ufloat(994 * 10**(-9) , (994 * 10**(-9)) * 0.002)
bR3 = 773
bR4 = (1000 - bR3) / bR3
bR4 = ufloat(bR4, bR4 * 0.005)
bC3x = bC2 * bR4

bR2 = ufloat(179, 179 * 0.03)
bR3x = bR2 * bR4

bRx = (bR1x + bR2x + bR3x) / 3
bCx = (bC1x + bC2x + bC3x) / 3
print('bC1x =', bC1x, ' bC2x =', bC2x, ' bC3x =', bC3x, ' bCx =', bCx)
print('bR1x =', bR1x, ' bR2x =', bR2x, ' bR3x =', bR3x, ' bRx =', bRx)

print('------------------------------------------------------------------------')
print('Nr. c, Lx,Rx = Wert19')
#1
cL2 = ufloat(0.0146, 0.0146 * 0.002)
cR3 = 281
cR4 = cR3 / (1000 - cR3)
cR4 = ufloat(cR4, cR4 * 0.005)
cL1x = cL2 * cR4

cR2 = ufloat(286, 286 * 0.03)
cR1x = cR2 * cR4
#2
cL2 = ufloat(0.0201, 0.0201 * 0.002)
cR3 = 287
cR4 = cR3 / (1000 - cR3)
cR4 = ufloat(cR4, cR4 * 0.005)
cL2x = cL2 * cR4

cR2 = ufloat(287, 287 * 0.03)
cR2x = cR2 * cR4

cLx = (cL1x + cL2x) / 2
cRx = (cR1x + cR2x) / 2
print('cL1x =', cL1x, ' cL2x =', cL2x, ' cLx =', cLx)
print('cR1x =', cR1x, ' cR2x =', cR2x, ' cRx =', cRx)

print('------------------------------------------------------------------------')
print('Nr. d, Lx,Rx = Wert19')
#1
dR2 = ufloat(332, 332 * 0.002)
dR3 = ufloat(215, 215 * 0.03)
dR4 = ufloat(655, 655 * 0.03)
dC4 = 750 * 10**(-9)
dR1x = (dR2 * dR3) / dR4
dL1x = dR2 * dR3 * dC4

#2
dR2 =  ufloat(664, 664 * 0.002)
dR3 = ufloat(95, 95 * 0.03)
dR4 = ufloat(538, 538 * 0.03)
dC4 = 750 * 10**(-9)
dR2x = (dR2 * dR3) / dR4
dL2x = dR2 * dR3 * dC4

#3
dR2 =  ufloat(1000, 1000 * 0.002)
dR3 = ufloat(96, 96 * 0.03)
dR4 = ufloat(796, 796 * 0.03)
dC4 = 750 * 10**(-9)
dR3x = (dR2 * dR3) / dR4
dL3x = dR2 * dR3 * dC4

dLx = (dL1x + dL2x + dL3x) / 3
dRx = (dR1x + dR2x + dR3x) / 3
print('dL1x =', dL1x, ' dL2x =', dL2x, ' dL3x =', dL3x, ' dLx =', dLx)
print('dR1x =', dR1x, ' dR2x =', dR2x, ' dR3x =', dR3x, ' dRx =', dRx)

print('------------------------------------------------------------------------')
print('Nr. e')
v = np.array([20, 70, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 700, 1000, 2000, 7000, 15000, 30000])
Ubr = np.array([4.56, 3.76, 1.78, 1.51, 1.28, 1.07, 0.88, 0.70, 0.56, 0.40, 0.26, 0.14, 0.02, 0.21, 0.23, 0.33, 0.43, 0.52, 0.61, 0.70, 0.78, 0.87, 0.96, 1.37, 2.14, 3.26, 3.90, 3.92, 3.92])
x = v / 380
y1 = Ubr / 4.5
w = 2*math.pi*v
w0 = 1 / (4.165*10**(-4))
O = w / w0
y2 = ((O**2-1)**2/((1-O**2)**2+16*O**2))**(0.5)
plt.plot(x, y1, 'rx', label="Experimentelle Werte")
plt.plot(x, y2, 'b-', label="Theoretische Werte")
plt.xlabel(r'$\Omega = \frac{f}{f_0}$')
plt.ylabel(r'$\frac{U_\text{br}}{U_\text{s}}$')
plt.xscale('log')
plt.grid()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('build/AufgabeE.pdf')
plt.close()
w0 = 1 / (Wert3 * 1000)
print('f0 theoretisch: ', w0/(2*math.pi))
var = np.mean(y1 / y2)
print('% Abweichung von Exp zu Theo Wert: ', (var - 1)*100)
print('------------------------------------------------------------------------')
