# Autor: Daniel Pina
# Projeto: Dicionários

# Projeto aquele lá

escola = {
    "salas":"sala_musica",
    "localizacao": "bloco_A",
    "qtd_lugares":"40",
    "caracteristica":"acustica"
    }

# Acessando dados do dicionário
print(f'Sala disponivel{escola["salas"]}')

#Adicionando mais itens ao dicionário
escola["iluminacao"] =  "led"
print(f'Sala disponivel {escola["iluminacao"]}')

# Alterando um valor do dicionário
escola["salas"] =  "sala"
print(f'Sala disponivel {escola["salas"]}')