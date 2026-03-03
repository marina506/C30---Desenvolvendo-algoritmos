senha_correta = 123456
senha = int(input("Digite a senha: "))
nome = (input("Digite seu nome:"))

if senha == senha_correta:
    print("Olá, SEUNOME. Seja bem-vindo ao nosso banco!")
else:
    print("Senha incorreta! Você ainda tem 2 tentativas.")
    
    senha = int(input("Digite a senha: "))
    
    if senha == senha_correta:
        print("Olá. Seja bem-vindo ao nosso banco!")
    else:
        print("Senha incorreta! Você ainda tem 1 tentativa.")
        
        senha = int(input("Digite a senha: "))
        
        if senha == senha_correta:
            print("Olá. Seja bem-vindo ao nosso banco!")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")