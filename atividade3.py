login = input("Digite seu login: ")
senha = input("Digite a senha: ")

if (login == "procopio" and senha == "12345") or \
   (login == "paiva" and senha == "54321"):
    print("Seja bem-vindo!")
else:
    print("Usuário e senha não conferem!") 