# Sistema de Rank com Penalidade

def rank_jogador(pontos, derrotas):
    pontos = pontos - (derrotas * 10)

    if pontos < 0:
        return "Banido"
    elif pontos < 100:
        return "Bronze"
    elif pontos < 300:
        return "Prata"
    elif pontos < 600:
        return "Ouro"
    else:
        return "Diamante"


def saque(saldo, valor):
    taxa = 2
    return saldo - valor - taxa


def deposito(saldo, valor):
    return saldo + valor



saldo = 100
pontos = 200
derrotas = 3

saldo = deposito(saldo, 50)
saldo = saque(saldo, 30)

rank = rank_jogador(pontos, derrotas)

print("Saldo final:", saldo)
print("Rank do jogador:", rank)