# Autor
# Projeto: Try Execept

# try: Código de exceção

try:
    valor1 = float (input("Digite o 1° valor: "))
    valor2 = float (input("Digite o 2° valor: "))
    soma = valor1+valor2
    print(f"O resultado da soma é: {soma}")
except:
    print("Caro usuário, você não digitou um número!")
    print("-----Digite um número válido!-----")
