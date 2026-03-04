#listas

nome1 = "Ana"
nome2 = "Bruno"
nome3 = "Carlos"

nomes = ["Arthur", "João", "Maria"]
print(nomes)

dados = ["Gabriel", 0, 1.60, True]

print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

alunos = ["Adriano", "Bárabara", "Camila"]

print("Primeiro", alunos[0])
print("Primeiro", alunos[1])
print("Primeiro", len(alunos))
print("Primeiro", alunos[2])
print("Primeiro", [len(alunos) - 1])

nomes = ["Ana", "Bruno", "Caio"]
print("Original", nomes)
nomes.apprnd("Daniel")
print("Atualizado:", nomes)