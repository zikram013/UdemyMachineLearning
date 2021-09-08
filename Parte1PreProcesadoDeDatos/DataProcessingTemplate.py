# Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Importar el dataSet
# Para mostrar el dataFrame del dataset debemos debuguear la variable
dataset = pd.read_csv("Data.csv")
# localizar elementos por posicion
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
# tratamiento de los NAs
# Reemplazamiento de los valores desconocidos (0=columna 1=fila)
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
labelenconderX = preprocessing.LabelEncoder()
x[:, 0] = labelenconderX.fit_transform(x[:, 0])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x), dtype=np.float)
labelenconderY = preprocessing.LabelEncoder()
y=labelenconderY.fit_transform(y)


"""Realizado en gis, comprobar imports en casa"""

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from skalearn.model_selection import train_test_split
xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size = 0.2, random_state = 0) # EL 20% (tope 30%) de los datos se dedicaran a testing y el reto como conjunto de entrenamiento

# Escalado de variables
from sklearn.preprocessing import StandardScaler
scX=StandardScaler()
xTrain = scX.fit_transform(xTrain)
xTest = scX.transform(xTest)
"""¿Se deben escalar las variables dummies? Si, hay que escalarlas por coherencia para que queden  en el mismo rango
No, no hay que escalarlas porque al hacerlo perdemos la pertenencia a la clase dummy al hacerlas y perdemos ese significado"""

print()
