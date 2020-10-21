import math
import numpy as np
f= input("Enter the frequency (in Hertz):")
u = input("Enter the voltage (in volts):")
charge = (6 * 1.602e-19)
a = math.sin(math.pi / 4)
mass = 9.96323e-27
Li_values = []
def solution(i, length):
    Li = 1 / int(f) * math.sqrt(int(u) * a * charge * i / (2 * mass))
    print(i, Li)
    Li_values.append(Li)
    L = np.sum(Li_values)
    if L >= 5:
        print('Total length of the tubes is', L,'meters. You can fit only', i - 1,
              'tubes, because Doruntins room is only 5 meters wide. Try a different voltage and/or frequence.')
        exit()
    if L<5 and length == i+1:
        print ('Total length of the tubes is',L,'meters. Congrats you can fit this accelerator in Doruntins room.')
vec_func = np.vectorize(solution)
A = np.arange(0, 21)
vec_func(list(A), len(list(A)))
