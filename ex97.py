def calcular_determinante():

    print("Programa para calcular a determinante da matriz")
    print()

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))
d = int(input("Informe o valor de D: "))

det = (a * d) - (b * c)

print("O determinante da matriz é:",det)