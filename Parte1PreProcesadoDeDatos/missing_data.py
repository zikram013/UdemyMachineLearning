import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer


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