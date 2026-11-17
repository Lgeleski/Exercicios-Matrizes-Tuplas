matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

identidade = True

for i in range(3):
    for j in range(3):
        if i == j and matriz[i][j] != 1:
            identidade = False
        elif i != j and matriz[i][j] != 0:
            identidade = False

if identidade:
    print("A matriz é identidade!")
else:
    print("A matriz não é identidade!")
