#ANALISE EXPLORSATÓRIA DE DADOS (EDA_EXPLORATORY DATA ANALYSIS)

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("/home/lorena/Documentos/ATIVIDADES-SCTEC/Modulo2/titanic.csv")
print(df.head())
print("\n")
print(df.info())
print("\n")
print(df.describe())
print("\n")
print(df.isnull().sum())
print("\n")

#datatypes
print(df.dtypes)
print("\n")

#filtros
print(df[df['age'] > 10].head())
print("\n")

duplicados = df.duplicated().sum()
print(f"Número de linhas duplicadas: {duplicados}")
#ouuu
duplicateRows = df[df.duplicated()]
print(len(duplicateRows))
print(len(df))

df.drop_duplicates(keep="last", inplace=True)
print(len(df))

#df.dropna(subset=['deck'], inplace=True) #APAGAR LINHAS COM VALORES NULOS NA COLUNA DECK
df.replace(np.nan, '0', inplace=True)
print(df)

#renomear colunas
df = df.rename(columns={'sex': 'Genero'})
print(df.head(5))

sorted_df = df.sort_values(by='Genero', ascending=True)
print(sorted_df.head())

#groupby
grouped_by = df.groupby('age')
print(grouped_by.head())