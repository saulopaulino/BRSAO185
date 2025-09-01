"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
def calcular_idade_em_dias(ano_nascimento, ano_atual):
    try:
        if ano_nascimento > ano_atual:
            raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
        idade_anos = ano_atual - ano_nascimento
        idade_dias = idade_anos * 365  # Ignorando anos bissextos para simplificação
        return idade_dias
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números inteiros."
    
# Aplicação prática
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
print(f"Idade em dias: {idade_em_dias} dias")
def calcular_idade_em_dias(ano_nascimento, ano_atual):
    try:
        if ano_nascimento > ano_atual:
            raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
        idade_anos = ano_atual - ano_nascimento
        idade_dias = idade_anos * 365  # Ignorando anos bissextos para simplificação
        return idade_dias
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números inteiros."
