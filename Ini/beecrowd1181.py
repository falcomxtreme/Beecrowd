L = int(input(""))
T = input("")
M = []
resultado = 0.0

for i in range(12):
    Linha = []
    M.append(Linha)
    
    for j in range(12):
      Linha.append(float(input("")))

    
if T=="S":
    for i in range(12):
     resultado = resultado + M[L][i]
    print(f"{resultado:.1f}")
 
elif T=="M":   
    for i in range(12):
     resultado = resultado + M[L][i]
    resultado = resultado/12
    print(f"{resultado:.1f}")