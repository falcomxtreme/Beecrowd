Valor = int(input(""))

def idade(x):
    anos = x//365
    resto = x%365

    meses = resto//30
    resto = resto%30

    dias = resto

    return anos, meses, dias

anos, meses, dias = idade(Valor)
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")