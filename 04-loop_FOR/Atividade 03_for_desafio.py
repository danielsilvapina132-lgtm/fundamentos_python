#Autor:Daniel Pina
#Projeto : Desafio Fatorial

#A expressão completa fica assim:
# 
numero = int(input('digite o fatorial desejado:'))
fatorial = 1

for i in range(1,numero+1):
    # calculo da fatorial 
    fatorial=fatorial*i
     
    #print do resultado
    print(f'Fatorial: {fatorial}')