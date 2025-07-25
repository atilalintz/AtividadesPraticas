import datetime # Módulo para conseguir o ano atual automaticamente

print("--- Calculadora de Idade em Dias ---")

# 1. Solicitar o ano de nascimento da pessoa
while True:
    try:
        ano_nascimento_str = input("Digite o ano de nascimento (ex: 1990): ").strip()
        ano_nascimento = int(ano_nascimento_str)
        
        # Obter o ano atual automaticamente
        ano_atual = datetime.datetime.now().year

        # Validar o ano de nascimento
        if ano_nascimento <= 0 or ano_nascimento > ano_atual:
            print(f"Ano de nascimento inválido. Por favor, digite um ano entre 1 e {ano_atual}.")
            continue # Pede o ano novamente
        
        break # Sai do loop se o ano for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

# 2. Calcular a idade em anos
idade_em_anos = ano_atual - ano_nascimento

# 3. Transformar a idade em dias (desconsiderando anos bissextos)
# Consideramos que um ano tem 365 dias para simplificar.
idade_em_dias = idade_em_anos * 365

# 4. Exibir o resultado final
print("\n--- Resultado ---")
print(f"Você nasceu em: {ano_nascimento}")
print(f"O ano atual é: {ano_atual}")
print(f"Sua idade aproximada em anos é: {idade_em_anos} anos")
print(f"Sua idade aproximada em dias é: {idade_em_dias} dias")

print("\n--- Cálculo Concluído ---")