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

    responstaUrl = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    tentativasMaximas = 3  # Número máximo de tentativas
    atrasoInicial = 1     # Atraso inicial em segundos
    
    for tentativa in range(tentativasMaximas):
        try:
            response = requests.get(responstaUrl)
            response.raise_for_status()  # Lança um erro para status de resposta HTTP ruins (4xx ou 5xx)
            
            dados = response.json()

            # A chave no JSON retornado é a moeda_BRL (ex: USDBRL, EURBRL)
            chaveMoedaBRL = f"{moeda}BRL"

            if "erro" in dados and dados["erro"]: # Embora a AwesomeAPI não use muito 'erro: true', é bom manter para APIs genéricas
                 print(f"\nNão foi possível encontrar a cotação para '{moeda}'. Verifique o código da moeda.")
                 print("Lembre-se que algumas moedas podem não estar disponíveis ou o código pode estar incorreto.")
                 return
            elif chaveMoedaBRL not in dados:
                print(f"\nNão foi possível encontrar a cotação para '{moeda}'. Verifique o código da moeda.")
                print("Lembre-se que algumas moedas podem não estar disponíveis ou o código pode estar incorreto.")
                return

            cotacaoInfo = dados[chaveMoedaBRL]

            # Extraindo e formatando os dados
            nomeMoeda = cotacaoInfo.get('name', 'Nome não disponível')
            valorAtual = float(cotacaoInfo.get('bid', 0))
            valorMaximo = float(cotacaoInfo.get('high', 0))
            valorMinimo = float(cotacaoInfo.get('low', 0))
            timestamp = int(cotacaoInfo.get('timestamp', 0))

            # Conversão do timestamp para data/hora legível
            dataHoraAtualizacao = datetime.fromtimestamp(timestamp)

            print(f"\n--- Cotação de {nomeMoeda} ({moeda}) para Real (BRL) ---")
            print(f"Cotação Atual (Compra): R$ {valorAtual:.4f}")
            print(f"Valor Máximo (24h): R$ {valorMaximo:.4f}")
            print(f"Valor Mínimo (24h): R$ {valorMinimo:.4f}")
            print(f"Última Atualização: {dataHoraAtualizacao.strftime('%d/%m/%Y %H:%M:%S')}")
            print("--------------------------------------------------")
            return # Sai da função se a consulta for bem-sucedida

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                tempoEspera = atrasoInicial * (2 ** tentativa) # Atraso exponencial
                print(f"Erro 429: Limite de requisições excedido. Tentando novamente em {tempoEspera:.1f} segundos...")
                time.sleep(tempoEspera)
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
            
    print(f"\nFalha ao obter a cotação após {tentativasMaximas} tentativas. Por favor, tente novamente mais tarde.")


if __name__ == "__main__":
    consultar_cotacao_moeda()