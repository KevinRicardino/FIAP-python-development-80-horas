"""
Uma loja oferece pagamentos por boleto bancário ou por cartão de crédito.
Os clientes que pagam por boleto têm direito a 5% de desconto sobre
o valor da compra, enquanto os clientes que pagam por cartão de
crédito podem escolher parcelar a compra em até 12x.
"""

print("\n==== Saldão da alegria! ====\n")

total_compra = float(input("Por favor, informe o valor total da compra do cliente: "))
forma_pagamento = int(input(
    "Por favor, selecione a forma de pagamento:"
    "\n\n\t1 - Boleto"
    "\n\t2 - Cartão"
    "\n\nInsira aqui o método escolhido: "
))

if forma_pagamento == 1:
    # desconto
    total_compra_desconto = total_compra * 0.95
    # print(f"\nO total da compra de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto. \nO cliente deverá pagar R${total_compra_desconto:.2f}.")
    print(
        f"\nO total da compra de R${total_compra:.2f} sofreu um desconto pelo pagamento em boleto."
        f"\nO cliente deverá pagar R${total_compra_desconto:.2f}."
    )
else:
    # parcelamento
    parcelas = int(input("\nInforme o número de parcelas desejadas: "))
    valor_parcela = total_compra / parcelas
    print(f"\nO total da compra de R${total_compra:.2f} será pago em {parcelas} parcelas de R${valor_parcela:.2f}.")