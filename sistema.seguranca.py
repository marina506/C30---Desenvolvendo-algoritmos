# Sistema de Segurança com Múltiplas Condições 

def verificar_acesso():
    tentativas = 0

    while tentativas < 3:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")

        if usuario == "admin" and senha == "1234":
            print("Acesso total")
            return
        elif usuario == "admin":
            print("Senha incorreta")
        else:
            print("Usuário inválido")

        tentativas += 1

    print("Bloqueado")
verificar_acesso()