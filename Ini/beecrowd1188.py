O = input("")
M = []
Quantidade = 0
Resultado = 0
C1 = 0
L = 0

for i in range(12):
    Linha = []
    M.append(Linha)
    for j in range(12):
        Linha.append(float(input("")))
    C1 = C1+1
    L = L+1

C1 = C1/2
C2 = C1 - 1
L = L/2

for i in range(12):
    for j in range(12):
        if i > L and j >= C2 and j <= C1:
            Resultado = Resultado + M[i][j]
            Quantidade = Quantidade + 1
    if i > L:
      C1 = C1 + 1
      C2 = C2 - 1

if O == "S":
    print(f"{Resultado:.1f}")

elif O == "M":
    Resultado = Resultado/Quantidade
    print(f"{Resultado:.1f}")