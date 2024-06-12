import random

numero_aleatorio = random.randint(1, 100)

acertou = False
while acertou == False:
    print("Digite um numero: ")
    numero = int(input())

    if numero == numero_aleatorio:
        print("Voce Acertou!")
        acertou = True
    elif numero > numero_aleatorio:
        print("O numero aleatorio é menor")
    else:
        print("O numero aleatorio é maior")
