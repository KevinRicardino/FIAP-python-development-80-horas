print("\n==== Quilão do André ====\n")

preco_quilo = float(input("Informe o valor cobrado por quilo: "))
peso_prato = float(input("Informe o peso do prato do cliente (em Kg): "))

preco_prato = preco_quilo * peso_prato

# print("\n\tO valor do prato é R${:.2f}".format(preco_prato))
print(f"\tO valor do prato é R${preco_prato:.2f}")


if peso_prato > 1:
    print(
        "\nComo o peso do prato do cliente ultrapassou 1Kg, ele deve pagar apenas o valor fixo de:"
        "\n\tR$ 80,00."
    )
    print("\nComo o peso do prato do cliente ultrapassou 1Kg, ele deve pagar apenas o valor fixo de R$ 80,00.")