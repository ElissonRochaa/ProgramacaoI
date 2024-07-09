#Inicializar as listas de professores e alunos vazias
lista_professores = []
lista_alunos = []

#Mostrar um cabeçalho
print("Bem-vindo a lista de Professores e Alunos")

#Mostrar o menu de opções
# Menu:
# 1- Cadastrar um novo Professor
# 2- Cadastrar um novo Aluno
# 3- Ver Professores cadastrados
# 4- Ver Alunos cadastrados
# 5- Excluir o último professor da lista
# 6- Excluir o último aluno da lista
# 7- Encerrar o programa
opcao = 0
while opcao !=7:
    print("Menu:")
    print("1- Cadastrar um novo Professor")
    print("2- Cadastrar um novo Aluno")
    print("3- Ver Professores cadastrados")
    print("4- Ver Alunos cadastrados")
    print("5- Excluir o último professor da lista")
    print("6- Excluir o último aluno da lista")
    print("7- Encerrar o programa")

    #Pegar a opção que o usuario deseja
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        #print("Realizar cadastro de professores...")
        novo_professor = input("Digite o nome do professor a ser cadastrado: (digite 0 para voltar para o menu)")
        if novo_professor == '0':
            print("Voltando para o Menu...")
        elif len(novo_professor) < 3:
            print("Professor não cadastrado, o nome deve conter mais de 3 caracteres")
        else:
            lista_professores.append(novo_professor)
            print("Professor cadastrado com sucesso")

    elif opcao == 2:
        #print("Realizar cadastro de Alunos...")
        novo_aluno = input("Digite o nome do aluno a ser cadastrado: (digite 0 para voltar para o menu)")
        if novo_aluno == '0':
            print("Voltando para o Menu...")
        elif len(novo_aluno) < 3:
            print("Aluno não cadastrado, o nome deve conter mais de 3 caracteres")
        else:
            lista_alunos.append(novo_aluno)
            print("Aluno cadastrado com sucesso")
    elif opcao == 3:
        print("Exibir os alunoes cadastrados...")
    elif opcao == 4:
        print("Exibir os alunos cadastrados...")
    elif opcao == 5:
        print("Excluir o ultimo professor cadastrado...")
    elif opcao == 6:
        print("Excluir o ultimo aluno cadastrado...")
    elif opcao == 7:
        print("Sair do sistema...")
    else:
        print("opção invalida...")
