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
    textoProcessado = texto.lower()

    # 2. Remover acentos (normaliza e remove caracteres de combinação)
    textoProcessado = unicodedata.normalize('NFD', textoProcessado)
    textoProcessado = textoProcessado.encode('ascii', 'ignore').decode('utf-8')

    # 3. Remover espaços e pontuação
    # O padrão '[^a-z0-9]' significa "qualquer coisa que NÃO seja uma letra de 'a' a 'z' ou um dígito de '0' a '9'"
    textoProcessado = re.sub(r'[^a-z0-9]', '', textoProcessado)

    # 4. Comparar a string processada com sua versão invertida
    return textoProcessado == textoProcessado[::-1]

# --- Solicita a entrada do usuário ---
frasePalavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

# --- Verifica e exibe o resultado ---
if verificar_palindromo(frasePalavra):
    print(f"A frase/palavra '{frasePalavra}' é um palíndromo.")
else:
    print(f"A frase/palavra '{frasePalavra}' NÃO é um palíndromo.")
    