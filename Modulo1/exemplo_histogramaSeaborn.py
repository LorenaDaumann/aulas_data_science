import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

plt.figure(figsize=(8, 6))

sns.histplot(data=titanic, x='sex', palette='pastel')
plt.show()
