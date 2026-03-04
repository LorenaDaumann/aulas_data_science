#range(inicio, fim+1)

# 1. utilize o laço de repetição for para contar ou iterar entre um intercvalo de números e imprimirno terminal todos os numeros pares desse intervaloi
# 2. escreva um programa que solicita ao usuário dois números: o ínicio e o fim de um intervalo. 
# 3. Em seguida, o programa deve imprimir todos os números pares dentro desse intervalo.
# O resultado desse código, seria apresenatar no terminal os numeros pares entre 1 e 10, que seriam: 2, 4, 6, 8 e 10.

numerinhos = 10
for i in range(1, numerinhos + 1):
    if i % 2 == 0:
        print(i)

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
print(f"Números pares entre {inicio} e {fim}:")
for i in range(inicio, fim + 1):
    if i % 2 == 0:
        print(i)




#FUNÇÕES DESATIVADAS DO VS CODE QUE AUTOCOMPLLETAM O CODIGO, PARA QUE EU POSSA PRATICAR MAIS A ESCRITA DO CODIGO, E NÃO FICAR DEPENDENTE DE AUTOCOMPLETAR O CODIGO.
# Editor: Suggest On Trigger Characters
# Editor: Quick Suggestions

# Editor: Suggest Selection
# Editor: Accept Suggestion On Enter
# Editor: Parameter Hints
# Editor: Auto Closing Brackets
# Editor: Auto Closing Quotes
# Editor: Auto Surround   