"""
Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.
"""

print("Salário por Horas Trabalhadas")
print("-" * 30)
print("\n")

# Entrada de dados
numero_funcionario = int(input("Informe o número do funcionário: "))
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Informe o valor recebido por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Saída formatada
print(f"\nNúmero do funcionário: {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")