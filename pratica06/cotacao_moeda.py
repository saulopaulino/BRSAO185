import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    chave = f"{moeda}BRL"
    cotacao = dados[chave]
    print(f"Moeda: {moeda}")
    print(f"Valor Atual: R$ {cotacao['bid']}")
    print(f"Valor Máximo: R$ {cotacao['high']}")
    print(f"Valor Mínimo: R$ {cotacao['low']}")
    print(f"Última Atualização: {cotacao['create_date']}")
else:
    print("Erro ao consultar a cotação.")
