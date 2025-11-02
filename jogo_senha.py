resposta = ""
tentativa = 0

while resposta != "python":
    resposta = input("\nDigite a senha secreta: ")
    tentativa = tentativa + 1
    print(f"Quantidade de tentativas: {tentativa}")

print("A senha correta foi digitada!")
print(f"\nFoi preciso usar {tentativa} tentativas para o acerto.")