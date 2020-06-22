import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('Total_Python.csv')


print(df.head())

print(df.tail())
print(df.index)
print(df.columns)
print("-----")

print(df.describe())
print(df.median())
print(df.mode())
print(df.var())


#print(df.columns)
#print(df.columns[0])
#print(df.columns[1])
#print(df.columns[2])

claims = df.columns[0]
prior_art = df.columns[1]
inventors = df.columns[2]

#for index, row in df.iterrows():
    #print(claims, prior_art, inventors)

    

#with open('Total_Python.csv','r') as csvfile:
   # plots = csv.reader(csvfile, delimiter=',')
   # for row in plots:
       # x.append(int(row[0]))
       # y.append(int(row[1]))
       # z.append(int(row[2]))


#threedee = plt.figure().gca(projection='3d')
#threedee.scatter(claims, prior_art, inventors)
#threedee.set_xlabel('Claims')
#threedee.set_ylabel('Cited Proior Art')
#threedee.set_zlabel('Inventors')


#plt.title('Thyroid Patents')
#plt.legend()
#plt.show()
