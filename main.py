# O que é um webhook?
# Um webhook é uma maneira de um aplicativo fornecer informações em tempo real para outros aplicativos.
# Ele é um "gancho" que permite que um aplicativo envie dados automaticamente para outro aplicativo quando um evento específico ocorre.

# Nesse exemplo, vou usar o site webhook.site para criar um webhook e enviar uma requisição POST para ele.

import requests
import json

URL = "https://webhook.site/940e8df9-4cbc-434b-9199-86f6b9080625" # URL do webhook.site

# Data precisa ser um dicionário no formato json
dict_data = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

dict_data_json = json.dumps(dict_data) # Converte o dicionário para json

requests.post(URL, data=dict_data_json)