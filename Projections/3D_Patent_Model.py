#3D patent projection to vector space

#Matplot
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

#Other dependencies
import numpy as np
import csv

style.use('ggplot')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

with open('qm_2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        z.append(float(row[2]))


plt.scatter(x,y,z, label='Patents')

ax.set_xlabel('Claims')
ax.set_ylabel('Cited Proior Art')
ax.set_zlabel('Inventors')

plt.title('Patents')
plt.legend()
plt.show()
