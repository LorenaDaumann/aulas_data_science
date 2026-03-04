def minha_funcao():
    nome = "Lan Code"
    print(f"Essa é minha função! Prazer, {nome}")


def saudacao(nome):
    print(f"Prazer, {nome}")

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

if verificar_par(6):
    print(f"É par!")
else:
    print(f"É impar:")

def somar(n1, n2):
    resultado = n1+n2
    return resultado

def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

soma_da_lista = somar_lista(6,7,8,9,12)
print(f"\nO resultado é {soma_da_lista}")

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma+=numero
        media = soma/qtd
    return media

resultado = calcular_media(7,3,2,9)
print(f"\nA média é {resultado}\n")

def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

informacoes_pessoais(nome="Lan code", idade=19, cidade="São Paulo", estado="SP")



######################EXERCÍCIOS###########################

def funcao_num(numerinho):
    numerinho -= 0
    return

funcao_num(17)     


##########################################################

def contagem_regressiva(numero):
    while True:
        print(numero)
        numero -=1
        if numero <0:
            break
    
contagem_regressiva(2)

#ouuuuuuuu

def contagem_regressiva2(numero):
   for i in range(numero, 0, -1):
    print(i)

contagem_regressiva2(2)

###########################################################

def maior_num(lista_numeros):
    maior_num= lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior_num:
            maior_num = numero
    return maior_num

lista = [4,8,9,2,5]
maior_num_lista = maior_num(lista)
print(f"O maior numero da lista é {maior_num_lista}")

#ouuuuuuuuuuuuuuuuuuuuuuuuuuuuuu

def maior_num2(lista_numeros):
    maior_num2= max(lista_numeros)
    return maior_num2

lista2 = [4,8,9,2,5]
maior_num_lista2 = maior_num(lista2)
print(f"O maior numero da lista é {maior_num_lista2}")