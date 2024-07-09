
def main():

    lista_clientes = []
    for i in range(2):
        dados_cliente = {}
        nome = input("Digite seu nome: ")
        dados_cliente['Nome'] = nome
        idade = int(input("Digite sua idade: "))
        dados_cliente['Idade'] = idade

        print(dados_cliente)
        lista_clientes.append(dados_cliente)

    print(lista_clientes)

main()