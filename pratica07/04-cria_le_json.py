"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json
import os # Importa o módulo os para verificar a existência do arquivo

def criaLeJSON():
    # 1. Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
    dadosPessoa = {
        "nome": "Mariana Souza",
        "idade": 29,
        "cidade": "Campinas"
    }

    print("--- Dados da Pessoa para Salvar ---")
    for chave, valor in dadosPessoa.items():
        print(f"{chave.capitalize()}: {valor}")
    print("----------------------------------\n")

    # 2. Solicite ao usuário o nome do arquivo JSON.
    nomeArquivo = input("Digite o nome do arquivo JSON para salvar/ler (ex: pessoa.json): ")

    # Garante que a extensão .json esteja presente
    if not nomeArquivo.lower().endswith('.json'):
        nomeArquivo += '.json'

    # --- Parte de Escrita do Arquivo JSON ---
    print(f"\nTentando salvar dados no arquivo: '{nomeArquivo}'...")
    try:
        # 3. Salve os dados no arquivo usando o módulo `json`.
        with open(nomeArquivo, 'w', encoding='utf-8') as arquivoJSON:
            json.dump(dadosPessoa, arquivoJSON, indent=4, ensure_ascii=False)
            # 'indent=4' para formatar o JSON com identação para melhor legibilidade
            # 'ensure_ascii=False' para permitir caracteres não-ASCII (como acentos) serem salvos diretamente
        
        # 4. Confirma a gravação
        print(f"Dados salvos com sucesso no arquivo: '{nomeArquivo}'")

    except IOError as e:
        print(f"\nErro de E/S (Entrada/Saída) ao escrever no arquivo '{nomeArquivo}': {e}")
        print("Verifique se você tem permissão de escrita ou se o nome do arquivo é válido.")
        return # Sai da função se houver erro na escrita
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao salvar o arquivo: {e}")
        return # Sai da função se houver erro na escrita

    # --- Parte de Leitura do Arquivo JSON ---
    print(f"\nTentando ler dados do arquivo: '{nomeArquivo}'...")
    # Trata possível erro de ausência do arquivo (embora tenhamos acabado de escrever, é bom para reuso)
    if not os.path.exists(nomeArquivo):
        print(f"\nErro: O arquivo '{nomeArquivo}' não foi encontrado para leitura.")
        return

    try:
        # 4. Após salvar, leia o mesmo arquivo
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivoJSON:
            dadosCarregados = json.load(arquivoJSON)
        
        # 4. ...e imprima os dados carregados.
        print(f"\n--- Dados Carregados do Arquivo '{nomeArquivo}' ---")
        for chave, valor in dadosCarregados.items():
            print(f"{chave.capitalize()}: {valor}")
        print("-------------------------------------------------")

    except FileNotFoundError: # Este erro é mais específico que IOError para o caso de leitura
        print(f"\nErro: O arquivo '{nomeArquivo}' não foi encontrado para leitura. Ele pode ter sido movido ou excluído após a escrita.")
    except json.JSONDecodeError as e:
        print(f"\nErro ao decodificar JSON do arquivo '{nomeArquivo}': {e}")
        print("O arquivo pode estar corrompido ou não é um JSON válido.")
    except IOError as e:
        print(f"\nErro de E/S (Entrada/Saída) ao ler o arquivo '{nomeArquivo}': {e}")
        print("Verifique se você tem permissão de leitura.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao ler o arquivo: {e}")

if __name__ == "__main__":
    criaLeJSON()