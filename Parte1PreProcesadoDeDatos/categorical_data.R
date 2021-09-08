#Plantilla para el pre procesado de datos categoricos
#Importar el dataset
#Getwd()para saber en que directorio estamos
setwd("Parte1PreProcesadoDeDatos/")
dataset = read.csv('Parte1PreProcesadoDeDatos/Data.csv')
View(dataset)

#Codificar Variables categoricas
dataset$Country = factor(dataset$Country,
                         levels = c("France","Spain","Germany"),
                          labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels=c("No","Yes"),
                            labels = c(0,1))