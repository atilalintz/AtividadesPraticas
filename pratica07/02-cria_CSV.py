"""
    2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""
import csv

def escreverDadosCSV():
    """
    Cria dados fictícios de pessoas, solicita um nome de arquivo ao usuário
    e escreve esses dados em um arquivo CSV com cabeçalhos.
    Trata possíveis erros de escrita.
    """
    # 1. Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
    dadosPessoas = [
        ["Nome", "Idade", "Cidade"],  # Cabeçalho
        ["Alice Silva", 30, "São Paulo"],
        ["Bruno Costa", 24, "Rio de Janeiro"],
        ["Carla Mendes", 35, "Belo Horizonte"],
        ["Daniel Pereira", 28, "Porto Alegre"]
    ]

    # 2. Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
    nomeArquivo = input("Digite o nome do arquivo CSV para salvar (ex: pessoas ou pessoas.csv): ")

    # Garante que a extensão .csv esteja presente, se o usuário não digitar
    if not nomeArquivo.lower().endswith('.csv'):
        nomeArquivo += '.csv'

    try:
        # Abre o arquivo no modo de escrita ('w') com 'newline=' para evitar linhas em branco extras
        with open(nomeArquivo, 'w', newline='', encoding='utf-8') as arquivoCSV:
            # 3. Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
            escritorCSV = csv.writer(arquivoCSV)
            for linha in dadosPessoas:
                escritorCSV.writerow(linha)

        # 4. Confirme a gravação exibindo uma mensagem com o nome do arquivo.
        print(f"\nDados salvos com sucesso no arquivo: '{nomeArquivo}'")

    # 5. Trate possíveis erros de escrita de arquivo.
    except IOError as e:
        print(f"\nErro de E/S (Entrada/Saída) ao escrever no arquivo '{nomeArquivo}': {e}")
        print("Verifique se você tem permissão de escrita ou se o nome do arquivo é válido.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao salvar o arquivo: {e}")

if __name__ == "__main__":
    escreverDadosCSV()