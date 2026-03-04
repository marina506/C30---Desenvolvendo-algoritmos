compras = ["Arroz", "Feijão", "Carne", "Frango", "Farofa"]

print(compras[0])
print(compras[1])
print(compras[2])
print(compras[3])

n = int(input("Quantos itens você quer adicionar? "))

for i in range(n):
    item = input(f"Digite o item {i+1}: ")
    compras.append(item)

print("Sua lista final:", compras)