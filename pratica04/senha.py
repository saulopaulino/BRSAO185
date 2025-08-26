"""""
Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

"""
import getpass

print("\n")
print("Verificador de Senha Forte")
print('-' * 30)
print("Regras para uma senha forte:")
print("1. Deve ter pelo menos 8 caracteres.")
print("2. Deve conter pelo menos um número.")
print("\n")
print("Digite 'sair' para encerrar o programa.")
print("\n")
while True:
    senha = getpass.getpass("Digite uma senha: ").strip()
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    try:
        if len(senha) < 8:
            metade = len(senha) // 2
            senha_masc = senha[:metade] + '*' * (len(senha) - metade)
            raise ValueError(f"A senha '{senha_masc}' é inválida. Deve conter pelo menos 8 caracteres.")
        if not any(char.isdigit() for char in senha):
            metade = len(senha) // 2
            senha_masc = senha[:metade] + '*' * (len(senha) - metade)
            raise ValueError(f"A senha '{senha_masc}' é inválida. Deve conter pelo menos um número.")
        if not any(char.isalpha() for char in senha):
            metade = len(senha) // 2
            senha_masc = senha[:metade] + '*' * (len(senha) - metade)
            raise ValueError(f"A senha '{senha_masc}' é inválida. Deve conter pelo menos uma letra.")
        # Solicita confirmação
        confirmacao = getpass.getpass("A senha é válida. Confirme a senha: ").strip()
        if senha == confirmacao:
            senha_masc = senha[:2] + '*' * (len(senha) - 2)
            print(f"Senha forte! A senha '{senha_masc}' foi aceita e confirmada.")
            break
        else:
            print("As senhas não coincidem. Por favor, tente novamente.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, tente novamente.")