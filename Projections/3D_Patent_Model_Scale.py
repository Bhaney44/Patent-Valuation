#3D patent projection to vector space

#Matplot
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D


#Other dependencies
import numpy as np
import csv

plt.clf()
style.use('ggplot')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

with open('Total_Python.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(int(row[2]))


ax = Axes3D(fig)
ax.set_xlim3d(0, 200)
ax.set_ylim3d(0,2000)
ax.set_zlim3d(0,20)

plt.scatter(x,y,z, label='Patents') 

ax.set_xlabel('Claims')
ax.set_ylabel('Cited Proior Art')
ax.set_zlabel('Inventors')

plt.title('Thyroid Patents')
plt.legend()
plt.show()
