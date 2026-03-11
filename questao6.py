idade = int(input("Digite sua idade para verificar a categoria: "))
print("Sua idade é:", idade, "Agora vamos verificar sua categoria")

if idade < 12:
    cat = "Infantil"
elif idade < 18:
    cat = "Juvenil"
elif idade < 60:
    cat = "Adulto"
else:
    cat = "Sênior"

print("Categoria:", cat)
print("Bem-vindo à competição!")