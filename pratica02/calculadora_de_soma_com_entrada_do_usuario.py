"""
Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.
"""

# Variáveis
print("Qual é o valor de X?")
print("\n")
var_A = int(input("Informe o valor de A: "))
print("\n")
var_B = int(input("Informe o valor de B: "))

# Cálculo

var_X = var_A + var_B

# Exibição do Resultado
print("\n")
print("Resultado")
print('-' * 30 )
print(f"O valor de X = {var_X}, sendo que o cálculo foi X = {var_A} + {var_B}")

# Fim do Programa