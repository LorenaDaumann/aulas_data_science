import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# Line plot
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.savefig('grafico_linhas.png')
plt.close()

# Bar chart
x = ['Maçãs', 'Bananas', 'Laranjas']
y = [5, 7, 9]

plt.bar(x, y)
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.savefig('grafico_barras.png')
plt.show()

# import matplotlib
# matplotlib.use("TkAgg")

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
# plt.title("Teste")
# plt.show()


