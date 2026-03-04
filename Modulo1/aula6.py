# pilha = []
# pilha.append(1)
# pilha.append(2)
# pilha.append(3)
# print("Pilha após adicionar elementos:")
# print(pilha)  # Imprime a pilha atualizada  

# pilha.pop()  # Remove o último elemento da pilha
# print("\nPilha após remover o último elemento:")
# print(pilha)  # Imprime a pilha atualizada

from collections import deque
fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
print("Fila após adicionar elementos:") 
print(fila)  # Imprime a fila atualizada

fila.popleft()  # Remove o primeiro elemento da fila
print("\nFila após remover o primeiro elemento:")
print(fila)  # Imprime a fila atualizada 

