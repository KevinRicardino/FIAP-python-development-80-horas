def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida="km/h"):
    # Código da nossa função
    velocidade_media = distancia / tempo
    # Exibir o resultado
    print(f"A velocidade média é {velocidade_media:.2f} {unidade_medida}")

# Solicitar distância e tempo
#distancia_digitada = float(input("Digite a distância percorrida: "))
#tempo_digitado = float(input("Digite o tempo da viagem: "))
calcular_velocidade_media(200, 3)