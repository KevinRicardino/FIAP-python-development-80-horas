texto = "Este texto quebra de linha \naqui. Porém aqui temos uma \ttabulação"
print(texto)

texto = "texto em minúsculas AINDA É texto"
print(texto.capitalize())
print(texto.title())
print(texto.upper())
print(texto.lower())
print(texto.startswith("Tex")) # Irá retornar False por ser → case sensitive
print(texto.endswith("o")) # Irá retornar True
print(texto.count("m"))
print("em" in texto)
print(texto.replace("AINDA", "com certeza"))
print(texto)