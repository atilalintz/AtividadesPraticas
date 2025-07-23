"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).
"""
num = int(input("Informe sua idade:"))

if num <= 11:
    print(f"Você é uma criança.")
elif  num <= 17:
    print(f"Você é Adolecente.")
elif  num <= 59:
    print(f"Você é maior de idade!.")
elif  num <= 99:
    print(f"Você é Idoso.")
else:
    print(f"Você é uma lenda viva!")