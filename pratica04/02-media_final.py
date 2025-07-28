"""
2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.  
"""
notas = []  # Aqui vamos guardar todas as notas válidas que você digitar

print("--- Sistema de Registro de Notas da Turma ---")
print("Por favor, digite as notas dos alunos (entre 0 e 10).")
print("Para parar e ver a média, digite 'fim'.")

while True:
    # Solicita a entrada da nota e já a prepara (remove espaços e converte para minúsculas)
    entradaUsuario = input("Digite a nota (ou 'fim'): ").strip().lower()

    if entradaUsuario == 'fim':
        break  # Se o usuário digitar 'fim', saímos do loop de entrada de notas

    try:
        # Tenta converter a entrada para um número decimal (float)
        nota = float(entradaUsuario)
        
        # Verifica se a nota está dentro do intervalo permitido (0 a 10)
        if 0 <= nota <= 10:
            notas.append(nota)  # Se a nota for válida, adiciona ela à lista
            print(f"Nota {nota:.2f} registrada com sucesso.")
        else:
            # Se a nota estiver fora do intervalo, avisa o usuário
            print("Erro: A nota deve ser entre 0 e 10. Por favor, tente novamente.")
    except ValueError:
        # Se a entrada não for um número nem 'fim', avisa sobre a entrada inválida
        print("Erro: Entrada inválida. Por favor, digite um número ou 'fim'.")

"""
 Resultados Finais

Agora, vamos ver a média da turma e quantas notas válidas foram registradas.
"""
print("\n--- Relatório da Turma ---")

if notas:  # Verifica se a lista de notas não está vazia
    totalNotasValidas = len(notas)  # Conta quantas notas válidas foram registradas
    somaNotas = sum(notas)      # Soma todas as notas válidas
    
    mediaFinal = somaNotas / totalNotasValidas  # Calcula a média
    
    print(f"Total de notas válidas registradas: {totalNotasValidas}")
    # Exibe a média com duas casas decimais
    print(f"Média final da turma: {mediaFinal:.2f}") 
else:
    # Se nenhuma nota foi registrada, informa o usuário
    print("Nenhuma nota válida foi registrada para calcular a média.")

print("--- Fim do Programa ---")