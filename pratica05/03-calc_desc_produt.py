print("--- Calculadora de Desconto ---")

# Solicita o preço original do produto
while True:
    try:
        preco_original_str = input("Digite o preço original do produto: R$ ").strip()
        preco_original = float(preco_original_str)
        if preco_original < 0:
            print("O preço não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o preço for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o preço.")

# Solicita o percentual de desconto desejado
while True:
    try:
        percentual_desconto_str = input("Digite o percentual de desconto desejado (ex: 10 para 10%): ").strip()
        percentual_desconto = float(percentual_desconto_str)
        if percentual_desconto < 0:
            print("O percentual de desconto não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o percentual for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o percentual de desconto.")

# Calcula o preço final com desconto
# Primeiro, calcula o valor do desconto em si
valor_do_desconto = preco_original * (percentual_desconto / 100)

# Depois, subtrai o valor do desconto do preço original para encontrar o preço final
preco_final = preco_original - valor_do_desconto

# Exibe o preço final arredondado para duas casas decimais
print("\n--- Resultado do Desconto ---")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Percentual de Desconto: {percentual_desconto:.0f}%")
print(f"Valor do Desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")

print("\n--- Cálculo Concluído ---")