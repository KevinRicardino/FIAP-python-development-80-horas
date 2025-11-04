op = 0
ficha = {}

while op != 4:
    print("\n")
    print("=" * 70)
    print("FICHA CADASTRAL".center(70))
    print("=" * 70)
    print("\t[1] - Incluir informações na ficha")
    print("\t[2] - Recuperar informação da ficha")
    print("\t[3] - Exibir a ficha completa")
    print("\t[4] - Sair")
    print("=" * 70)

    try:
        op = int(input("→ Informe a opção desejada: "))
    except ValueError:
        print("\n⚠️ Entrada inválida! Digite apenas números inteiros.")
        input("\nPressione ENTER para tentar novamente...")
        continue

    if op == 1:
        # Inserir dados na ficha
        chave = input("\nInforme o campo que deseja cadastrar na ficha: ")
        valor = input("Informe o dado que deseja cadastrar neste campo: ")
        #ficha[chave] = valor → Este é o modo direto de se fazer isso, mas é recomendável a sempre se usar o metodo por ele já contar com maior segurança
        ficha.update({chave:valor})

    elif op == 2:
        # Recuperar dados da ficha
        print(f"\nCampos disponíveis na ficha: \n")
        for campo in ficha.keys():
            print(f"\t| {campo}")

        chave = input("\nInforme qual campo deseja exibir: ").strip()

        if chave in ficha.keys():
            print(f"\nO campo '{chave}' contém o dado '{ficha.get(chave)}'.")
        else:
            print("\n⚠️ Campo inexistente! Verifique o nome e tente novamente.")
        #----------------------------------------------------
        #print(ficha.get(chave))
        #----------------------------------------------------
        #if chave in ficha.keys():
        #    print(ficha[chave])
        #else:
        #    print("Você digitou um campo inexistente.")

    elif op == 3:
        # Exibir ficha completa
        print("\nFICHA CADASTRAL:\n")
        for campo, dado in ficha.items():
            print(f"\t| {campo.upper()} → {dado.upper()}")

    elif op == 4:
        print("\nSaindo do sistema de ficha cadastral...")
        break