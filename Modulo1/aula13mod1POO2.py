class Pessoa: #por padrao inicie o nome da classe com MAIUSCULA
    def __init__(self, nome, idade, altura):  #toda vez que criar um objeto da classe, o METODO CONSTRUTOR é chamado automaticamente
        #self representa a classe
        self.__nome = nome
        self.__idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos e minha altura é {self.altura}m.")

    def get_nome(self):
        return self.__nome
    
    def set_idade(self, nova_idade):
        if nova_idade >= 40:
            self.__idade = nova_idade


pessoa1 = Pessoa("\nJosé", 17, "1.80")
pessoa2 = Pessoa("\nLorena", 18, "1.70")
pessoa1.apresentar()
pessoa2.apresentar()

# print(pessoa1.nome) #público 0o0
pessoa1.set_idade(45)
pessoa1.apresentar()
print(pessoa1.get_nome()) #privado 




class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura) #maneira para acessar tudo da classe mãe, sem precisar repetir o código
        self.matricula = matricula

    def estudante(self):
        super().apresentar()
        print(f"A matrícula do aluno é {self.matricula}.")

    def apresentar(self):
        print(f"Olá, meu nome é {super().get_nome()}, tenho {self.__idade} anos e minha matrícula é {self.matricula}.")

aluno1 = Aluno("Maria", 20, "1.65", "2023001")
aluno1.estudante()

################PRATICAR CLASSES E OBJETOS COM DIFERENTES NIVEIS DE COMPLEXIDADE##########################
##ACESSAR AULA 13 PARA RECURSOS (SITE, FILMES E LIVROS)