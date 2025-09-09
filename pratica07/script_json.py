import json

# Dados a serem escritos
pessoa = {
    "nome": "Daniel",
    "idade": 30,
    "cidade": "Curitiba"
}

# Escrita
with open("pessoa.json", "w", encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

# Leitura
with open("pessoa.json", "r", encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")
