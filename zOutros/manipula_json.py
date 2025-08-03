import json

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo", "profissão": ["Engenheiro", "Professor"]}
""" 
with open("arquivo.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
"""
with open("arquivo.json", "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)  # Exibir o conteúdo lido do arquivo JSON