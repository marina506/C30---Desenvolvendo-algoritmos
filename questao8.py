compra = float(input("Valor da compra: "))

if compra < 100:
    desconto = 0
elif compra < 500:
    desconto = compra * 0.05
elif compra < 1000:
    desconto = compra * 0.10
else:
    desconto = compra * 0.15

valor_final = compra - desconto

print("Valor da compra:", compra)
print("Desconto:", desconto)
print("Total a pagar:", valor_final)