IdadeDias = int(input(""))

Anos = IdadeDias/365
Resto = IdadeDias%365
Meses = Resto/30
Resto = Resto%30
Dias = Resto/1

print(f"{int(Anos)} ano(s)")
print(f"{int(Meses)} mes(es)")
print(f"{int(Dias)} dia(s)")