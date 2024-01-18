x1, y1 = map(float, input("").split(" "))
x2, y2 = map(float, input("").split(" "))

def DistanciaEntreDoisPontos(x1, y1, x2, y2):
    resultado = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return resultado

distancia = DistanciaEntreDoisPontos(x1, y1, x2, y2)
print(f"{distancia:.4f}")