import numpy as np

#criando um array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1[2])


arr2 = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]])
print(arr2[1,2]) #acessando o elemento da linha 1 e coluna 2
print(arr2[0,1]) #acessando o elemento da linha 0 e

print(f"Shape da matriz:{arr2.shape}") #mostra o formato da matriz
print(f"Dimensão da matriz:{arr2.ndim}") #mostra a dimensão da matriz
print(f"Tipo de dados da matriz:{arr2.dtype}") #mostra o tipo de dados da matriz
print(f"Tamanho da matriz/Número de elementos:{arr2.size}") #mostra o número de elementos da matriz

#operações matematicas
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1 + 10) #soma 10 a cada elemento do array
print(arr1 * 2) #multiplica cada elemento do array por 2

print("Media: ")
print(np.mean(arr1)) #calcula a média dos elementos do array
print("Mediana: ")
print(np.median(arr1)) #calcula a mediana dos elementos do array
print("Desvio Padrão: ")
desvio_padrao = np.std(arr1) #calcula o desvio padrão dos elementos do array
print(desvio_padrao)

print("Variancia: ")
variancia = np.var(arr1)
print(variancia)

print(arr1.sum()) #calcula a soma dos elementos do array
print(arr1.min()) #encontra o valor mínimo do array
print(arr1.max()) #encontra o valor máximo do array

