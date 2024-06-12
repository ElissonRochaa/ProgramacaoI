
lista_idade = []

for j in range(2):
    n = int(input('Digite a quantidade de idades que vc deseja digitar: '))
    lista_temporaria = []
    for i in range(n):
        idade = int(input(f'Digite a {i+1}ª idade:'))
        lista_temporaria.append(idade)
    lista_idade.append(lista_temporaria)

print(lista_idade)
print("Elementos com o for")
for idade in lista_idade:
    print(idade)

print("Elementos com while")
contador = 0
while contador < len(lista_idade):
    print(lista_idade[contador])
    contador = contador + 1
    #contador += 1

