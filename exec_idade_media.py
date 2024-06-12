
print("Digite a quantidade de pessoas irão fornecer a idade:")
quantidade = int(input())

somatorio_idade = 0
for i in range(quantidade):
    print(f"Digite a {i+1}ª idade")
    idade = int(input())

    #somatorio_idade = somatorio_idade + idade
    somatorio_idade += idade

media_idade = somatorio_idade // quantidade

if media_idade <= 25:
    print(f"A media da turma foi {media_idade}, entao a turma é jovem")
elif media_idade <= 60:
    print(f"A media da turma foi {media_idade}, entao a turma é adulta")
else:
    print(f"A media da turma foi {media_idade}, entao a turma é idosa")