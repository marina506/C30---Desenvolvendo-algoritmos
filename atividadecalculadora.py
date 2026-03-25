def calculadora():
    print("CALCULADORA")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        print("Resultado:", num1 + num2)

    elif opcao == "2":
        print("Resultado:", num1 - num2)

    elif opcao == "3":
        print("Resultado:", num1 * num2)

    elif opcao == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Não pode dividir por zero!")

    elif opcao == "0":
        print("Saindo")

    else:
        print("Opção inválida!")

calculadora()