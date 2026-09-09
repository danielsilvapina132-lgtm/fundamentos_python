# Autor
# Projeto: Try Execept
# except: Tratamento de exceção
# try: Código de exceção

def divisao():
    try:
        valor1 = float (input("Digite o 1° valor: "))
        valor2 = float (input("Digite o 2° valor: "))
        divisao = valor1/valor2
        
    except ZeroDivisionError:

        print("Caro usuário, não é possível dividir um número por 0!!")
        print("-----Digite um número maior que 0!-----") 
    except ValueError:
        print("Digite apenas números!")
    else: 
        print(f"O resultado da divisão é: {divisao}")

divisao()


