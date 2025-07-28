"""
1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.

---
"""

import random
import string

def gerar_senha_segura(tamanho):
    """
    Gera uma senha aleatória com letras maiúsculas, minúsculas, números e símbolos.

    Args:
        tamanho (int): O tamanho desejado para a senha.

    Returns:
        str: A senha gerada.
    """
    # Define os conjuntos de caracteres para a senha
    letrasMinusculas = string.ascii_lowercase
    letrasMaiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation # Inclui !@#$%&* etc.

    # Combina todos os tipos de caracteres
    todosCaracteres = letrasMinusculas + letrasMaiusculas + numeros + simbolos

    # Garante que a senha contenha pelo menos um de cada tipo, se o tamanho permitir
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser no mínimo 4 para incluir todos os tipos de caracteres.")

    senha = [
        random.choice(letrasMinusculas),
        random.choice(letrasMaiusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Preenche o restante da senha com caracteres aleatórios de todos os tipos
    for _ in range(tamanho - 4):
        senha.append(random.choice(todosCaracteres))

    # Embaralha a senha para garantir a aleatoriedade
    random.shuffle(senha)

    return "".join(senha)

if __name__ == "__main__":
    while True:
        try:
            tamanhoSenha = int(input("Digite o tamanho da senha desejada (ex: 8, 12, 16): "))
            if tamanhoSenha <= 0:
                print("Por favor, digite um número inteiro positivo para o tamanho da senha.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    try:
        senhaGerada = gerar_senha_segura(tamanhoSenha)
        print(f"\nSua senha segura gerada é: {senhaGerada}")
    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")