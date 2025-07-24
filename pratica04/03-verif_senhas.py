"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  
"""

import re # Módulo para usar expressões regulares (útil para verificar números)

while True:
    senha = input("Digite a senha com no minimo 8 caracteres e um numero: ou 'sair' para encerrar): ").strip()

    if senha.lower() == 'sair':
        print("Saindo do verificador de senhas. Até mais!")
        break # Encerra o programa se o usuário digitar 'sair'

    # --- Critérios de Força da Senha ---
    tem_oito_caracteres = len(senha) >= 8
    tem_numero = bool(re.search(r'\d', senha)) # Verifica se há pelo menos um dígito na senha

    # --- Avaliação da Senha ---
    if tem_oito_caracteres and tem_numero:
        print("\n--- Senha FORTE! ---")
        print("Sua senha atende aos critérios de segurança.")
        break # Encerra o programa porque uma senha forte foi criada
    else:
        print("\n--- Senha FRACA! ---")
        print("Para ser considerada forte, sua senha precisa de:")
        if not tem_oito_caracteres:
            print("  - Pelo menos 8 caracteres.")
        if not tem_numero:
            print("  - Pelo menos um número.")
        print("Por favor, tente outra senha.")
        # O loop continua automaticamente para pedir uma nova senha
