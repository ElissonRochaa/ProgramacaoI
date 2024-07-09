#Produto
nome = 'Feijão'
variavel_teste = nome
numero = 10
real = 3.14
print(variavel_teste)
input()
numero = '03'
codigo = 10
preco = 4.99
#quantidade = 2
ativo = True

print("Digite a quantidade que voce queira de", nome)
quantidade = int(input())

#quantidade = input("Digite a quantidade que voce queira de " + nome)
preco_final = quantidade * preco

print("Você comprou", quantidade, nome, "com o preço unitário de R$",
       preco, "que resultou no valor total de R$", preco_final)