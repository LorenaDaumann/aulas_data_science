# 1. crie dois arrys com nomes e slario de funcionarios
# 2. em seguida, mostre na tela o gráfico destes valores
# Create arrays with employee names and salaries

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

nomes = np.array(["Alice", "Bob", "Carlos", "Diana", "Eva"])
salarios = np.array([3000, 3500, 4000, 3200, 4500])

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(nomes, salarios, color='steelblue')
plt.xlabel('Funcionários')
plt.ylabel('Salário (R$)')
plt.title('Salários dos Funcionários')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
