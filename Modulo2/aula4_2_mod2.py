import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/home/lorena/Documentos/ATIVIDADES-SCTEC/Modulo2/titanic.csv")

survived_counts = df['survived'].value_counts()
print(survived_counts)

plt.figure(figsize=(8, 6))
plt.bar(survived_counts.index, survived_counts, color=['skyblue', 'salmon'])

plt.title('Contagem de Sobreviventes')
plt.xlabel('Survived (0 / 1)')
plt.ylabel('Countagem')

plt.show()

#outlier - detectar e rremover os valores descrepantes