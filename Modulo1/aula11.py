def dividir(a,b):
    r = 0
    try:
        r = a/b
        return print(r)
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except:
        print("Erro inesperado, desculpe.")
    finally:
        print("Operação de divisão finalizada.")
#geralmente não usamos print ao usar resturn - ou seja, dentro da função - para deixar o código mais versátil, mais limpo

dividir(4,"a") #TEM que chamar a função para que ela seja mostrada (amostradinha)
#enviar valores é enviar argumentos, os argumentos é o que a gente manda para os parametros

#quem é nina e pq mutou


#FUNÇÃO LOCAl: funciona apenas dentro da função
# FUNCÇÃO GLOBAL: vai funcionar em cada canto do código
