N = int(input(""))

#nota(s) de R$ 100,00
NotasDe100 = N//100
Resto = N%100
#nota(s) de R$ 50,00
NotasDe50 = Resto//50
Resto = Resto%50
#nota(s) de R$ 20,00
NotasDe20 = Resto//20
Resto = Resto%20
#nota(s) de R$ 10,00
NotasDe10 = Resto//10
Resto = Resto%10
#nota(s) de R$ 5,00
NotasDe5 = Resto//5
Resto = Resto%5
#nota(s) de R$ 2,00
NotasDe2 = Resto//2
Resto = Resto%2
#nota(s) de R$ 1,00
NotasDe1 = Resto//1
Resto = Resto%1

print(N)
print(F"{NotasDe100} nota(s) de R$ 100,00")
print(F"{NotasDe50} nota(s) de R$ 50,00")
print(F"{NotasDe20} nota(s) de R$ 20,00")
print(F"{NotasDe10} nota(s) de R$ 10,00")
print(F"{NotasDe5} nota(s) de R$ 5,00")
print(F"{NotasDe2} nota(s) de R$ 2,00")
print(F"{NotasDe1} nota(s) de R$ 1,00")