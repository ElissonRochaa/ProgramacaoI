import json

def cadastrar_cliente():
    ### Cada cliente
    # Nome
    # email
    # cpf
    dict_cliente = {}
    print("Iniciando o cadastro do cliente...")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    cpf = input("Digite o cpf: ")
    dict_cliente["Nome"] = nome
    dict_cliente["Email"] = email
    dict_cliente['CPF'] = cpf
    return dict_cliente
    #clientes.append(dict_cliente)
    #return clientes


def menu():
    print("Menu:")
    print("1-Cadastrar Cliente")
    print("2-Mostrar Clientes")
    print("3-Encerrar o programa")
    print("4-Apagar ultimo cliente")

def regra_cpf_unico(lista_clientes, cliente):
    for c in lista_clientes:
        if c['CPF'] == cliente['CPF']:
            return True
    
    return False

def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print("-----------------------")
        print("Nome: ", cliente['Nome'])
        print("Email: ", cliente['Email'])
        print()

def salvar_clientes(lista_clientes):
    arquivo = 'arquivo_clientes.json'
    with open(arquivo, 'w') as arquivo_aberto:
        json.dump(lista_clientes, arquivo_aberto, indent=4)

def ler_clientes():
    lista_clientes = []
    try:
        arquivo = 'arquivo_clientes.json'
        with open(arquivo, 'r') as file:
            lista_clientes = json.load(file)
    except FileNotFoundError:
        print("Arquivo Clientes ainda não existe...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        return lista_clientes


def main():
    lista_clientes = ler_clientes()
    while True:
        menu()
        opcao = int(input("Digite a sua escolha: "))
        if opcao == 1:
            cliente = cadastrar_cliente()
            if regra_cpf_unico(lista_clientes, cliente) == False:
                lista_clientes.append(cliente)
            else:
                print("Usuario já existente")
        elif opcao == 2:
            mostrar_clientes(lista_clientes)
        elif opcao == 3:
            print("Encerrando o programa...")
            print("salvando as informações...")
            salvar_clientes(lista_clientes)
            break
        elif opcao == 4:
            lista_clientes.pop(-1)
        else:
            print("Opcao invalida")


main()