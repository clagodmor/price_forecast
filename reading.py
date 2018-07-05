# -------------------------------------------------------------------------
# SCRIPT:reading.py
# AUTHOR: Clara Godoy
# DAT: 20th May 2018
# DESCRIPTION:agrupa los datos obtenidos de Meteologica S.A. en un fichero csv
# -------------------------------------------------------------------------

import numpy as np
import pandas as pd
import zipfile
import os

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
hydro_disp_data="data/DISP_HIDRO_HIST.csv"
hydro_prod_data="data/PROD_HIDRO_HIST.csv"

df= pd.read_table(price_data,sep=';')
df=df.rename(columns={'FECHA':'date','PRECIO cEUR/kWh':'price'})
df=df.round(3)
os.remove(price_data)

df2 = pd.read_table(wind_data,sep=';')
df2=df2.rename(columns={'FECHA':'date','EOLICA':'wind'})
os.remove(wind_data)

df3 = pd.read_table(demand_data,sep=';')
df3=df3.rename(columns={'FECHA':'date','DEMANDA':'demand'})
os.remove(demand_data)

df4 = pd.read_table(photo_data,sep=';')
df4=df4.rename(columns={'FECHA':'date','FOTOVOLTAICA':'photo'})
os.remove(photo_data)

df5 = pd.read_table(temperature_data,sep=';')
df5=df5.rename(columns={'FECHA':'date','TEMPERATURA dK':'temp'})
df5=df5.round(0)
os.remove(temperature_data)

df6 = pd.read_table(solarthermal_data,sep=';')
df6=df6.rename(columns={'FECHA':'date','TERMOSOLAR':'thermo'})
os.remove(solarthermal_data)

df7 = pd.read_table(hydro_disp_data,sep=';')
df7=df7.rename(columns={'FECHA':'date','DISP_HIDRO kW':'hydro_disp'})
os.remove(hydro_disp_data)

df8 = pd.read_table(hydro_prod_data,sep=';')
df8=df8.rename(columns={'FECHAS':'date','PROD_HIDRO kW':'hydro_prod'})
os.remove(hydro_prod_data)


df=df.merge(df2,left_on='date',right_on='date',how='inner')
df=df.merge(df3,left_on='date',right_on='date',how='inner')
df=df.merge(df4,left_on='date',right_on='date',how='inner')
df=df.merge(df5,left_on='date',right_on='date',how='inner')
df=df.merge(df6,left_on='date',right_on='date',how='inner')
df=df.merge(df7,left_on='date',right_on='date',how='inner')
df=df.merge(df8,left_on='date',right_on='date',how='inner')

df.to_csv('data/TOTAL.csv',index=False)
def train_validate_test_split(df, train_percent=.6, validate_percent=.2, seed=None):
    np.random.seed(seed)
    perm = np.random.permutation(df.index)
    m = len(df)
    train_end = int(train_percent * m)
    validate_end = int(validate_percent * m) + train_end
    train = df.ix[perm[:train_end]]
    validate = df.ix[perm[train_end:validate_end]]
    test = df.ix[perm[validate_end:]]
    return train, validate, test

train, validate, test = train_validate_test_split(df)

train.to_csv('data/train.csv',index=False)
validate.to_csv('data/validate.csv',index=False)
test.to_csv('data/test.csv',index=False)
