# ===============================================
#                 TELA DE LOGIN
# ===============================================

print("=" * 75)
print("TELA DE LOGIN".center(75))
print("=" * 75)

while True:
    usuario = input("\nUsuário (ou 'sair' para encerrar): ").strip()
    if usuario.lower() == 'sair':
        print("\nEncerrando o sistema...")
        break

    senha = input("Senha (ou 'sair' para encerrar): ").strip()
    if senha.lower() == 'sair':
        print("\nEncerrando o sistema...")
        break

    # Validação de acesso
    if usuario.upper() == "ADMIN" and senha == "123":
        print("\n✅ Acesso autorizado! Bem-vindo, ADMIN.")
        break
    else:
        print("\n❌ Usuário ou senha incorretos. Tente novamente.")
