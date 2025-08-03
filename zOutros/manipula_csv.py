import csv

with open("zOutros/arquivo.csv", "w", encoding="utf-8" ) as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Átila", 51, "Andrelândia"]) # Escrever o cabeçalho
        
"""with open("zOutros/arquivo.csv", "r", encoding="utf-8" ) as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)  # Exibir cada linha do arquivo CSV"""
        
"""

arquivo = open("zOutros/arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close
#arquivo = open("zOutros/arquivo.txt", "r") # Abrir o arquivo em modo leitura
#conteudo = arquivo.read()  # Ler todo o conteúdo do arquivo
#conteudo = arquivo.readline()  # Ler o conteúdo do arquivo linha por linha
#conteudo = arquivo.readlines()  # Ler o conteúdo do arquivo como uma lista de linhas
#print(" Exibir o conteúdo lido:", conteudo)
arquivo.write("Escrevendo no arquivo\n")  # Escrever no arquivo
arquivo.writelines("Escrevendo várias linhas\n")  # Escrever várias linhas no arquivo
"""