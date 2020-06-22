#3D patent projection to vector space

#Matplot
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Other dependencies
import numpy as np
import csv


fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x, y, z = np.loadtxt('Total_Python.csv', delimiter=',', unpack=True)

ax1.scatter(x,y,z)
plt.show()




ax.set_zlabel('Claims')
ax.set_ylabel('Cited Proior Art')
ax.set_xlabel('Inventors')

plt.title('Thyroid Patents')
plt.legend()
plt.show()
