"""Crie um programa que permita a um professor registrar as notas de uma turma.
 O programa deve continuar solicitando notas até que o professor digite 'fim'. 
 Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
 No final, deve exibir a média da turma."""""
notas = []

while True:
    try:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip()
        if entrada.lower() == 'fim':
            break
        
        # Substitui vírgula por ponto
        entrada = entrada.replace(',', '.')
        
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
            print(f"Nota {nota} é um valor válido e foi registrada com sucesso.")
        else:
            raise ValueError("Nota inválida! O valor deve estar entre 0 e 10.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, tente novamente.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média das notas: {media:.2f}")
    print(f"Total de notas válidas: {len(notas)}")
else:
    print("Nenhuma nota válida foi registrada.")
