
#Imports
import matplotlib.pyplot as plt
import csv


#Create empty list
x = []
y = []

with open('qm_1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.scatter(x,y, label='Patents')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Patents')
plt.legend()
plt.show()
