vendaDoces = int(input("Digite a quantidade de doces vendidos:"))
vendaBolos = int(input("Digite a quantidade de bolos vendidos:"))
vendaPaes = int(input("Digite a quantidade de pães vendidos:"))

total = (vendaDoces * 2) + (vendaBolos * 3) + (vendaPaes * 1)

if total >= 150:
    print("B")

elif total >= 120:
    print("D")

elif total >= 100:
    print("P")        

else:
    print("N")    