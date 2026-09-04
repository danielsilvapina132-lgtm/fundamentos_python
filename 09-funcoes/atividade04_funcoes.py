# Autor: Daniel Pina
# Projeto: Funções dentro de funções

# função principal
def calcular ():
    # função juros simples = c * i * t
    def juros_simples(c, i, t):
        return c * i * t
    # função juros compostos 
    def juros_composto(c, i, t):
        return c *(1 + i) **t - c 

    # escolha a função
    op = input('Escolha 1-Juros Simples ou 2-Juros Compostos')

    # Entrada de dados 
    c = float(input('Digite o capital: '))
    i = float(input('Digite a taxa: (ex: 0.05): ')) 
    t = float(input('Digite as parcelas: '))

    # Condicional que escolhe a operação
    if op == '1':
        print(juros_simples(c, i, t))
    else:
        print(juros_composto(c, i, t))

calcular()