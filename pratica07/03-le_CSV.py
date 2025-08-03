"""
    3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
"""

import csv
import os # Importa o módulo os para verificar a existência do arquivo

def lerDadosCSV():
    # 1. Solicite ao usuário o nome do arquivo CSV a ser lido.
    nomeArquivo = input("Digite o nome do arquivo CSV para ler (ex: pessoas.csv): ")

    # Garante que a extensão .csv esteja presente, se o usuário não digitar
    if not nomeArquivo.lower().endswith('.csv'):
        nomeArquivo += '.csv'

    # 4. Trate erros como arquivo inexistente
    if not os.path.exists(nomeArquivo):
        print(f"\nErro: O arquivo '{nomeArquivo}' não foi encontrado no diretório atual.")
        return

    try:
        # Abre o arquivo no modo de leitura ('r')
        # 'newline=' é importante para o csv.reader também, evitando problemas de quebra de linha
        # 'encoding=' garante que caracteres especiais sejam lidos corretamente
        with open(nomeArquivo, 'r', newline='', encoding='utf-8') as arquivoCSV:
            # 2. Utilize o módulo `csv` para abrir o arquivo e ler os dados.
            leitorCSV = csv.reader(arquivoCSV)

            print(f"\n--- Conteúdo do arquivo '{nomeArquivo}' ---")
            for linha in leitorCSV:
                print(linha)

    # 4. Trate erros como problemas na leitura.
    except IOError as e:
        print(f"\nErro de E/S (Entrada/Saída) ao ler o arquivo '{nomeArquivo}': {e}")
        print("Verifique se o arquivo não está corrompido ou se você tem permissão de leitura.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao ler o arquivo: {e}")

if __name__ == "__main__":
    lerDadosCSV()