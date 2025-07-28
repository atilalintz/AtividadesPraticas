"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""

import requests
from datetime import datetime
import time # Importa o módulo time para usar time.sleep()

def consultar_cotacao_moeda():
    """
    Solicita o código de uma moeda estrangeira, consulta sua cotação em relação ao Real
    e exibe informações. Trata erros de moeda inválida, falha na conexão e erro 429.
    """
    while True:
        moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP) ou 'sair' para finalizar: ").upper()
        if moeda == 'SAIR':
            print("Saindo do programa.")
            return

        if not moeda.isalpha() or len(moeda) != 3:
            print("Código de moeda inválido. Por favor, digite um código de 3 letras (ex: USD).")
            continue
        else:
            break

    responsta_url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    tentativas_maximas = 3  # Número máximo de tentativas
    atraso_inicial = 4     # Atraso inicial em segundos
    
    for tentativa in range(tentativas_maximas):
        try:
            response = requests.get(responsta_url)
            response.raise_for_status()  # Lança um erro para status de resposta HTTP ruins (4xx ou 5xx)
            
            dados = response.json()

            # A chave no JSON retornado é a moeda_BRL (ex: USDBRL, EURBRL)
            chave_moeda_brl = f"{moeda}BRL"

            if "erro" in dados and dados["erro"]: # Embora a AwesomeAPI não use muito 'erro: true', é bom manter para APIs genéricas
                 print(f"\nNão foi possível encontrar a cotação para '{moeda}'. Verifique o código da moeda.")
                 print("Lembre-se que algumas moedas podem não estar disponíveis ou o código pode estar incorreto.")
                 return
            elif chave_moeda_brl not in dados:
                print(f"\nNão foi possível encontrar a cotação para '{moeda}'. Verifique o código da moeda.")
                print("Lembre-se que algumas moedas podem não estar disponíveis ou o código pode estar incorreto.")
                return

            cotacao_info = dados[chave_moeda_brl]

            # Extraindo e formatando os dados
            nome_moeda = cotacao_info.get('name', 'Nome não disponível')
            valor_atual = float(cotacao_info.get('bid', 0))
            valor_maximo = float(cotacao_info.get('high', 0))
            valor_minimo = float(cotacao_info.get('low', 0))
            timestamp = int(cotacao_info.get('timestamp', 0))

            # Conversão do timestamp para data/hora legível
            data_hora_atualizacao = datetime.fromtimestamp(timestamp)

            print(f"\n--- Cotação de {nome_moeda} ({moeda}) para Real (BRL) ---")
            print(f"Cotação Atual (Compra): R$ {valor_atual:.4f}")
            print(f"Valor Máximo (24h): R$ {valor_maximo:.4f}")
            print(f"Valor Mínimo (24h): R$ {valor_minimo:.4f}")
            print(f"Última Atualização: {data_hora_atualizacao.strftime('%d/%m/%Y %H:%M:%S')}")
            print("--------------------------------------------------")
            return # Sai da função se a consulta for bem-sucedida

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                tempo_espera = atraso_inicial * (2 ** tentativa) # Atraso exponencial
                print(f"Erro 429: Limite de requisições excedido. Tentando novamente em {tempo_espera:.1f} segundos...")
                time.sleep(tempo_espera)
            else:
                print(f"\nErro HTTP: {e}")
                return # Sai da função para outros erros HTTP
        except requests.exceptions.ConnectionError:
            print("\nErro de conexão: Não foi possível conectar à internet ou à API da AwesomeAPI.")
            return
        except requests.exceptions.Timeout:
            print("\nErro de tempo limite: A requisição demorou muito para responder.")
            return
        except requests.exceptions.RequestException as e:
            print(f"\nErro na requisição à API: {e}")
            return
        except ValueError:
            print("\nErro: Resposta inesperada da API ou problema na conversão de valores.")
            return
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            return
            
    print(f"\nFalha ao obter a cotação após {tentativas_maximas} tentativas. Por favor, tente novamente mais tarde.")


if __name__ == "__main__":
    consultar_cotacao_moeda()