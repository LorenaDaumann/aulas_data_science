import pandas as pd

#criando uma serie
serie = pd.Series([1, 2, 3, 4, 5])
print(serie)

data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)
print(df)

print(df['Nome'])

#acessando uma linha
print(df.iloc[0])

#acessando um valor específico
print(df.loc[0, 'Nome'])

#pd.read_csv('caminho/para/seu/arquivo.csv') #para ler um arquivo csv e criar um DataFrame a partir dele