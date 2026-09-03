# Autor: Daniel Pina
# Projeto: Uso de API 
# Desafio: Clima atual Mairinque

import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -23.545833,
    "longitude": -47.183333,
    "current": "temperature_2m,wind_speed_10m",
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
dados = response.json()

print(f"Temperatura atual em Mairinque: {dados['current']['temperature_2m']}°C")