#  Missão Espacial – Lógica Composta 

def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    if clima != "bom":
        return "Clima desfavorável"
    if not sistema_ok:
        return "Falha no sistema do foguete"
    return "Lançamento autorizado"

combustivel = int(input("Digite a quantidade de combustível: "))
clima = input("Como está o clima? (bom/ruim): ").lower()
sistema_input = input("Sistema operacional OK? (s/n): ").lower()
sistema_ok = sistema_input == "s"

resultado = lancar_foguete(combustivel, clima, sistema_ok)
print("Resultado:", resultado)