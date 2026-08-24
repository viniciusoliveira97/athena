import os
from dotenv import load_dotenv
import requests

load_dotenv()

chave_api = os.getenv("API_FUTEBOL_KEY")

headers = {
    "Authorization": f"Bearer {chave_api}"
}

resposta = requests.get("https://api.api-futebol.com.br/v1/campeonatos/14/partidas", headers=headers)

print(resposta.status_code)