"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no 
valor total da conta e na porcentagem de gorjeta desejada. Calcule o valor da 
gorjeta baseado no total da conta e na porcentagem desejada.

 Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta
   (float): A porcentagem da gorjeta (ex: 15 para 15%)
   Retorna: float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    try:
        if valor_conta < 0 or porcentagem_gorjeta < 0:
            raise ValueError("O valor da conta e a porcentagem da gorjeta devem ser números não negativos.")
        gorjeta = (valor_conta * porcentagem_gorjeta) / 100
        return gorjeta
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números."
    
# Aplicação prática
valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta desejada: "))
valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    try:
        if valor_conta < 0 or porcentagem_gorjeta < 0:
            raise ValueError("O valor da conta e a porcentagem da gorjeta devem ser números não negativos.")
        gorjeta = (valor_conta * porcentagem_gorjeta) / 100
        return gorjeta
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números."