def verificarNumero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

numero = int(input("Digite um número: "))
print(verificarNumero(numero))