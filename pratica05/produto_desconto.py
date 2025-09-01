"""
Crie um programa que receba o preço original de um produto e um percentual de desconto,
 realizando o cálculo do preço final após a aplicação do desconto. 
 
 Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 

Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcular_preco_com_desconto(preco_original, percentual_desconto):
    try:
        if preco_original < 0 or percentual_desconto < 0:
            raise ValueError("O preço do produto e o percentual de desconto devem ser números não negativos.")
        desconto = (preco_original * percentual_desconto) / 100
        preco_final = preco_original - desconto
        return round(preco_final, 2)
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números."
    
# Aplicação prática
preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
preco_final = calcular_preco_com_desconto(preco_original, percentual_desconto)
print(f"Preço final após desconto: R$ {preco_final:.2f}")
def calcular_preco_com_desconto(preco_original, percentual_desconto):
    try:
        if preco_original < 0 or percentual_desconto < 0:
            raise ValueError("O preço do produto e o percentual de desconto devem ser números não negativos.")
        desconto = (preco_original * percentual_desconto) / 100
        preco_final = preco_original - desconto
        return round(preco_final, 2)
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números."