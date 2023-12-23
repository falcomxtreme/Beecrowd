O = input("")
M = []
Quantidade = 0
Resultado = 0
C = 0
L = 0

for i in range(12):
    Linha = []
    M.append(Linha)
    for j in range(12):
        Linha.append(float(input("")))
    C = C + 1
    L = L + 1

C = C/2 - 1
L = L/2 - 1

for i in range(12):
    for j in range(12):
        if j < i and j < C and i <= L:
            Resultado = Resultado + M[i][j]
            Quantidade = Quantidade + 1
        elif i > L and j < C:
            Resultado = Resultado + M[i][j]
            Quantidade = Quantidade + 1
    if i > L:
        C = C - 1

if O == "S":
    print(f"{Resultado:.1f}")

elif O == "M":
    Resultado = Resultado/Quantidade
    print(f"{Resultado:.1f}")