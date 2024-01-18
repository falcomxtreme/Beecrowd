T = int(input(""))
N = []

def Preenchimento(y, z):
    x = 0
    for i in range(1000):
        if x == y-1:
            z.append(x)
            x = 0
        else:
            z.append(x)
            x += 1
    for i in range(1000):
        print(f"N[{i}] = {z[i]}")

Preenchimento(T, N)