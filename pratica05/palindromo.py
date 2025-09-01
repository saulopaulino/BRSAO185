"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

import string
def eh_palindromo(texto):
    try:
        # Remover espaços e pontuação, e converter para minúsculas
        texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
        # Verificar se o texto é igual ao seu reverso
        return texto_limpo == texto_limpo[::-1]
    except TypeError:
        return "Erro: O parâmetro deve ser uma string."
    
# Aplicação prática
entrada = input("Digite uma palavra ou frase: ")
if eh_palindromo(entrada):
    print(f"A entrada '{entrada}' é um palíndromo.")
else:
    print(f"A entrada '{entrada}' não é um palíndromo.")
def eh_palindromo(texto):
    try:
        # Remover espaços e pontuação, e converter para minúsculas
        texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
        # Verificar se o texto é igual ao seu reverso
        return texto_limpo == texto_limpo[::-1]
    except TypeError:
        return "Erro: O parâmetro deve ser uma string."