def caixaMercado():

    try:
        preco1 = float(input("Digite o primeiro preço:"))
        preco2 = float(input("Digite o segundo preço:"))

        total = preco1 + preco2
        print("Resultado:", total)

    except ValueError:
        print("Erro capturado! Digite apenas números")

caixaMercado()