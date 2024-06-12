print("Tabuada de multiplicação - UPE GARANHUNS")
print()
print('Digite um número inteiro:')
valor = int(input())

print('Digite ate que numero vai a tabuada:')
tab = int(input())
tab = tab + 1

print("O valor digitado pelo usuario foi: ", valor)
print()

for i in range(tab):
    print(f'{valor} x {i} = {valor*i}')
# i = 0
# while i < 11:
#     print(f'{valor} x {i} = {valor*i}')
#     i = i + 1