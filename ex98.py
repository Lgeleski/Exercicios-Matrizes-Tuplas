A = []
B = []
C = []

print("Digite os valores da primeira matriz:")
for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor [{i+1}][{j+1}]: "))
        linha.append(valor)
    A.append(linha)

print("\nDigite os valores da segunda matriz:")
for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor [{i+1}][{j+1}]: "))
        linha.append(valor)
    B.append(linha)

for i in range(4):
    linha = []
    for j in range(3):
        linha.append(A[i][j] + B[i][j])
    C.append(linha)

print("\nMatriz resultante da soma:")
for i in range(4):
    for j in range(3):
        print(f"{C[i][j]:5}", end="")
    print()
