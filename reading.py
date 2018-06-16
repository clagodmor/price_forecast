# -------------------------------------------------------------------------
# SCRIPT:reading.py
# AUTHOR: Clara Godoy
# DAT: 20th May 2018
# DESCRIPTION:agrupa los datos obtenidos de Meteologica S.A.
# -------------------------------------------------------------------------


import pandas as pd
import zipfile


# Extracción de ficheros
zipfilename = "data/HISTORICAL_DATA.zip"
password = None

# open and extract all files
z = zipfile.ZipFile(zipfilename, "r")
try:
    z.extractall(path="data/",pwd=password)
except:
    print('Error')
    pass
z.close()

#lectura y ordenación por fechas

# WIND POWER DATA
wind_data="data/WIND_HIST.csv"
photo_data="data/PHOTO_HIST.csv"
demand_data="data/DEMAND_HIST.csv"
price_data="data/PRICE_HIST.csv"
solarthermal_data="data/THERMO_HIST.csv"
temperature_data="data/TEMP_HIST.csv"

df= pd.read_table(price_data,sep=';')
df=df.rename(columns={'FECHA':'date','PRECIO cEUR/kWh':'price'})

df2 = pd.read_table(wind_data,sep=';')
df2=df2.rename(columns={'FECHA':'date','EOLICA':'wind'})

df3 = pd.read_table(demand_data,sep=';')
df3=df3.rename(columns={'FECHA':'date','DEMANDA':'demand'})

df4 = pd.read_table(photo_data,sep=';')
df4=df4.rename(columns={'FECHA':'date','FOTOVOLTAICA':'photo'})

df5 = pd.read_table(temperature_data,sep=';')
df5=df5.rename(columns={'FECHA':'date','TEMPERATURA dK':'temperature'})

df6 = pd.read_table(temperature_data,sep=';')
df6=df6.rename(columns={'FECHA':'date','TERMOSOLAR':'thermo'})

df=df.merge(df2,left_on='date',right_on='date',how='inner')
df=df.merge(df3,left_on='date',right_on='date',how='inner')
df=df.merge(df4,left_on='date',right_on='date',how='inner')
df=df.merge(df5,left_on='date',right_on='date',how='inner')

df.to_csv('out.csv')