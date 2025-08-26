while True:
    try:
        num1 = float(input("Digite o 1º número: "))
        num2 = float(input("Digite o 2º número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        print(f"O resultado é: {resultado}")
        break

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida. Por favor, tente novamente.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, tente novamente.")