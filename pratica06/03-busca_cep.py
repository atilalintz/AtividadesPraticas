"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""
import requests


def consultar_cep():
    """
    Solicita um CEP ao usuário, consulta a API ViaCEP e exibe os dados do endereço.
    Trata casos de CEP inválido, não encontrado ou erros de conexão.
    """
    while True:
        cep = input("Digite o CEP (apenas números, sem traço): ")

        # Validação básica do CEP
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Por favor, digite 8 dígitos numéricos.")
            continue # Pede o CEP novamente
        else:
            break # Sai do loop se o CEP for válido

    api_url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lança um erro para status de resposta HTTP ruins (4xx ou 5xx)
        dados = response.json()

        # Verifica se o CEP foi encontrado (a API ViaCEP retorna 'erro' se não encontrar)
        if "erro" in dados and dados["erro"]:
            print(f"\nCEP '{cep}' não encontrado.")
        else:
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {dados.get('cep', 'Não disponível')}")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
            print("-------------------------------")

    except requests.exceptions.ConnectionError:
        print("\nErro de conexão: Não foi possível conectar à internet ou à API do ViaCEP.")
    except requests.exceptions.Timeout:
        print("\nErro de tempo limite: A requisição demorou muito para responder.")
    except requests.exceptions.RequestException as e:
        print(f"\nErro na requisição à API do ViaCEP: {e}")
    except ValueError:
        print("\nErro: Resposta inesperada da API. Não foi possível decodificar o JSON.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    consultar_cep()