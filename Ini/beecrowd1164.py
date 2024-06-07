N = int(input(""))

def num_perfeito(num):
    soma_divisores = 0

    for i in range(1,num):
        if num%i == 0:
            soma_divisores += i

    if soma_divisores == num:
        return print(f'{num} eh perfeito')
    else:
        return print(f'{num} nao eh perfeito')
    
for i in range(N):
    X = int(input(""))
    num_perfeito(X)