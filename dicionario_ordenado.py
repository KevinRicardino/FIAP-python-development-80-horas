# Importação do OrderedDict
from collections import OrderedDict

# Criação
dicionario_ordenado = OrderedDict()
print(dicionario_ordenado)

# Adicionando chaves e valores
dicionario_ordenado["NOME"] = "Iphone"
dicionario_ordenado["MARCA"] = "Apple"
dicionario_ordenado["MODELO"] = "14 PRO MAX"

# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

# Alterando um item
dicionario_ordenado["MARCA"] = "Maça"
print()

# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

# Removendo um item
dicionario_ordenado.pop("MARCA")
print()

# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")

# Reinserindo um item neste dicionário
dicionario_ordenado["MARCA"] = "Apple"
print()

# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f"{chave} -- {valor}")