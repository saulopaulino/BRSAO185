""""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Variáveis

distancia_percorrida = 300  # em km
combustivel_gasto = 25  # em litros

# Cálculo
consumo_medio = distancia_percorrida / combustivel_gasto  # km/l

# Exibição do resultado

print("-" * 30)
print("Dados da Viagem")
print("\n")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print("\n")
print("-" * 30)
print(f"Consumo médio: {consumo_medio:.2f} km/l")
print("-" * 30)

# Fim do programa
# Este programa calcula o consumo médio de combustível de um veículo com base na distância percorrida  
