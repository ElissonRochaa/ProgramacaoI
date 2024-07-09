def funcao_exemplo():
    resultado = 10
    print(resultado)
    return resultado

def main():
    resultado = 20
    print(resultado)
    resultado = funcao_exemplo()
    print(resultado)


main()