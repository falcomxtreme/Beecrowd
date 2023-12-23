O = input("")
M = []
Quantidade = 0
L = -1
Resultado = 0.0

for i in range(12):
    Linha = []
    M.append(Linha)
    for j in range(12):
        Linha.append(float(input("")))
    L = L + 1

for i in range(12):
    for j in range(12):
        if j < L:
            Resultado = Resultado + M[i][j]
            Quantidade = Quantidade + 1
    L = L - 1

if O == "S":
    print(f"{Resultado:.1f}")

elif O == "M":
    Resultado = Resultado/Quantidade
    print(f"{Resultado:.1f}")