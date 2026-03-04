animal = ["Cachorro", "Gato"]
print("Lista inicial: ", animal)

animal.append("Pato") # Adiciona no fim da lista
print("Lista atualizada: ", animal)

animal.insert(1, "Coelho") # Add em uma posição esoecífica
print("Lista atualizada: ", animal)

animal.extend(["Macaco", "Leão"]) # Add mais de um dado 
print("Lista atualizada: ", animal) 

animal.remove("Leão")
print(animal)

removido = animal.pop()
print(f"Removido: {removido}")
print("Após pop()", animal) 

removido2 = animal.pop(1)
print(f"Removido do índice 1{removido2}")
print("Após pop(1):", animal)
