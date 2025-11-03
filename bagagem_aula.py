"""
Uma companhia aérea permite que seus clientes do tipo premium despachem bagagens de até 32 kg
sem nenhum custo adicional, enquanto os clientes do tipo gold podem levar malas de até 28 kg
sem nenhum custo adicional e os demais devem pagar por qualquer bagagem despachada.
"""

tipo_cliente = input("Por favor, informe o tipo do cliente: PREMIUM, GOLD ou REGULAR ")
peso_bagagem = float(input("Informe o peso da bagagem que o cliente deseja despachar "))

if tipo_cliente.upper() == "PREMIUM":
    # O que acontece se for Premium
    if peso_bagagem <= 32:
        # Exibir mensagem avisando que pode levar a bagagem
        print(f"\n\tCliente {tipo_cliente}, sua bagagem está dentro do limite permitido!\n\tNão é necessário pagar "
              f"nenhum valor para despachá-la.")

    else:
        peso_excedente = peso_bagagem - 32
        # Exibir mensagem avisando sobre o peso excedente
        print(f"\n\t→ O cliente {tipo_cliente} têm direito a despacharem bagagens de até 32 kg.\n\tA bagagem atual "
              f"excede este peso em {peso_excedente} kg.\n\tDirija-se ao balcão de cobrança para realizar o pagamento "
              f"referente ao peso adicional.")
elif tipo_cliente.upper() == "GOLD":
    # O que acontece se for Gold
    if peso_bagagem <= 28:
        # Exibir a mensagem avisando que pode levar a bagagem
        print(f"\n\tCliente {tipo_cliente}, sua bagagem está dentro do limite permitido!\n\tNão é necessário pagar "
              f"nenhum valor para despachá-la.")
    else:
        peso_excedente = peso_bagagem - 28
        # Exibir a mensagem avisando sobre o excedente
        print(f"\n\tOs clientes {tipo_cliente} tem direito a despacharem bagagens de até 28 kg.\n\tA bagagem atual "
              f"excede este peso em {peso_excedente} kg.\n\tDirija-se ao balcão de cobrança para realizar o "
              f"pagamento referente ao peso adicional.")
else:
    # O que acontece se for Regular
    print(f"\n\tOs cliente {tipo_cliente + "es"} não tem direito à bagagem gratuita.\n\tFavor dirigir-se ao balcão "
          f"de cobranças para realizar o pagamento pela bagagem.")
