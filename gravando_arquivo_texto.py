texto_para_gravar = "Este texto será gravado!"

with open("arquivo_texto.txt", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(texto_para_gravar)

#with open → Com o arquivo aberto.
#arquivo_texto.txt → Nome do arquivo.
#mode="w" → Modo escrita, ou seja, modo de edição do arquivo.
#encoding="UTF-8" → É a codificação escolhida para os caractéres que serão usados no arquivo.
#as arquivo → É o objeto que representa o arquivo.

print("O arquivo foi gravado.")