#Plantilla para el pre procesado de datos
#Importar el dataset
#Getwd()para saber en que directorio estamos
setwd("Parte1PreProcesadoDeDatos/")
dataset = read.csv('Parte1PreProcesadoDeDatos/Data.csv')
View(dataset)
#dataset=dataset[,2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
install.packages("caTools") # Instalar paquetes, solo hacerlo una vez y dejar comentada
library(caTools) # Para cargar la libreria
set.seed(123) # Definir la semilla aleatoria
split = sample.split(dataset$Purchased,SplitRatio=0.8) # Definimos que porcentaje de los datos van a formar parte del conjunto de entrenamiento y el resto de los datos seran para testing
training_set = subset(dataset,split == TRUE) # Cogemos el subconjunto de datos que tengan TRUE que son los de entrenamiento
testing_set = subset(dataset,split==FALSE)  # Cogemos el subconjunto de datos que tengan FALSE que son los de testing

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])
