#Verificar se o numero é par ou impar

print('Digite o numero desejado: ')
numero = int(input())

resto = numero % 2

if resto == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")