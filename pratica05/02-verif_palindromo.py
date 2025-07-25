import unicodedata # Módulo para remover acentos
import re          # Módulo para remover pontuação

def verificar_palindromo(texto: str) -> bool:
    """
    Verifica se uma palavra ou frase é um palíndromo, desconsiderando
    espaços, acentos, pontuação e letras maiúsculas/minúsculas.

    Parâmetros:
    texto (str): A palavra ou frase a ser verificada.

    Retorna:
    bool: True se for um palíndromo, False caso contrário.
    """
    # 1. Converter para minúsculas
    texto_processado = texto.lower()

    # 2. Remover acentos (normaliza e remove caracteres de combinação)
    texto_processado = unicodedata.normalize('NFD', texto_processado)
    texto_processado = texto_processado.encode('ascii', 'ignore').decode('utf-8')

    # 3. Remover espaços e pontuação
    # O padrão '[^a-z0-9]' significa "qualquer coisa que NÃO seja uma letra de 'a' a 'z' ou um dígito de '0' a '9'"
    texto_processado = re.sub(r'[^a-z0-9]', '', texto_processado)

    # 4. Comparar a string processada com sua versão invertida
    return texto_processado == texto_processado[::-1]

# --- Solicita a entrada do usuário ---
frase_ou_palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

# --- Verifica e exibe o resultado ---
if verificar_palindromo(frase_ou_palavra):
    print(f"A frase/palavra '{frase_ou_palavra}' é um palíndromo.")
else:
    print(f"A frase/palavra '{frase_ou_palavra}' NÃO é um palíndromo.")
    