"""
1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
"""
while True: # Loop principal para continuar pedindo entradas até que uma operação válida seja concluída com sucesso
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        # Se a entrada para qualquer um dos números não for um valor numérico válido,
        # exibe uma mensagem de erro e reinicia o loop 'while True'.
        print("Entrada inválida. Por favor, digite números válidos.")
        continue # Volta para o início do loop para pedir os números novamente

    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao not in ["+", "-", "*", "/"]:
        # Se a operação digitada não for uma das válidas,
        # exibe uma mensagem de erro e reinicia o loop 'while True'.
        print("Operação inválida. Por favor, digite uma operação válida.")
        continue # Volta para o início do loop para pedir os números e a operação novamente

    resultado = None # Inicializa a variável 'resultado' como None

    try:
        # Realiza a operação escolhida.
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            # Aqui é onde um ZeroDivisionError pode ocorrer se 'num2' for 0.
            # O bloco 'try' vai tentar fazer a divisão, e se 'num2' for 0,
            # o 'except ZeroDivisionError' irá capturar o erro.
            resultado = num1 / num2
        
        # Se chegamos a este ponto, a operação foi realizada com sucesso
        # (incluindo a divisão, sem erro de divisão por zero).
        print("---")
        print(f"O resultado de {num1} {operacao} {num2} é = {resultado}")
        print("---")
        break # Sai do loop 'while True', pois a operação foi um sucesso e o programa pode terminar.

    except ZeroDivisionError:
        # Captura especificamente o erro de divisão por zero.
        # Exibe uma mensagem de erro apropriada e reinicia o loop 'while True',
        # obrigando o usuário a tentar novamente.
        print("Erro: Não é possível dividir por zero. Por favor, tente novamente.")
        continue # Volta para o início do loop para pedir todas as entradas novamente