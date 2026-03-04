# 1. crie uma classe chmada carros
# 2. defina seus atributos, devem conter modelo, placa e ano
# 3. em seguida, crie os seguintes métodos: mostrarplaca() e ao instanciar a classe a partir de um objetos, mostre a placa deste veículo

class carros:
    def __init__(self, marca, ano, cor, placa):
        self.marca = marca
        self.ano = ano
        self.placa = placa
        self.cor = cor 

    def mostrarplaca(self):
        print(self.placa)

carro1 = carros("Fiat", 2020, "Preto", "ABC-1234")
carro2 = carros("Chevrolet", 2021, "Branco", "DEF-5678")
carro3 = carros("Volkswagen", 2019, "Vermelho", "GHI-9012")

carro1.mostrarplaca()
carro2.mostrarplaca()
carro3.mostrarplaca()