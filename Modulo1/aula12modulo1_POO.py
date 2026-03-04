class Pessoa: #por padrao inicie o nome da classe com MAIUSCULA
    def __init__(self, nome, idade, altura):  #toda vez que criar um objeto da classe, o METODO CONSTRUTOR é chamado automaticamente
        #self representa a classe
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha altura é {self.altura}m.")

pessoa1 = Pessoa("José", 18, "1.80")
pessoa2 = Pessoa("Lorena", 18, "1.70")
pessoa1.apresentar()
pessoa2.apresentar()