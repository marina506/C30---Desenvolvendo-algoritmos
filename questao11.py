soma = 0
print("A soma de todos os números pares de 1 a 100:")
for numero in range(1, 101):
    if numero % 2 == 0:
        soma += numero

print(soma)
