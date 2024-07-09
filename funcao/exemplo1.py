def somar(a, b):
    """
    Documentacao aqui sobre a função de soma...
    """
    soma = a+b
    return soma

def dividir(a, b):
    return a/b

def operadores(a, b):
    soma = somar(a, b)
    divisao = dividir(a, b)
    return soma, divisao

def cumprimentar(nome="World"):
    print("Hello,", nome)

def main():
    # nome = input("Digite um nome: ")
    # cumprimentar(nome)
    # cumprimentar()

    # print(dividir(2, 5))
    # print(dividir(b=2, a=5))

    valor_soma, valor_divisao = operadores(2, 5)
    print(valor_soma, valor_divisao)

    # numero1 = int(input('Digite o primeiro numero: '))
    # numero2 = int(input('Digite o segundo numero: '))
    # resultado = somar(numero1, numero2)
    # print(resultado)

if __name__ == "__main__":
    main()