import requests

# Chave de API da NASA
api_key = "geZSNvabmUiJUHQKhlotgSGPBq58e1et1tVh57aj"

# URL da API da NASA para obter informações sobre asteroides próximos da Terra
url = "https://api.nasa.gov/neo/rest/v1/feed"

# Data de início e fim da pesquisa
start_date = "2023-02-26"
end_date = "2023-02-27"

# Parâmetros da consulta
query_params = {
    "start_date": start_date,
    "end_date": end_date,
    "api_key": api_key
}

# Fazer a solicitação à API da NASA
response = requests.get(url, params=query_params)

# Analisar os dados retornados pela API
data = response.json()

# Obter informações sobre asteroides
asteroids = data["near_earth_objects"][start_date]

# Imprimir informações sobre os asteroides
for asteroid in asteroids:
    print("Nome:", asteroid["name"])
    print("Diâmetro:", asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
          "-", asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"], "km")
    print("Distância:", asteroid["close_approach_data"][0]["miss_distance"]["kilometers"], "km")
    print("Velocidade:", asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"], "km/s")
    print("-" * 40)
