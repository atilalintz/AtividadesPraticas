def calcular_valor_base_e_gorjeta(valor_total: float, porcentagem: float) -> tuple[float, float]:
    """
    Calcula o valor da gorjeta e o valor base (sem gorjeta) a partir de um total e uma porcentagem.

    Parâmetros:
    valor_total (float): O valor total que inclui a gorjeta.
    porcentagem (float): A porcentagem da gorjeta (ex: 10 para 10%).

    Retorna:
    tuple[float, float]: Uma tupla contendo (valor_da_gorjeta, valor_base_sem_gorjeta).
    """
    # Se o total_com_gorjeta é 110% (100% da conta + 10% de gorjeta),
    # então a conta original é (valor_total / (100 + porcentagem)) * 100
    fator_conversao = 1 + (porcentagem / 100)
    valor_base_sem_gorjeta = valor_total / fator_conversao
    valor_da_gorjeta = valor_total - valor_base_sem_gorjeta
    return valor_da_gorjeta, valor_base_sem_gorjeta

def calcular_gorjeta_adicional(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta a ser adicionada a uma conta.

    Parâmetros:
    valor_conta (float): O valor total da conta sem gorjeta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta a ser adicionada (ex: 15 para 15%).

    Retorna:
    float: O valor da gorjeta calculada.
    """
    return valor_conta * (porcentagem_gorjeta / 100)

# --- Início do Programa ---

print("--- Calculadora de Gorjeta Avançada para Restaurantes ---")

# 1. Garçom informa o valor total da conta
while True:
    try:
        valor_conta_str = input("Garçom, digite o valor total da conta: R$ ").strip()
        valor_conta = float(valor_conta_str)
        if valor_conta < 0:
            print("O valor da conta não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o valor for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o valor da conta.")

# 2. Pergunta se a gorjeta já está embutida
while True:
    gorjeta_embutida_str = input("A gorjeta já está embutida nesse valor? (sim/não): ").strip().lower()
    if gorjeta_embutida_str in ['sim', 'não', 'nao']:
        break
    else:
        print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

# --- Lógica de Cálculo ---

if gorjeta_embutida_str == 'sim':
    # Cenário: Gorjeta já embutida
    print("\n--- Gorjeta Embutida Detectada ---")
    while True:
        try:
            porcentagem_embutida_str = input("Quantos por cento é a gorjeta embutida no valor total? (ex: 10, 15): ").strip()
            porcentagem_embutida = float(porcentagem_embutida_str)
            if porcentagem_embutida < 0:
                print("A porcentagem não pode ser negativa. Digite um valor válido.")
                continue
            # Evita divisão por zero ou valor irreal caso a porcentagem seja -100%
            if porcentagem_embutida <= -100:
                print("A porcentagem de gorjeta embutida não pode ser menor ou igual a -100%. Digite um valor válido.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a porcentagem.")

    # Calcula o valor da gorjeta e o valor original da conta
    valor_da_gorjeta_embutida, valor_conta_sem_gorjeta = calcular_valor_base_e_gorjeta(valor_conta, porcentagem_embutida)

    print("\n--- Detalhes da Conta (Gorjeta Embutida) ---")
    print(f"Valor Total Original da Conta (com gorjeta): R$ {valor_conta:.2f}")
    print(f"Porcentagem da Gorjeta Embutida: {porcentagem_embutida:.0f}%")
    print(f"Valor da Gorjeta Embutida: R$ {valor_da_gorjeta_embutida:.2f}")
    print(f"Valor da Conta SEM Gorjeta: R$ {valor_conta_sem_gorjeta:.2f}")

else: # gorjeta_embutida_str == 'não' ou 'nao'
    # Cenário: Gorjeta não embutida (segue o fluxo anterior)
    print("\n--- Cálculo de Gorjeta Adicional ---")
    while True:
        try:
            porcentagem_gorjeta_str = input("Cliente, digite a porcentagem de gorjeta desejada (ex: 10, 15, 20): ").strip()
            porcentagem_gorjeta = float(porcentagem_gorjeta_str)
            if porcentagem_gorjeta < 0:
                print("A porcentagem da gorjeta não pode ser negativa. Por favor, digite um valor válido.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a porcentagem da gorjeta.")

    # Calcula a gorjeta a ser adicionada
    gorjeta_calculada = calcular_gorjeta_adicional(valor_conta, porcentagem_gorjeta)
    valor_total_com_gorjeta = valor_conta + gorjeta_calculada

    print("\n--- Detalhes da Conta (Gorjeta Adicional) ---")
    print(f"Valor da Conta (sem gorjeta): R$ {valor_conta:.2f}")
    print(f"Porcentagem da Gorjeta Desejada: {porcentagem_gorjeta:.0f}%")
    print(f"Valor da Gorjeta Calculada: R$ {gorjeta_calculada:.2f}")
    print(f"Valor Total a Pagar (Conta + Gorjeta): R$ {valor_total_com_gorjeta:.2f}")

print("\n--- Operação Concluída ---")