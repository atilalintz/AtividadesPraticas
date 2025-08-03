with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close
#arquivo = open("zOutros/arquivo.txt", "r") # Abrir o arquivo em modo leitura
#conteudo = arquivo.read()  # Ler todo o conteúdo do arquivo
#conteudo = arquivo.readline()  # Ler o conteúdo do arquivo linha por linha
#conteudo = arquivo.readlines()  # Ler o conteúdo do arquivo como uma lista de linhas
#print(" Exibir o conteúdo lido:", conteudo)
#arquivo.write("Escrevendo no arquivo\n")  # Escrever no arquivo
#arquivo.writelines("Escrevendo várias linhas\n")  # Escrever várias linhas no arquivo