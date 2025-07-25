def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
    float: O valor da gorjeta calculada.
    """
    # Para calcular a gorjeta, multiplicamos o valor da conta pela porcentagem
    # e dividimos por 100 para converter a porcentagem em decimal.
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

# --- Interação com o Usuário ---

print("--- Calculadora de Gorjeta para Restaurantes ---")

# Loop para garantir que o garçom digite um valor de conta válido
while True:
    try:
        # Garçom digita o valor total da conta
        valor_conta_str = input("Garçom, digite o valor total da conta sem gorjeta: R$ ").strip()
        valor_conta = float(valor_conta_str)
        if valor_conta < 0:
            print("O valor da conta não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o valor for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o valor da conta.")

# Loop para garantir que o cliente digite uma porcentagem de gorjeta válida
while True:
    try:
        # Cliente digita a porcentagem da gorjeta
        porcentagem_gorjeta_str = input("Cliente, digite a porcentagem(%) de gorjeta desejada (ex: 10, 15, 20): ").strip()
        porcentagem_gorjeta = float(porcentagem_gorjeta_str)
        if porcentagem_gorjeta < 0:
            print("A porcentagem da gorjeta não pode ser negativa. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se a porcentagem for válida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a porcentagem da gorjeta.")

# --- Cálculo e Exibição do Resultado ---
# Chama a função para calcular a gorjeta com os valores digitados
gorjeta_calculada = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
valor_total_com_gorjeta = valor_conta + gorjeta_calculada

print("\n--- Detalhes da Conta ---")
print(f"Valor da Conta: R$ {valor_conta:.2f}")
print(f"Porcentagem da Gorjeta: {porcentagem_gorjeta:.0f}%")
print(f"Valor da Gorjeta: R$ {gorjeta_calculada:.2f}")
print(f"Valor Total a Pagar (Conta + Gorjeta): R$ {valor_total_com_gorjeta:.2f}")

print("\n--- Operação Concluída ---")