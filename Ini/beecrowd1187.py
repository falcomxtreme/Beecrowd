O = input("")
M = []
Quantidade = 0
Resultado = 0
C1 = 0
C2 = -1

for i in range(12):
    Linha = []
    M.append(Linha)
    for j in range(12):
        Linha.append(float(input("")))
    C2 = C2 + 1

for i in range(12):
    for j in range(12):
        if j > C1 and j < C2:
            Resultado = Resultado + M[i][j]
            Quantidade = Quantidade + 1
    C1 = C1 + 1
    C2 = C2 - 1

if O == "S":
    print(f"{Resultado:.1f}")

elif O == "M":
    Resultado = Resultado/Quantidade
    print(f"{Resultado:.1f}")