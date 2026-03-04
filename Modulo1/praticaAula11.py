# 1. Crie um trecho de código try, catch(except) e finally
# 2. dentro da instrução try, coloque um trecho de códigos que efetue uma operação matemática de divisão entre duas variaveis
# 3. defina a mensagem erro e de sucesso que voce deseja exibir e insira ela nos respectivos comando de cada uma, conforme aprendeu na aula
#4. agora teste ir trocando o valor de uma das variaveis por um valor do tipo string, para verificar se o erro é tratado corretamente

#"trate seus programas como peças de literatura e trate erros como oportunidades para aprender" Donald Knuth

def funcaozinha(a, b):
    result = 0
    try:
     result = a/b
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except TypeError:
        print("Erro: não é possível dividir tipos diferentes de número.")
    finally:
        print("Desculpe, tente novamente!")

funcaozinha(9.0,10)