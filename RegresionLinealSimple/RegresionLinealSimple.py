#Regresion lineal simple

#Copiar Plantilla de pre procesado de datos

import numpy as np
import matplotlib.pylot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size=1/3,random_state = 0)

#Crear modelo de regresion lineal simple con el conjunto de entrenamiento

from sklearn.linear_model import LinearRegression
regression = LinearRegression() # Como es una regresion lineal simple no hace falta pasarle ningun tipo de parámetros
regression.fit(xTrain,yTrain) #Acepta dos parametros, en primer lugar el conjunto de variables independientes o la matriz de características
# Ambos deben tener el mismo tamaño

# Predecir el conjunto de los test
yPred = regression.predict (xTest)
 

# Visualizar los resultados de entrenamiento
plt.scatter(xTrain,yTrain,color="red")
plt.plot(xTrain,regression.predict(xTrain,color="blue"))
plt.title("Salary vs Experience Years")
plt.xlabel("Experience years")
plt.ylabel("Salary")
plt.show()

