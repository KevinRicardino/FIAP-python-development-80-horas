print("==== Boas vindas ao calculador de inteiros ====\n")
primeiro_valor = int(input("Por favor, informe o primeiro valor: "))
print(f"Tipo do primeiro valor: {type(primeiro_valor).__name__}")
segundo_valor = int(input("Por favor, informe o segundo valor: "))
print(f"Tipo do segundo valor: {type(segundo_valor).__name__}")

soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
divisao = primeiro_valor / segundo_valor
multiplicacao = primeiro_valor * segundo_valor

print("\n==== Resultados das operações ====")
# print("\nO resultado da soma foi: {}".format(soma))
# print(f"\nO resultado da soma foi: {soma}")
print(
    f"\nO resultado da soma foi: {soma}"
    f"\nO resultado da subtração foi: {subtracao}"
    f"\nO resultado da divisão foi: {divisao:.2f}"
    f"\nO resultado da multiplicação foi: {multiplicacao}"
)
