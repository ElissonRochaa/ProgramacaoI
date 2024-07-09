
def main():

    # lista = ["Elisson", "Jose", "Maria"]
    # for nome in lista:
    #     print(nome)

    dados_cliente = {
        'Nome': 'Elisson',
        'Idade': 47,
        'Endereco': "Rua Fulano, 10",
        'Telefone': "8198764321"
    }

    for chave, valor in dados_cliente.items():
        print("Chave: ", chave)
        print("Valor: ", valor)

main()