# Sistema de Magia com Combinação 

def tipo_magia(fogo, agua):
    if fogo and agua:
        return "Vapor"
    elif fogo:
        return "Fogo"
    elif agua:
        return "Água"
    else:
        return "Sem magia"

fogo = input("Tem fogo? (S/N): ") == "S"
agua = input("Tem água? (S/S): ") == "S"

print("Tipo da sua magia:", tipo_magia(fogo, agua))