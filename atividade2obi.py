N = int(input("Digite o número inicial de pessoas infectadas:"))
R = int(input("Digite o fator reprodutivo:"))
P = int(input("Digite o total desejado de pessoas infectadas:"))

infectadosDias = N
total = N
dias = 0

while total < P: 
    novosInfectados = infectadosDias = N 
    total += novosInfectados 
    infectadosDias = novosInfectados
    dias += 1

print(dias)      