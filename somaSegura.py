def soma_segura():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        return a + b
    except ValueError:
        print("Entrada inválida, digite somente números")
        return 0

resultado = soma_segura()
print("Resultado:", resultado)