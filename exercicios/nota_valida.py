continuar_pedindo = True

# while continuar_pedindo:
#     print("Digite a nota a primeira prova: ")
#     nota1 = float(input())

#     if nota1 >= 0 and nota1 <= 10:
#         print("Nota Valida")
#         continuar_pedindo = False
#     else:
#         print("Nota invalida")


while True:
    print("Digite a nota a primeira prova: ")
    nota1 = float(input())

    if nota1 >= 0 and nota1 <= 10:
        print("Nota Valida")
        break
    else:
        print("Nota invalida")