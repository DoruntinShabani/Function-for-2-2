from scipy import signal
A = [1.0, 2.0, 3.0]
B= [4.0, 5.0, 6.0, 7.0]
y = signal.convolve(A, B)
print(y)
import matplotlib.pyplot as plt
plt.plot(y)
plt.show()
