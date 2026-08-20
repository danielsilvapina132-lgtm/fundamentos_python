# Autor: Grupo 2
# Projeto: Cálculo Gasolina x Etanol
print ('qual combustivel é mais vantajoso abastecer?')
nome = input('qual seu nome?')
etanol = float(input('qual o valor atual do etanol na sua região?'))
gasolina = float(input('qual o valor atual da gasolina na sua região?'))

resultado = etanol/gasolina

if resultado < 0.70 :
      print(f'vale mais a pena utilizar etanol!')

else :
      print(f'vale mais a pena utilizar gasolina!')
