O = input("")
M = []
Resultado = 0
Quantidade = 0
L = 0
C = 0

for i in range(12):
    Linha = []
    M.append(Linha)
    for j in range(12):
        Linha.append(float(input("")))
    L = L + 1

C = L - 1
L = L/2 - 1

for i in range(12):
    for j in range(12):
        if j > C:
            Resultado = Resultado + M[i][j]
            Quantidade = Quantidade + 1
    if i < L:
        C = C - 1
    elif i > L:
        C = C + 1

if O == "S":
    print(f"{Resultado:.1f}")
elif O == "M":
    Resultado = Resultado/Quantidade
    print(f"{Resultado:.1f}")    