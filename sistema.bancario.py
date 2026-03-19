# Sistema bancário com taxa


def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        taxa = saque * 0.02
        saque = saque + taxa
    
    saldo = saldo - saque
    return saldo

saldo = float(input("Digite seu saldo: "))
saque = float(input("Digite o valor do saque: "))

resultado = saldo_final(saldo, saque)

print("Seu resultado:", resultado)