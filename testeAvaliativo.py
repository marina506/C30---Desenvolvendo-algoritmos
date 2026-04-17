# Questão 1

print("Hello Word!")

# Questão 2

print("Eleição escolar")
idade = int(input("Digite sua idade:"))

if idade  >= 16:
    print("Pode votar!")

else:
    print("Ainda não pode votar!")    

# Questão 3

# Questão 4

print("Cálculo IMC")

try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    if peso <= 0 or altura <= 0:
        print("O peso e a altura devem ser maiores que zero.")
    else:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("Abaixo do peso")
        elif 18.5 <= imc <= 24.9:
            print("Peso normal")
        else:
            print("Sobrepeso")

except ValueError:
    print(" Digite apenas números válidos.")

# Questão 5

print("Lista amigos - festa")

nomes = []

while True:
    nome = input("Digite um nome (ou 'fim' para parar): ")

    if nome == "fim":
        break
    else:
        nomes.append(nome)

quantidade = len(nomes)

if quantidade % 2 == 0:
    print("A quantidade é par")
else:
    print("A quantidade é ímpar")

# Questão 6

print("Média temperaturas da semana")

temperaturas = []

for i in range(7):
    temp = float(input("Digite a temperatura: "))
    temperaturas.append(temp)

soma = 0

for t in temperaturas:
    soma += t

media = soma / 7

print("Média da semana:", media)

# Questão 7

print("Número de vendas")

vendas = [13, 6, 7, 10, 9, 13]

soma = 0

for v in vendas:
    if v % 2 == 0:
        soma += v

print("Soma dos valores pares:", soma)

# Questão 8

print("LOja online")

valorProduto = float(input("Digite o valor do produto para verificar o desconto:"))
 
if valorProduto > 500:
    desconto = valorProduto * 0.20
    valorFinal = valorProduto - desconto
    print("Foi aplicado o desconto de 20%, assim, o valor final ficou:", valorFinal)

elif valorProduto > 200 and valorProduto < 500:
    desconto10 = valorProduto * 0.10
    valorFinal10 = valorProduto - desconto10
    print("Foi aplicado o desconto de 10%, assim, o valor final ficou:", valorFinal10)

else:
    print("Nenhum desconto apliacado, valor permance:", valorProduto)

# Questão 9

print("Média alunos")    

notaAlunos = [8, 9, 6, 4, 5, 10]

acimaMedia = 0

for n in notaAlunos:
    if n > 7:
        acimaMedia += 1

print("Quantidade acima de 7:", acimaMedia)

# Questão 12

print("Menu")

while True:
    print("\nCalculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 5:
            print("Saindo")
            break

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", n1 + n2)

        elif opcao == 2:
            print("Resultado:", n1 - n2)

        elif opcao == 3:
            print("Resultado:", n1 * n2)

        elif opcao == 4:
            if n2 == 0:
                print("Erro: divisão por zero")
            else:
                print("Resultado:", n1 / n2)

        else:
            print("Opção inválida")

    except ValueError:
        print(" Digite apenas números válidos")

    


