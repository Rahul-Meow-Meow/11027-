import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Values.txt')
x_values = data[:,0]

y_values = data[:,1]

y_calcu = data[:,2]
plt.stem(x_values, y_values, label='y(t) v/s t')
plt.scatter(x_values, y_calcu, marker = 'X',s=100, color = 'red', label = r'Simulation')
plt.xlabel('t')
plt.ylabel('y(t)')

#plt.axhline(0, color='black',linewidth=0.5)
#plt.axvline(0, color='black',linewidth=0.5)

plt.grid(True)
plt.savefig('y(t)_vs_t.png')

