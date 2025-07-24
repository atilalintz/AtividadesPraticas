"""
4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas. 
"""

pares = 0
impares = 0 
totasImpares = []
totosPares = []

while True:
    num = input("Digite um numero inteiro ou 'fim' pra encerrar: ")
    if num.lower() == 'fim':
      break
    try:
      num = int(num)
      if num % 2 == 0:
        pares += 1
        totosPares.append(num)
        print(f"O numero {num} é par")
      else:
        impares += 1
        totasImpares.append(num)
        print(f"O numero {num} é impar")
    except ValueError:
        # Se a conversão para int falhar (por exemplo, digitou texto que não é 'fim'),
        # isso significa que a entrada não é um número inteiro válido.
        print("Erro: A entrada não é um número inteiro válido. Por favor, tente novamente.")

print(f"A quantidade total de numeros pares é {pares}")
print(f"Os numeros pares digitados são {totosPares}")
print(f"A quantidade total de numeros impares é {impares}")
print(f"Os numeros impares digitados são {totasImpares}")    