inimigos = [(50, 30), (10, 10), (10, 90), (30, 25)]

print("=" * 68)
print(f"ＢＡＴＡＬＨＡ ＮＡＶＡＬ".center(60))
print("=" * 68)

while True:
    # Se não houver mais inimigos, o jogo termina imediatamente
    if not inimigos:
        print("\n🏆 Parabéns! Você derrotou todos os inimigos!")
        break

    for x, y in inimigos:
        print(f"\t→\tA posição é X={x} e Y={y}")
    print("=" * 68)

    try:
        x = int(input("Informe a posição X que deseja arriscar: "))
        y = int(input("Informe a posição Y que deseja arriscar: "))
    except ValueError:
        print("\n⚠️  Entrada inválida! Digite apenas números inteiros.")
        input("\nPressione qualquer tecla para tentar novamente...")
        continue

    if (x, y) in inimigos:
        inimigos.remove((x, y))
        print("\n\t✅ Você acertou um inimigo!\n")
    else:
        print("\n\t❌ Água! Você errou!\n")

    input("Pressione qualquer tecla para continuar...")

