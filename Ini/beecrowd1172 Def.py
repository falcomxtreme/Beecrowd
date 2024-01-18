X = []

def substituicao(n):
    for i in range(10):
        val = n[i]
        if val <= 0:
            n[i] = 1
        print(f"X[{i}] = {n[i]}")

for i in range(10):
    x = int(input(""))
    X.append(x)

substituicao(X)