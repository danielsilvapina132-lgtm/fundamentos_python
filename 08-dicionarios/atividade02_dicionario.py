# Autor: Daniel Pina
# Projeto: Uso de API (conceito de dicionário)

# requisições http - GET
import requests

# uso da API da Shopee Express
# 18123-020
cep = input("Digite seu CEP (somente números):"). strip().replace("-","")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")