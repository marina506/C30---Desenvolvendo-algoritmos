import random

#Manipulção de listas em python

numeros = [10,20,30,20,40,20,50]

#1
print("Quantos elementos exixtem na lista:", len(numeros))

#2
print("Quantas vezes 20 aparece na lista:", numeros.count(20))

#3
print("Posição de 30 na lsita:", numeros.index(30))
print("100 está na lista?", 100 in numeros)


#parte 2 atividade - ordem
#1
numeros = [91,34,67,15,82]
print(numeros)

#2
numeros.sort()
print("Após sort():", numeros)

#3
numeros.sort(reverse=True)
print("Após sort():", numeros)

#parte 3
numeros = [80, 7, 10, 9, 19] 
random.shuffle(numeros)
print("Embaralhar:", numeros)

#parte 4
lista = [13,6,7,10,8,5]
print(lista)

lista.sort()
print("Após sort():", lista)

lista.sort(reverse=True)
print("Após sort():", lista)

random.shuffle(lista)
print("Embaralhar:", lista)




