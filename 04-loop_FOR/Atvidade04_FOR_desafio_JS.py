#Autor:Daniel Pina
#Projeto : Desafio JS 

# variaveis e entrada de dados 

c = float(input('digite o capital inicial:'))
i = float(input('digite a taxa:'))
t = float(input('digite o tempo (meses):'))

#calculos
j= c*i*t
montante = j + c


# impressão do resultado
print(f'a taxa é {j}. e o montante é: {montante}')
