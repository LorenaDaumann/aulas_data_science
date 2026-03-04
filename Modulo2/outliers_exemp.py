import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/home/lorena/Documentos/ATIVIDADES-SCTEC/Modulo2/titanic.csv")

sns.boxplot(x=df["age"])
plt.show()