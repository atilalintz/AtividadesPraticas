import datetime # Módulo para conseguir o ano atual automaticamente

print("--- Calculadora de Idade em Dias ---")

# 1. Solicitar o ano de nascimento da pessoa
while True:
    try:
        anoNascimentoStr = input("Digite o ano de nascimento (ex: 1990): ").strip()
        anoNascimento = int(anoNascimentoStr)
        
        # Obter o ano atual automaticamente
        anoAtual = datetime.datetime.now().year

        # Validar o ano de nascimento
        if anoNascimento <= 0 or anoNascimento > anoAtual:
            print(f"Ano de nascimento inválido. Por favor, digite um ano entre 1 e {anoAtual}.")
            continue # Pede o ano novamente
        
        break # Sai do loop se o ano for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

# 2. Calcular a idade em anos
idadeAnos = anoAtual - anoNascimento

# 3. Transformar a idade em dias (desconsiderando anos bissextos)
# Consideramos que um ano tem 365 dias para simplificar.
idadeDias = idadeAnos * 365

# 4. Exibir o resultado final
print("\n--- Resultado ---")
print(f"Você nasceu em: {anoNascimento}")
print(f"O ano atual é: {anoAtual}")
print(f"Sua idade aproximada em anos é: {idadeAnos} anos")
print(f"Sua idade aproximada em dias é: {idadeDias} dias")

print("\n--- Cálculo Concluído ---")