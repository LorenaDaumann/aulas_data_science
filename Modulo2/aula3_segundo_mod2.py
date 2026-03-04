import matplotlib.pyplot as plt

#definindo as variaveis
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#criando um grafico de pontos
plt.scatter(x, y, label = "Pontos", color = "b", marker = "*", s = 100)
plt.legend()
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Grafico de Pontos")
plt.show()