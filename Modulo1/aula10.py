def pure_increments(elements, index):
    # return [x + increment for x in elements]
    new_elements = elements.copy()
    new_elements[index] += 1
    return new_elements

lista = [1, 2, 3, 4, 5,6,7,8,9]
print(pure_increments(lista, 0))

print(lista)



def somar_lista(*numeros):
    print(numeros)

somar_lista(6,7,8,9,5)

def somar_lista2(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

soma_da_lista = somar_lista2(6,7,8,9,5)
print(f"O resultado é {soma_da_lista}")

def calcular_media(*numeros):
    qtd = len(numeros)
    soma =  0
    for numero in numeros:
        soma+=numero
    media = soma/qtd
    return media

resultado = calcular_media(7,2,9,4)
print(f"A média é {resultado}")

def info_pessoais (**infos):
    for chave, valor in infos.items():
        print(f"{chave}: {valor}")

info_pessoais(nome="Lorena", idade=19, cidade="São Paulo", estado="SP")