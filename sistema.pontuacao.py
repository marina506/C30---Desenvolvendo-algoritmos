# Sistema de Pontuação com Bônus Oculto 

def pontuacao_total(pontos, tempo):
    
    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20

    # resultado final
    if pontos > 200:
        return "Recorde"
    else:
        return pontos

pontos = int(input("Digite seus pontos: "))
tempo = int(input("Digite o tempo: "))

resultado = pontuacao_total(pontos, tempo)
print("Seu resultado:", resultado)