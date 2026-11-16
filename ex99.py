
pessoas = []

for i in range(10):
    print(f"Pessoa {i + 1}")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = (nome, idade)
    pessoas.append(pessoa)

menores = []
maiores = []

for pessoa in pessoas:
    if pessoa[1] < 18:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

print("PESSOAS COM MENOS DE 18 ANOS ")
for pessoa in menores:
    print(f"Nome: {pessoa[0]} - Idade: {pessoa[1]} anos")

print("PESSOAS COM 18 ANOS OU MAIS")
for pessoa in maiores:
    print(f"Nome: {pessoa[0]} - Idade: {pessoa[1]} anos")
