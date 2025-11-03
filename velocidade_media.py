print("==== Simulador de computador de bordo====\n")
distancia = float(input("Por favor, informe a distância percorrida (em km): "))
tempo = float(input("Por favor, informe o tempo da viagem (em horas): "))

velocidade_media = distancia / tempo

print("\nA velocidade média é de {:.2f} km/h.".format(velocidade_media))
print(f"A velocidade média é de {velocidade_media:.2f} km/h.")