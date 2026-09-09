# Autor: Daniel Pina
# Projeto: Programa IMC com função e tratamento de exceção
# except: Tratamento de exceção
# try: Código de exceção

def imc():
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = peso / (altura*altura)
    except ZeroDivisionError as e:
        print("Caro usuário, não é possível dividir um número por 0!!")
        print("-----Digite um número maior que 0!-----") 
    except ValueError:
        print("Digite apenas números!")
    else: 
        print(f"O resultado da divisão é: {imc:.2f} ")
    if imc <= 18.5:
        print("Cuidado magreza!")
    elif imc <= 25.0:
        print("Você está saudável")
    elif imc <= 35:
        print("Alerta! Você está com sobrepeso!")
                
        
imc()
  












