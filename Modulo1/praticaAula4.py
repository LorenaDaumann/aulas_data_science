#crie uma lista de alunos e realize as seguintes operações:
#1. Adicione novos alunos à lista
#3. Remova um aluno específico da lista que desistiu do curso
#4 Por fim, use o conceito de dicionario para que voce possa pesquisar um aluno 
# especifico dessa lista

alunos = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print("Lista de alunos:")
print(alunos)  # Imprime a lista de alunos

alunos.extend(['Frank', 'Grace'])
alunos.remove('Charlie')  # Remove o aluno 'Charlie' da lista
print("\nLista de alunos atualizada - aluno 'Charlie' removido:")
print(alunos)  # Imprime a lista de alunos atualizada

alunos_dict = {aluno: i for i, aluno in enumerate(alunos)}# Converte a lista de alunos em um dicionário, onde a chave é o nome do aluno e o valor é o índice na lista
print("\nDicionário de alunos:")
print(alunos_dict)  # Imprime o dicionário de alunos
aluno_pesquisado = 'Bob'
if aluno_pesquisado in alunos_dict:
    print(f'Aluno {aluno_pesquisado} encontrado no índice {alunos_dict[aluno_pesquisado]}.')
else:
    print('Aluno não encontrado.')
