# print('Digite o primeiro numero:')
# num1 = int(input())

# print('Digite o segundo numero:')
# num2 = int(input())

# print('Digite o terceiro numero:')
# num3 = int(input())

# print('Digite o quarto numero:')
# num4 = int(input())

# print('Digite o quinto numero:')
# num5 = int(input())
soma = 0
tam = int(input('Digite quantos numeros deseja somar: '))
for i in range(tam):
    print(f'Digite o {i+1}º numero:')
    numero = int(input())
    soma = soma+numero

media = soma/tam

print(f'Soma: {soma}')
print(f'Media: {media}')