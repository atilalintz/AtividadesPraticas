print("--- Calculadora de Desconto ---")

# Solicita o preço original do produto
while True:
    try:
        precoOriginalStr = input("Digite o preço original do produto: R$ ").strip()
        precoOriginal = float(precoOriginalStr)
        if precoOriginal < 0:
            print("O preço não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o preço for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o preço.")

# Solicita o percentual de desconto desejado
while True:
    try:
        percentualDescontoStr = input("Digite o percentual de desconto desejado (ex: 10 para 10%): ").strip()
        percentualDesconto = float(percentualDescontoStr)
        if percentualDesconto < 0:
            print("O percentual de desconto não pode ser negativo. Por favor, digite um valor válido.")
            continue
        break # Sai do loop se o percentual for válido
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o percentual de desconto.")

# Calcula o preço final com desconto
# Primeiro, calcula o valor do desconto em si
valorDesconto = precoOriginal * (percentualDesconto / 100)

# Depois, subtrai o valor do desconto do preço original para encontrar o preço final
precoFinal = precoOriginal - valorDesconto

# Exibe o preço final arredondado para duas casas decimais
print("\n--- Resultado do Desconto ---")
print(f"Preço Original: R$ {precoOriginal:.2f}")
print(f"Percentual de Desconto: {percentualDesconto:.0f}%")
print(f"Valor do Desconto: R$ {valorDesconto:.2f}")
print(f"Preço Final com Desconto: R$ {precoFinal:.2f}")

print("\n--- Cálculo Concluído ---")