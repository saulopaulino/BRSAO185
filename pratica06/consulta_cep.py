import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    if "erro" not in dados:
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP não encontrado.")
else:
    print("Erro ao consultar o CEP.")
