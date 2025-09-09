import re
import statistics

tempos = []

with open("log_treinamento.txt", "r") as arquivo:
    for linha in arquivo:
        match = re.search(r"Tempo de execução: (\d+\.\d+)", linha)
        if match:
            tempos.append(float(match.group(1)))

media = statistics.mean(tempos)
desvio = statistics.stdev(tempos)

print(f"Média: {media:.2f} segundos")
print(f"Desvio padrão: {desvio:.2f} segundos")
