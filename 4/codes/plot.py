import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Values.txt')
x_values = data[:,0]

y_values = data[:,1]

plt.stem(x_values, y_values, label='y(t) v/s t')

plt.xlabel('t')
plt.ylabel('y(t)')

#plt.axhline(0, color='black',linewidth=0.5)
#plt.axvline(0, color='black',linewidth=0.5)

plt.grid(True)
plt.savefig('y(t)_vs_t.png')

