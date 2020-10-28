import matplotlib.pyplot as plt
X = []
for line in open('2016-07-11_ipm_data.txt', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  xmax = max(X)
plt.grid(color='k')
plt.plot(X)
plt.plot(576,xmax, marker='o', color='r')
plt.show()
