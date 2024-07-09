#Pegue tres numeros do usuario e digite o menor numero entre eles

print('Digite o primeiro numero:')
x = int(input())

print('Digite o segundo numero:')
y = int(input())

print('Digite o terceiro numero:')
z = int(input())

###Condições
# if x < y:
#     if x < z:
#         print(f'{x} é o menor')
#     else:
#         print(f'{z} é o menor')
# else:
#     if y < z:
#         print(f'{y} é o menor')
#     else:
#         print(f'{z} é o menor')

if x < y and x < z:
    print(f'{x} é o menor')
elif y < x and y < z:
    print(f'{y} é o menor')
else:
    print(f'{z} é o menor')