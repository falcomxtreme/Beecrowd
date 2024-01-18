Salario = float(input(""))

def Renda(x):
    if x <= 2000:
        imposto = "Isento"
    elif x <= 3000:
        imposto = f"R$ {(x - 2000) * 0.08:.2f}"
    elif x <= 4500:
        imposto = f"R$ {(1000 * 0.08) + ((x - 3000) * 0.18):.2f}"
    else:
        imposto = f"R$ {(1000 * 0.08) + (1500 * 0.18) + ((x-4500) * 0.28):.2f}"
    return imposto

imposto = Renda(Salario)
print(imposto)