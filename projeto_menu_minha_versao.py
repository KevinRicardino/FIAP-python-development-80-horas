opcao = 0

while opcao != 3:
    print("=" * 75)
    print("CALCULO FATORIAL".center(75))
    print("=" * 75)
    print("\t[1] - Receber um elogio")
    print("\t[2] - Calcular o fatorial")
    print("\t[3] - Sair")
    print("=" * 75)

    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("\n→ Valor inválido!")
        opcao = 0 # Define um valor inválido para não quebrar o loop

    if opcao == 1:
        print("→ Você é uma pessoa muito inteligente!")
    elif opcao == 2:
        try:
            numero = int(input("Por favor, informe o numero do qual deseja o fatorial: "))
        except ValueError:
            print("→ Número inválido!")
            continue # Volta para o menu
        fat = numero
        for valor in range(1, numero, 1):
            fat = fat * valor
        print(f"→ O fatorial para o valor informado foi {fat}")
    elif opcao == 3:
        print("→ Saindo do sistema...")
    else:
        print("Escolha uma opção do menu.")