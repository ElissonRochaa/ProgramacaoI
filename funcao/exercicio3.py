
def criar_arvore_numeros(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

def main():
    numero = int(input("Digite um numero: "))
    criar_arvore_numeros(numero)

main()