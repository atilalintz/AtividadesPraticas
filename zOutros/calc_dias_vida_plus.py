import datetime # Módulo essencial para trabalhar com datas e horas

print("--- Calculadora de Idade Exata (Horário Local) ---")
print("Vamos calcular sua idade em dias, horas e segundos, com base no horário do seu sistema.")

# 1. Solicitar a data e hora de nascimento da pessoa
while True:
    try:
        ano_nascimento_str = input("Digite o ANO de nascimento (ex: 1990): ").strip()
        mes_nascimento_str = input("Digite o MÊS de nascimento (1-12): ").strip()
        dia_nascimento_str = input("Digite o DIA de nascimento (1-31): ").strip()
        hora_nascimento_str = input("Digite a HORA de nascimento (0-23): ").strip()
        minuto_nascimento_str = input("Digite o MINUTO de nascimento (0-59): ").strip()
        segundo_nascimento_str = input("Digite o SEGUNDO de nascimento (0-59): ").strip()

        # Converte as entradas para inteiros
        ano_nascimento = int(ano_nascimento_str)
        mes_nascimento = int(mes_nascimento_str)
        dia_nascimento = int(dia_nascimento_str)
        hora_nascimento = int(hora_nascimento_str)
        minuto_nascimento = int(minuto_nascimento_str)
        segundo_nascimento = int(segundo_nascimento_str)

        # Cria o objeto datetime de nascimento (sem fuso horário explícito)
        data_nascimento = datetime.datetime(
            ano_nascimento, mes_nascimento, dia_nascimento,
            hora_nascimento, minuto_nascimento, segundo_nascimento
        )
        
        # Obtém a data e hora atuais (também sem fuso horário explícito, assume o local)
        data_atual = datetime.datetime.now()

        # Valida se a data de nascimento não está no futuro
        if data_nascimento > data_atual:
            print("Data de nascimento inválida: Você não pode ter nascido no futuro! Tente novamente.")
            continue # Pede as informações novamente
        
        break # Sai do loop se a data e hora forem válidas
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos para ano, mês, dia, hora, minuto e segundo.")
    except Exception as e:
        # Captura outros erros que podem ocorrer ao criar a data (ex: mês 13, dia 32)
        print(f"Erro ao processar a data: {e}. Por favor, verifique os valores e tente novamente.")

# 2. Calcular a diferença de tempo
diferenca_tempo = data_atual - data_nascimento

# 3. Extrair a idade em diferentes unidades de tempo
# Total de dias completos
dias = diferenca_tempo.days

# Segundos restantes após os dias completos (segundos dentro do último dia incompleto)
segundos_restantes_do_dia = diferenca_tempo.seconds

# Calcular horas e segundos a partir dos segundos restantes do dia
horas_restantes = segundos_restantes_do_dia // 3600
minutos_restantes = (segundos_restantes_do_dia % 3600) // 60 # Não exibido no formato final, mas útil para depuração
segundos_finais = segundos_restantes_do_dia % 60


# 4. Exibir o resultado final no formato solicitado
print("\n--- Resultado da Idade Exata ---")
print(f"Sua data de nascimento: {data_nascimento.strftime('%d/%m/%Y %H:%M:%S')} (Horário Local)")
print(f"Data e hora atuais: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} (Horário Local)")
print(f"\nVocê viveu aproximadamente: - {dias:,} dias, {horas_restantes} horas e {segundos_finais} segundos.".replace(",", "."))

print("\n--- Cálculo Concluído ---")