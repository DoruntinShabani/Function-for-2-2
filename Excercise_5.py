import numpy as np
import matplotlib.pyplot as plt
T = np.arange(0.0, 3.1, 0.1)
rho=561.6
m0=0.511
X=[]
Y=[]
for x in T:
    gamma=((x*1000)/m0)+1
    delta_E=88.5*x**4 / rho
    X.append(gamma)
    Y.append(delta_E)


plt.grid(color='k')
plt.plot(X,Y)
plt.xlabel('Gamma of the electron')
plt.ylabel('Radiated Energy per Turn of Electron [keV]')
plt.title('Radiated energy per turn of an electron \n with respect to its Gamma for the Diamond Light Source')
plt.show()
