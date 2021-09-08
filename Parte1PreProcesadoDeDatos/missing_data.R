#Plantilla para el pre procesado de datos faltantes
#Importar el dataset
#Getwd()para saber en que directorio estamos
setwd("Parte1PreProcesadoDeDatos/")
dataset = read.csv('Parte1PreProcesadoDeDatos/Data.csv')
View(dataset)

#Tratamiento de los valores NAs
dataset$Age = ifelse(is.na(dataset$Age),
  ave(dataset$Age,FUN = function (x)mean(x,na.rm=TRUE)),
  dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
  ave(dataset$Salary,FUN = function (x)mean(x,na.rm=TRUE)),
  dataset$Salary)