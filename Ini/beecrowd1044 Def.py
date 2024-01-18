A, B = map(int, input("").split(" "))

def multiplos(x, y):
    if y%x == 0 or x%y == 0:
        result = "Sao Multiplos"
    else:
        result = "Nao sao Multiplos"
    return result

result = multiplos(A, B)
print(result)