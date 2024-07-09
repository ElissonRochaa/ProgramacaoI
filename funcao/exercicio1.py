def calcular_media(primeira_nota, segunda_nota, terceira_nota):
    media = (primeira_nota+segunda_nota+terceira_nota)/3
    return media

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)
    print(f"A media final foi de {media}")

if __name__ == "__main__":
    main()

