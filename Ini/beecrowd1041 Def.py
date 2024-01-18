x, y = map(float, input("").split(" "))

def CoordDeUmPonto(x, y):

    if x != 0 and y != 0:
        if x > 0 and y > 0:
            ponto = "Q1"
        elif x < 0 and y > 0:
            ponto = "Q2"
        elif x < 0 and y < 0:
            ponto = "Q3"
        else:
            ponto = "Q4"       
    else:
        if x == 0 and y == 0:
            ponto = "Origem"
        elif x == 0:
            ponto = "Eixo Y"
        else:
            ponto = "Eixo X"
    return ponto
    
Coord = CoordDeUmPonto(x, y)
print(Coord)