#Plantilla para el pre procesado de datos
#Importar el dataset
dataset = read.csv('Data.csv')
View(dataset)
#Tratamiento de los valores NAs
dataset$Age = ifelse(is.na(dataset$Age),
  ave(dataset$Age,FUN = function (x)mean(x,na.rm=TRUE)),
  dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
  ave(dataset$Salary,FUN = function (x)mean(x,na.rm=TRUE)),
  dataset$Salary)

#Codificar Variables categoricas
dataset$Country = factor(dataset$Country,
                         levels = c("France","Spain","Germany"),
                          labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels=c("No","Yes"),
                            labels = c(0,1))
                        
                        
# Dividir los datos en conjunto de entrenamiento y conjunto de test
install.packages("caTools") # Instalar paquetes, solo hacerlo una vez y dejar comentada
library(caTools) # Para cargar la libreria
set.seed(123) # Definir la semilla aleatoria
split = sample.split(dataset$Purchased,SplitRatio=0.8) # Definimos que porcentaje de los datos van a formar parte del conjunto de entrenamiento y el resto de los datos seran para testing
training_set = subset(dataset,split == TRUE) # Cogemos el subconjunto de datos que tengan TRUE que son los de entrenamiento
testing_set = subset(dataset,split==FALSE)  # Cogemos el subconjunto de datos que tengan FALSE que son los de testing

# Escalado de valores
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])
