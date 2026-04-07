import random
numero = random.randint(1,100)
tentativas = int(input("Digite algum número e adivinhe-o de 1 a 100:"))

while palpite != numero:
    tentativas += 1
    
    if palpite > numero:
        print("maior")
    elif palpite < numero:
        print("menor")
    
    palpite = int(input("Tente novamente: "))