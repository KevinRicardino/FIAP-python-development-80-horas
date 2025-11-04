# Dados

# Star Wars - Episódio IV - Uma nova esperança, George Lucas, 1977, 775000000.00

# Criação do dicionário
dicionario = {
    "nome": "Star Wars - Episódio IV - Uma nova esperança",
    "diretor": "George Lucas",
    "ano de lançamento": 1977,
    "bilheteria": 775000000.00
}
print(type(dicionario))

# Exibição do dicionário completo
print(dicionario)

# Exibição do valor de uma chave
print(dicionario["nome"])

# Inserção de uma nova chave e valor (gênero)
dicionario["gênero"] = "Space Opera"
print(dicionario)

# Método keys
print(dicionario.keys())
for chave in dicionario.keys():
    print(chave)

# Método values
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

# Método items
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")

# Método get
print(dicionario.get("público"))
print(dicionario.get("nome"))

# Método setdefault
dicionario.setdefault("público", 1000)
print(dicionario)
dicionario.setdefault("público", 9000) # Não irá funcionar, o setdefault não altera o valor associado a uma chave após ela ser definida.
print(dicionario)