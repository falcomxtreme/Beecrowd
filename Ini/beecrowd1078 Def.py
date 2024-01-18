N = int(input(""))

def tabuada(n):
    x = 1
    for i in range(10):
        print(f"{x} x {n} = {x*n}") 
        x += 1

tabuada(N)