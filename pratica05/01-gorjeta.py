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
    valorGorjeta = valorConta * (porcentagemGorjeta / 100)
    return valorGorjeta

# --- Interação com o Usuário ---

print("--- Calculadora de Gorjeta para Restaurantes ---")

# Loop para garantir que o garçom digite um valor de conta válido
while True:
    try:
        # Garçom digita o valor total da conta
        valorContaStr = input("Garçom, digite o valor total da conta sem gorjeta: R$ ").strip()
        valorConta = float(valorContaStr)
        if valorConta < 0:
            print("O valor da conta não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o valor for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o valor da conta.")

# Loop para garantir que o cliente digite uma porcentagem de gorjeta válida
while True:
    try:
        # Cliente digita a porcentagem da gorjeta
        porcentagemGorjetaStr = input("Cliente, digite a porcentagem(%) de gorjeta desejada (ex: 10, 15, 20): ").strip()
        porcentagemGorjeta = float(porcentagemGorjetaStr)
        if porcentagemGorjeta < 0:
            print("A porcentagem da gorjeta não pode ser negativa. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se a porcentagem for válida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a porcentagem da gorjeta.")

# --- Cálculo e Exibição do Resultado ---
# Chama a função para calcular a gorjeta com os valores digitados
gorjetaCalculada = calcular_gorjeta(valorConta, porcentagemGorjeta)
valorTotalComGorjeta = valorConta + gorjetaCalculada

print("\n--- Detalhes da Conta ---")
print(f"Valor da Conta: R$ {valorConta:.2f}")
print(f"Porcentagem da Gorjeta: {porcentagemGorjeta:.0f}%")
print(f"Valor da Gorjeta: R$ {gorjetaCalculada:.2f}")
print(f"Valor Total a Pagar (Conta + Gorjeta): R$ {valorTotalComGorjeta:.2f}")

print("\n--- Operação Concluída Muito Obrigado ---")