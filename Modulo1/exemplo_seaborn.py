import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
df_por_sexo = titanic.groupby('sex')['survived'].mean().reset_index()

plt.figure(figsize=(8, 6))

sns.barplot(data=df_por_sexo, x='sex', y='survived', palette='pastel')
plt.show()

