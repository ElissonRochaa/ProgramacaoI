#Encontrar o maior numero de 5 digitados

maior = 0
for i in range(5):
    numero = int(input(f'Digite o {i+1}º numero:'))
    if i == 0:
        maior = numero
    elif numero>maior:
        #print("entrou aquiiii")
        maior = numero
    #print(f'print temporario: maior por enquanto: {maior}')

print(f'Maior numero digitado: {maior}')