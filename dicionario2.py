contato = {
"@camila": "Camila",
"@paola": "Paola",
"@sheron": "Sheron",
"@bruna": "Bruna",
"@joao": "João",
}

#obter chaves
print("Chaves: ")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n valores:")   
for nome in contato.values():
    print(nome)

#obter pares (chave-valor)
print("\n Pares:")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")    

contato = {
"@camila": 1.66,
"@paola": 1.50,
"@sheron": 1.80,
"@bruna": 1.60,
"@joao": 1.70,
}

#ordenar por chave
print("Ordenar por chave:")
for insta in sorted(contato):
   print(f"{insta} --> {contato[insta]:.2f}m")    

#ordenr por valor
from operator import itemgetter
print("\n Ordenando por valor(altura)")   
for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")

    

   
