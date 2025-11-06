def exibe_promocao(*clientes):
    for cliente in clientes:
        print(f"Olá {cliente}!\nQueremos te avisar que a nova X-WING está em promoção!")

lista_clientes = ["Luke", "Princesa Leia", "Mestre Yoda"]
exibe_promocao(*lista_clientes)
#exibe_promocao("Princesa Leia")
#exibe_promocao("Mestre Yoda")