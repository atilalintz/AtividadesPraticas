import requests

def gerar_usuario_aleatorio():
    """
    Acessa a API randomuser.me, obtém dados de um usuário fictício e os exibe.
    Trata possíveis erros de conexão ou falha na API.
    """
    responsta_url = "https://randomuser.me/api/?nat=br"

    try:
        response = requests.get(responsta_url)
        response.raise_for_status()  # Lança um erro para status de resposta HTTP ruins (4xx ou 5xx)
        data = response.json()

        # Extrai as informações do usuário
        usuario = data['results'][0]
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        # Exibe as informações
        print("--- Informações do Usuário Aleatório ---")
        print(f"Nome Completo: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print("---------------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ou falha na API: {e}")
    except KeyError:
        print("Erro: Não foi possível extrair os dados esperados da API. A estrutura da resposta pode ter mudado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    gerar_usuario_aleatorio()