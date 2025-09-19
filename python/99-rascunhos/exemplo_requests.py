import requests

url = "https://www.rocketseat.com.br"

response = requests.get(url)

print(f"Solicitação HTTP para {url} retornou o statut {response.status_code}")