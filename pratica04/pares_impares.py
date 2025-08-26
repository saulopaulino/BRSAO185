""""
Crie um programa que solicite ao usuário que insira números inteiros.
O programa deve continuar solicitando números até que o usuário digite 'fim'.
Para cada número inserido, o programa deve informar se é par ou ímpar. 
Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
"""

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()
    if entrada.lower() == 'fim':
        print("Programa encerrado. Veja o resultado:")
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
            print(f"O número {numero} é par.")
        else:
            impares += 1
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print(f"Este dado não é um número. Por favor, insira um número inteiro.")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
