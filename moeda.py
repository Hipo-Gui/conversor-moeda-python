import requests, json


def apiDolar():
    # endereço da api
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    # request vai pegar os dados no formato json
    dados = requests.get(url, timeout=10).content #Vai pegar as informações com 10 segundos.

    # json.loads vai transformar em um dicionário python
    cotacao = json.loads(dados)

    return cotacao['USDBRL']['ask']

