import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('qm_1.csv', delimiter=',', unpack=True)
plt.scatter(x,y, label='Patents')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Patents')
plt.legend()
plt.show()
