# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica a faixa etária e exibe a mensagem correspondente
if idade < 12:
    categoria = "criança"
elif idade < 60:
    categoria = "adulto"
else:
    categoria = "idoso"

# Exibe a mensagem final
print(f"{nome}, você é considerado(a) {categoria}.")
