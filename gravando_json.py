import json
dicionario = {
    "nome": "Python",
    "missão": "Ser incrível!"
}

#print(json.dumps(dicionario, indent=4))
#print(json.dumps(dicionario, ensure_ascii=False))
conteudo = json.dumps(dicionario, ensure_ascii=False, indent=4)
with open("arquivo.json", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(conteudo)

print("Arquivo gerado corretamente!")

#json → Javascript Object Notation, esse metodo parecido com dicionários no python.
#.dumps → Significa que vamos usar uma função que joga ou despeja alguma coisa para o formato string, neste caso o dicionário.
#ensure_ascii=False → Garante que os acentos do Português irão permanecer corretos.
#indent=4 → Diz ao texto final para ter indentação de 4 espaços
