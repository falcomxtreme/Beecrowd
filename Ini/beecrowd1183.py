O = input("")
M = []
Resultado = 0.0
Quantidade = 0

for i in range(12):
    Linha = []
    M.append(Linha)
    for j in range(12):
        Linha.append(float(input("")))

for i in range(12):
    C = i+1
    while C < 12:
        Resultado = Resultado + M[i][C]
        C = C + 1
        Quantidade = Quantidade + 1

if O == "S":
    print(f"{Resultado:.1f}")

elif O == "M":
    Resultado = Resultado/Quantidade
    print(f"{Resultado:.1f}")