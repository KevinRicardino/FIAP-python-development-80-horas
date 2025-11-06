with open("arquivo_texto.txt", mode="r", encoding="UTF-8") as arquivo:
    #conteudo = arquivo.read()
    #conteudo = arquivo.readlines()
    conteudo = arquivo.read().splitlines()

#with open → Com o arquivo aberto.
#arquivo_texto.txt → Nome do arquivo.
#mode="r" → Modo leitura, ou seja, modo de visualização do arquivo.
#encoding="UTF-8" → É a codificação escolhida para os caractéres que serão usados no arquivo.
#as arquivo → É o objeto que representa o arquivo.

print(conteudo)