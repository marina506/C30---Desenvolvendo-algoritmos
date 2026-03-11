aluno = {}

aluno["nome"] = input("Qual o seu nome? ")
aluno["nota"] = float(input("Digite a sua nota: "))
aluno["nota2"] = float(input("Digite a sua segunda nota: "))

media = (aluno["nota"] + aluno["nota2"]) / 2

aluno["media"] = media

print("\nRelatório")

print("Nome:", aluno["nome"])
print("Primeira nota:", aluno["nota"])
print("Segunda nota:", aluno["nota2"])
print("Média:", aluno["media"])

if media >= 7:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado")