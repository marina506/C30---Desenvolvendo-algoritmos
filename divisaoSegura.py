def divisao(a, b):
    return a / b

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    resultado = divisao(a, b)
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Erro capturado! Não se divide por 0")