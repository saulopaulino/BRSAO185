""""
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:



Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

# Variáveis
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo
valor_desconto = (preco_original * porcentagem_desconto) / 100
preco_final = preco_original - valor_desconto

# Exibição do resultado
print("-" * 30)
print("Produto")
print(f"Nome: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Porcentagem de Desconto: {porcentagem_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
print("-" * 30)
print("Desconto calculado com sucesso!")
print("-" * 30)
print("Obrigado por usar o calculador de desconto!")
print("-" * 30)
# Fim do programa
# Este programa calcula o desconto de um produto e exibe os detalhes do produto, incluindo o nome, preço original, porcentagem de desconto, valor do desconto e preço final após o desconto.
