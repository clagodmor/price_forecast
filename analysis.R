## -------------------------------------------------------------------------
## SCRIPT: analysis.R
## CURSO: Master en Data Science
## AUTOR: Clara Godoy
## -------------------------------------------------------------------------

## -------------------------------------------------------------------------

##### 1. Bloque de inicializacion de librerias #####

if(!require("plyr")){
  install.packages("plyr")
  library("plyr")
}

if(!require("caTools")){
  install.packages("caTools")
  library("caTools")
}

if(!require("ROCR")){
  install.packages("ROCR")
  library("ROCR")
}

setwd("~/PycharmProjects/master-data-science")

## -------------------------------------------------------------------------
##       PARTE 1: REGRESION BINOMIAL LOGIT/LOGISTICA
## -------------------------------------------------------------------------

## -------------------------------------------------------------------------

##### 2. Bloque de carga de datos #####

price=read.csv2("data/out.csv")

str(price)
head(price)
summary(price)

price$temp=as.integer(price$temp)
price$price=as.numeric(price$price)

##### 14. Bloque de modelos de regresión poisson #####

hist(price$price)
mean(price$price)
sd(price$price)

modeloPoisson=glm(price~.-date, family=poisson(link = "log"),data=price)
summary(modeloPoisson)


###FORMATEO DEE VARIABLES

price$wind=as.factor(price$wind)
price$photo=as.factor(price$photo)
price$temp=as.factor(price$temp)
price$thermo=as.factor(price$thermo)
price$demand=as.factor(price$demand)
price$hydro=as.factor(price$hydro)


modeloPoisson=glm(price~.-date, family=poisson(link = "log"),data=price)
summary(modeloPoisson)
modeloPoissonFinal=step(modeloPoisson)
anova(modeloPoisson,modeloPoissonFinal,direction="both",trace=1)


coef(modeloPoissonFinal)
exp(coef(modeloPoissonFinal))


##### 19. Bloque de selección de variables #####

modeloPoisson=glm(cnt~.-instant-dteday-casual-registered, family=poisson(link = "log"),data=bicis)
summary(modeloPoisson)
modeloPoissonFinal=step(modeloPoisson)
anova(modeloPoisson,modeloPoissonFinal,direction="both",trace=1)

## -------------------------------------------------------------------------

##### 20. Bloque de cálculo de predicciones #####

price$prediccion=predict(modeloPoissonFinal,type="response")

## -------------------------------------------------------------------------

##### 21. Bloque de representación de distribución #####

Caso=35 #35,
price[Caso,]

lambda=price$prediccion[Caso]
lambda

plot(dpois(1:120,lambda), type="l")
round(dpois(1:120,lambda),4)*100
