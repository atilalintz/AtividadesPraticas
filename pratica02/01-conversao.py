"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

reais = 100.00
dolar = 5.20
euro = 6.15

conver_dolar = reais / dolar
conver_euro = reais / euro

print(f"Conversão de R$100,00 Reais para Dólar da ${conver_dolar:.2f}")
print(f"Conversão de R$100,00 Reais para Euro da ${conver_euro:.2f}")

