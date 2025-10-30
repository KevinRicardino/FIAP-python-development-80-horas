#NOME
#PESO
#ALTURA
#IDADE
#TEM PESO MÍNIMO PARA DOAR
#TEM IDADE MÍNIMA PARA DOAR

from datetime import date

print("\n==== Cadastro de doadores de sangue ====\n")
nome = input("Por favor, informe o seu nome completo: ")
peso = float(input("Por favor, informe o seu peso em Kg: "))
altura = int(input("Por favor, informe a sua altura em cm: "))
ano_nascimento = int(input("Por favor, informe seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16

texto_saida = f"\n\tNOME: {nome}\n\tPESO: {peso} Kg\n\tALTURA {altura} cm\n\tIDADE: {idade}\n\tTEM PESO MÍNIMO PARA DOAR: {tem_peso_minimo}\n\tTEM IDADE MÍNIMA PARA DOAR: {tem_idade_minima}."

print(texto_saida)