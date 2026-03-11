total = 0
contador = 0

while True:
    valor = float(input("Digite o depósito (0 para parar): "))

    if valor == 0:
        break

    total += valor
    contador += 1

print("Total depositado:", total)
print("Quantidade de depósitos:", contador)