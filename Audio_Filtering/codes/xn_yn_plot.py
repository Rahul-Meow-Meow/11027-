import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Generated_values_xn_yn.txt')
xn_x_values = data[0:7,0]
yn_x_values = data[:,0]

xn_y_values = data[0:7,1]
yn_y_values = data[:,2]

def plotting(x_values,y_values,name, ylabel,graphlabel):
	plt.stem(x_values, y_values, label=graphlabel)
	plt.xlabel('n')
	plt.ylabel(ylabel)
	plt.grid(True)
	plt.savefig(name)

plotting(xn_x_values, xn_y_values,'x(n)_vs_n.png', 'x(n)', 'Plot of x(n) vs n')
plt.clf()
plotting(yn_x_values, yn_y_values,'y(n)_vs_n.png', 'y(n)', 'Plot of y(n) vs n')
