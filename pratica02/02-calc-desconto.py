"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

preco_desconto = preco_original * (1 - porcentagem_desconto / 100)
preco_final = preco_original - preco_desconto

print("O nome do produto é:........", nome_produto,)
print(f"O preço original é:........R${preco_original:.2f}")
print("A porcentagem de desconto é:", porcentagem_desconto, "%")
print(f"O valor do desconto é:.....R${preco_desconto:.2f}")
print(f"O preço final da compra é: R${preco_final:.2f}") 
