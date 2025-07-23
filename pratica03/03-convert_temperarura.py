"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

tempDigitada = float(input("Informe a temperatura:"))

print("informe a unidade de origem:")
unidadeOrigem = input("digite C para Celsius, F para Fahrenheit ou K para Kelvin:")
print("Informe qual a unidade de destino:")
unidadeDestino = input("digite C para Celsius, F para Fahrenheit ou K para Kelvin:") 

temperatura = tempDigitada

if unidadeOrigem == "C" and unidadeDestino == "F":
    temperatura = (temperatura * 9/5) + 32
    print(f"A temperatura {tempDigitada} em Celsius equivale a {temperatura} em Fahrenheit:")
elif unidadeOrigem == "C" and unidadeDestino == "K":
    temperatura = temperatura + 273.15
    print(f"A temperatura {tempDigitada} em Celsius equivale a {temperatura} em Kelvin:")
elif unidadeOrigem == "F" and unidadeDestino == "C":
    temperatura = (temperatura - 32) * 5/9
    print(f"A temperatura {tempDigitada} em Fahrenheit equivale a {temperatura} em Celsius:")
elif unidadeOrigem == "F" and unidadeDestino == "K":
    temperatura = (temperatura - 32) * 5/9 + 273.15
    print(f"A temperatura {tempDigitada} em Fahrenheit equivale a {temperatura} em Kelvin:")
elif unidadeOrigem == "K" and unidadeDestino == "C":
    temperatura = temperatura - 273.15
    print(f"A temperatura {tempDigitada} em Kelvin equivale a {temperatura} em Celsius:")
elif unidadeOrigem == "K" and unidadeDestino == "F":
    temperatura = (temperatura - 273.15) * 9/5 + 32
    print(f"A temperatura {tempDigitada} em Kelvin equivale a {temperatura} em Fahrenheit:")
