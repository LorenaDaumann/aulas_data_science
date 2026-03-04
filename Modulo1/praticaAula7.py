# 1. crie uma lista e use a declaração da lista
# 2. depois aplique os principio de pilha, fila e lista que aprendemos na aula, adicionando e inserindo frutas
# 3. utilize o for para imprimir cada fruta da lista e o while para imprimir os números de 1 a 5
# 4. por fim, crie um condição para imprimir somente o primeiro e segundo elemento. somente os dois primeiros elementos da lista


from collections import deque
frutas = deque(["Maçã", "Banana", "Laranja", "Abacaxi", "Uva"])
print("Fila após adicionar elementos:") 
print(frutas)  # Imprime a fila atualizada

frutas.popleft()  # Remove o primeiro elemento da fila
print("\nFila após remover o primeiro elemento:")
print(frutas)  # Imprime a fila atualizada 


doces = ["Chocolate", "Bala", "Pirulito", "Goma de Mascar", "Doce de Leite"]
print(doces)
doces.pop()  # Remove o último elemento da pilha
print("\nPilha após remover o último elemento:")
print(doces)  # Imprime a pilha atualizada
