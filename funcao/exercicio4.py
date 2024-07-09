### VAMOS FAZER FATORIAL <3
### 5! -> 5*4*3*2*1 = 120
### 4! -> 4*3*2*1 = 24

# def fatorial(n):
#     resultado = 1
#     for i in range(n,0,-1):
#         print(i)
#         resultado = resultado * i
#     return resultado

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

def main():
    numero = int(input("Digite o numero para o fatorial: "))
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")

main()