def mediaNotas(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    resultado = mediaNotas(nota1, nota2, nota3)
    print("Resultado:", resultado)

except ValueError:
    print("Erro capturado! Digite apenas números")