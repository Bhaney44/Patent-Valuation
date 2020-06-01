#3D patent projection to vector space

#Matplot
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D

#Other dependencies
import numpy as np
import csv

def patent_file():
    csvfile = open('qm_0.csv', 'r')
    read = csv.reader(csvfile)
        for row in read:
            patent 


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
