
# for i in range(5):
#     print("Seja bem-vindo ao laço de repetição", i)

# i = 0
# while i < 5:
#     print("Seja bem-vindo ao laço de repetição com while", i)
#     i = i + 1

tecla = ''

while tecla != 's':
    print("Bem-vindo ao programa")
    print("Menu:")
    print("a-Agradecer")
    print("p-pedir ajuda")
    print("s-sair")
    tecla = input()

    if tecla == 'a':
        print("Obrigado")
    elif tecla == 'p':
        print("Socorrooo...")
    elif tecla == 's':
        print("saindo do programa")