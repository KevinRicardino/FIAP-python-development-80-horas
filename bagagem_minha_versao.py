"""
Uma companhia aérea permite que seus clientes do tipo premium despachem bagagens de até 32 kg
sem nenhum custo adicional, enquanto os clientes do tipo gold podem levar malas de até 28 kg
sem nenhum custo adicional e os demais devem pagar por qualquer bagagem despachada.
"""
import sys # ← Para poder encerrar o programa usando sys.exit()

# Códigos dos tipos de cliente
premium = "1"
gold = "2"
regular = "3"

print(
    "\n==== Tipos de clientes ===="
    "\n\nPor favor, informe o tipo de cliente entre as seguintes opções:"
    # "\n\nPREMIUM, GOLD OU REGULAR"
    "\n\n\t1 - PREMIUM"
    "\n\t2 - GOLD"
    "\n\t3 - REGULAR"
)

while True:
    tipo_cliente = input("\nSelecione o tipo de cliente entre 1, 2 ou 3 (ou digite 'sair' para finalizar o programa): ")

    if tipo_cliente == premium:
        tipo_cliente_nome = "PREMIUM"
        print(f"\tCliente '{tipo_cliente_nome}' selecionado.")
        break
    elif tipo_cliente == gold:
        tipo_cliente_nome = "GOLD"
        print(f"\tCliente '{tipo_cliente_nome}' selecionado.")
        break
    elif tipo_cliente == regular:
        tipo_cliente_nome = "REGULAR"
        print(f"\tCliente '{tipo_cliente_nome}' selecionado.")
        break
    else:
        if tipo_cliente.lower() == "sair":
            print("\tO programa foi encerrado.")
            sys.exit() # ← Encerra tudo, imediatamente
        # elif tipo_cliente == str:
        elif tipo_cliente.isalpha(): # ← Se o usuário digitar letras
            print("\tLetras não são aceitas. Digite apenas 1, 2 ou 3.")
        else:
            print("\tTente novamente, você precisa selecionar o cliente usando 1, 2 ou 3.")

while True:
    try:
        peso_bagagem = float(input("\nInforme o peso da bagagem que o cliente deseja despachar (em Kg): "))
        if peso_bagagem < 0:
            print("\tPor favor, informe um valor positivo.")
            continue
        break
    except ValueError:
        print("\tValor inválido! Tente novamente Digitando apenas números para o peso da bagagem.")

# Regras por tipo de cliente
if tipo_cliente == premium: # O que acontece se for premium
    if peso_bagagem <= 32: # Exibir mensagem avisando que pode levar a bagagem
        print(f"\n\tCliente '{tipo_cliente_nome}', sua bagagem está dentro do limite permitido!\n\tNão é necessário pagar nenhum valor para despachá-la.")
    else:
        peso_excedente = peso_bagagem - 32 # Exibir mensagem avisando sobre o peso excedente
        print(f"\n\tO cliente '{tipo_cliente_nome}' têm direito a despacharem bagagens de até 32 kg.\n\tA bagagem atual excede este peso em '{peso_excedente}' kg.\n\tAtenção: Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional.")
else:
    if tipo_cliente == gold: # o que acontece se for gold
        if peso_bagagem <= 28: # Exibir mensagem que pode levar a bagagem
            print(f"\n\tCliente '{tipo_cliente_nome}', sua bagagem está dentro do limite permitido!\n\tAtenção: Não é necessário pagar nenhum valor para despachá-la.")
        else:
            peso_excedente = peso_bagagem - 28 # Exibir a mensagem avisando o excedente
            print(f"\n\tO cliente '{tipo_cliente_nome}' têm direito a despacharem bagagens de até 28 kg.\n\tA bagagem atual excede este peso em '{peso_excedente}' kg.\n\tAtenção: Dirija-se ao balcão de cobrança para realizar o pagamento referente ao peso adicional.")
    else: # O que acontece se for regular
        print(f"\n\tO cliente '{tipo_cliente_nome}' não têm direito à bagagem gratuita.\n\tFavor dirigir-se ao balcão de cobranças para realizar o pagamento pela bagagem.")


