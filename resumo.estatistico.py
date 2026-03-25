def calculadora():
    print("Resumo Estatístico")

    num1 = float(input("Digite a primeira nota: "))
    num2 = float(input("Digite a segunda nota: "))
    num3 = float(input("Digite a terceira nota: "))

    soma = num1 + num2 + num3
    media = soma / 3
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    print("Soma:", soma)
    print("Média:", media)
    print("Maior nota:", maior)
    print("Menor nota:", menor)

calculadora()