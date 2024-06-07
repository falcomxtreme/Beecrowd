N = int(input(""))

def num_primo(num):
    div = 0

    for i in range(1, num+1):
        if num%i == 0:
            div += 1

        if div == 3:
            break
    
    if div == 2:
        return print(f'{num} eh primo')
    else:
        return print(f'{num} nao eh primo')
    
for i in range(N):
    X = int(input(""))
    num_primo(X)
