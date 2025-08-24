nome = input()
salario_fixo = float(input())
vendas = float(input())

comissao = vendas * 0.15
total = salario_fixo + comissao

print(f"TOTAL = R$ {total:.2f}")
