# Autor: Daniel Pina
# Projeto:  Estudando as funções

valor1 = float(input('digite o primeiro valor: '))
valor2 = float(input('digite o segundo valor: '))
soma = valor1+valor2
subtracao = valor1-valor2
multiplicacao = valor1*valor2
divisao = valor1/valor2
print(f'O valor da soma é: {soma}')
print(f'O valor da subtracao é: {subtracao}')
print(f'O valor da multiplicacao é: {multiplicacao}')
print(f'O valor da divisao é: {divisao}')

# função para realizar os calculos 
def calculadora(valor1,valor2):
    soma = valor1+valor2
    subtracao = valor1-valor2
    multiplicacao = valor1*valor2
    divisao = valor1/valor2

    print(f'O valor da soma é: {soma}')
    print(f'O valor da subtracao é: {subtracao}')
    print(f'O valor da multiplicacao é: {multiplicacao}')
    print(f'O valor da divisao é: {divisao}')








# entrada de dados 
valor1 = float(input('digite o primeiro valor: '))
valor2 = float(input('digite o segundo valor: '))

# chamada da função
calculadora = (valor1,valor2)




