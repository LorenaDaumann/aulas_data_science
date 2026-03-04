telefones = ['1234-5678', '9876-5432', '5555-5555', '1111-1111', '2222-2222']
print("Lista de telefones:")
print(telefones)  # Acessa o primeiro elemento

telefones.append('3333-3333')  # Adiciona um novo telefone à lista
print("\nLista de telefones atualizada - número adicionado:")
print(telefones)  # Imprime a lista atualizada

telefones.insert(0, '4444-4444')  # Insere um telefone na posição 2
print("\nLista de telefones atualizada - número inserido na posição 0:")
print(telefones)  # Imprime a lista atualizada

telefones.remove('5555-5555')  # Remove um telefone específico
print("\nLista de telefones atualizada - número '5555-5555' removido:")
print(telefones)  # Imprime a lista atualizada

telefones[1] = '9999-9999'  # Altera o telefone na posição 1 
print("\nLista de telefones atualizada - número na posição 1 alterado para '9999-9999':")
print(telefones)  # Imprime a lista atualizada  

telefones.pop()  # Remove o último telefone da lista
print("\n\nLista de telefones atualizada - último número removido:")
print(telefones)  # Imprime a lista atualizada

contato = ("Yan", "1234-5678")

telefones2 = []
telefones2.append(contato)  # Adiciona a tupla 'contato' à lista 'telefones2'
print("\nLista de telefones2 atualizada - tupla 'contato' adicionada:")
print(telefones2)

telefones3 = [("Maria", "9876-5432"), ("João", "5555-5555"), ("Ana", "1111-1111"), ("Pedro", "2222-2222")]
print("\n\nLista de telefones3:")
print(telefones3)

print("\nAcessando o primeiro contato da lista telefones3:")
print(telefones3[0][1]) # Acessa o número do primeiro contato na lista telefones3


#DICIONARIOS
telefones3_dict = dict(telefones3)  # Converte a lista de tuplas em um dicionário
print("\nDicionário de telefones:")
print(telefones3_dict)  # Imprime o dicionário de telefones

(telefones3_dict["Maria"])  # Acessa o número de telefone associado ao nome "Maria"
print("\nNúmero de telefone de Maria:")
print(telefones3_dict["Maria"])  # Imprime o número de telefone de Maria

telefones3_dict["Ana"] = "3333-3333"  # Altera o número de telefone associado ao nome "Ana"
print("\nDicionário de telefones atualizado - número de Ana alterado para '3333-3333':")
print(telefones3_dict)  # Imprime o dicionário de telefones atualizado

telefones3_dict.pop("João")  # Remove o contato associado ao nome "João"
print("\nDicionário de telefones atualizado - contato 'João' removido:")
print(telefones3_dict)  # Imprime o dicionário de telefones atualizado

######VER AULA 5 PARA EXPLICAÇÃO DE PACOTE E MÓDULO################