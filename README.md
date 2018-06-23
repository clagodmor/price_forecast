# Master in Data Science VI edition: PFM

##Electricity price forecasting

###1. ¿Para qué sirve?
Las predicciones de precio en general se usan en todos los sectores para una toma de decisiones óptima. 
En el sector energetico es clave en muchos sentidos:
* Las previsiones horarias y diarias resultan fundamentales para mercados de muy corto plazo, por parte de comercializadores y generadores de electricidad. Esencialmente para prever precios horarios del mercado diario.
* Prever el precio del mercado eléctrico a un horizonte en torno a doce meses constituye una herramienta clave para la toma de decisiones operativas y de gestión de riesgo a ese plazo para comercializadores y generadores, e igualmente puede ser utilizada por traders en la optimización de sus carteras de energía. 
* Las decisiones de inversión o desinversión en activos de generación eléctrica requieren un análisis riguroso y la proyección de los precios de electricidad a largo plazo (entre 5 y 20 años). Sirve de input para otras variables como valoración de inversiones y medición de riesgo de mercado

El principal objetivo de este codigo es el de crear una predicción de precio lo más precisa posible, utilizando variables explicativas poco usuales y con el máximo alcance posible.

###2. Variables explicativas
Por supuesto, la incertidumbre sobre la naturaleza (viento, lluvia, temperatura, etc), sobre el comportamiento de los agentes del sector, sobre la progresión de la economía y la asociada a cambios regulatorios hacen que estas variables (sobre todo, el precio de la electricidad) sean muy volátiles e inciertas, impidiendo el conocimiento de sus valores futuros con precisión.

Normalmente el precio de la electricidad se explica mediante la producción eólica del pais y la demanda existente. La premisa en la que se basa este proyecto es que en cada mercado/pais influencian más o menos otras variables.

###Datos
Los datos que se van a tener encuenta y las unidades en las que se van a tratar son:

|DATO|UNIDAD|ALIAS|
|----|------|-----|
|FECHA|horario en UTC|date|
|Precio eléctrico|cent€/kWh|price|
|Producción eólica|kW|wind|
|Porducción fotovoltaica|kW|photo|
|Demanda energética|kW|demand|
|Temperatura|dK|temp|
|Producción termosolar|kW|thermo|
|Disponibilidad hidraúlica|kW|hydro|


Data ceded by Meteologia S.A.