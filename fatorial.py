numero = int(input("Por favor, informe o número do qual deseja o fatorial: "))
fat = numero

for valor in range(1, numero, 1):
    fat = fat * valor

print(f"\nO fatorial para o valor informado foi {fat}.")