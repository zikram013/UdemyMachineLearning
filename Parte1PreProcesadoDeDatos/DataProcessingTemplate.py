# Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


# Importar el dataSet
# Para mostrar el dataFrame del dataset debemos debuguear la variable
dataset = pd.read_csv("Data.csv")
# localizar elementos por posicion
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
# EL 20% (tope 30%) de los datos se dedicaran a testing y el reto como conjunto de entrenamiento
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=0)

# Escalado de variables
"""
scX = StandardScaler()
xTrain = scX.fit_transform(xTrain)
xTest = scX.transform(xTest)
"""

"""
¿Se deben escalar las variables dummies? 
Si, hay que escalarlas por coherencia para que queden  en el mismo rango
No, no hay que escalarlas porque al hacerlo perdemos la pertenencia a la clase dummy al hacerlas y perdemos ese significado
"""

print()
