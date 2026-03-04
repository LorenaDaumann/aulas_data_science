import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

exemp1 = pd.read_csv("/home/lorena/Documentos/ATIVIDADES-SCTEC/Modulo2/Ice Cream Sales - temperatures.csv")

# Reshape data for heatmap visualization
exemp1_heatmap = exemp1.set_index("Temperature").T
plt.figure(figsize=(40, 5))
sns.heatmap(exemp1_heatmap, annot=True, fmt=".0f")
plt.title("Ice Cream Sales by Temperature")
plt.show()