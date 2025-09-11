import random
import time
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Função para tocar a música
def tocar_musica():
    pygame.mixer.music.load("champions.mp3")
    pygame.mixer.music.play(-1)  # -1 para repetir continuamente

# Função para parar a música
def parar_musica():
    pygame.mixer.music.stop()

# Lista dos grupos com seus integrantes
grupos = {
    "GRUPO 01": [
        "Amanda Gonçalves Taraborelli Sanchez",
        "Christopher Gonçalves Cruz",
        "Fernanda Avila Batista",
        "Henrique Costa Gonçalves",
        "Leandra Sousa",
        "Rafaela Fernanda De Carvalho Corrêa",
        "Wellington Candido De Souza"
    ],
    "GRUPO 02": [
        "Amanda Rocha Santos",
        "Claudio Luiz kaminski Junior",
        "Filipe De Siqueira Fogaça",
        "Ícaro Torres Mendes",
        "Luciana Lira De Menezes",
        "Roberta Alexandre De Arruda Dalia",
        "Yago Vilela"
    ],
    "GRUPO 03": [
        "Ana Luiza Menelli Taylor",
        "Davi Eduardo S. Agostinho",
        "Geiciele Patricia Tarcísio",
        "Ingrid Nascimento",
        "Maria Rita do Nascimento Vieira",
        "Saulo Paulino"
    ],
    "GRUPO 04": [
        "André Junckes Da Silva Mattos",
        "Douglas Araujo De Brito",
        "Geisiane Martins Do Nascimento",
        "Ingrid Silva",
        "Mikaely De Oliveira Almeida",
        "Shirley Rocha De Assis"
    ],
    "GRUPO 05": [
        "Carla Alessandra De Brito Lima",
        "Emauelle De Jesus Pinto Motta",
        "Giovana Alice Mendes Gouveia",
        "João Victor De Araújo Moura",
        "Mirella Priscilla Pereira Dos Santos",
        "Telio Mauricio Do Nascimento"
    ],
    "GRUPO 06": [
        "Caroline Suisso Do Nascimento",
        "Felipe Gabriel Da Silva",
        "Glória Gonzalez Blanco",
        "Ketlen Dos Santos Dutra",
        "Pedro Henrique Da Silva",
        "Valeria Alejandra Córdova Espejo"
    ]
}

# Título
print("🌥️ SORTEIO DA ORDEM DE APRESENTAÇÃO DE GRUPOS")
print("TCC - ESCOLA DA NUVEM\n")

# Embaralha os grupos
grupos_keys = list(grupos.keys())
random.shuffle(grupos_keys)

# Inicia a música
tocar_musica()

# Sorteio interativo com contagem regressiva
ordem_apresentacao = []
for i in range(len(grupos_keys)):
    input(f"PRESSIONE ENTER para sortear a {i+1}ª equipe:")
    print("Sorteando em...")
    for segundos in range(3, 0, -1):
        print(f"{segundos}...")
        time.sleep(1)
    sorteado = grupos_keys.pop(0)
    ordem_apresentacao.append(sorteado)
    print(f"\n🎉 {sorteado} foi sorteado!")
    print("Integrantes:")
    for nome in grupos[sorteado]:
        print(f"- {nome}")
    print("\n" + "-"*40 + "\n")

# Para a música antes de revelar a ordem final
parar_musica()

# Exibe a ordem final
print("📋 ORDEM FINAL DE APRESENTAÇÃO:")
for idx, grupo in enumerate(ordem_apresentacao, start=1):
    print(f"{idx}º - {grupo}")
print("\nBoa sorte a todos os grupos! 🍀")