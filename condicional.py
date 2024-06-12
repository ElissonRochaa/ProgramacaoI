#Segunda questão
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

print(f'A media das notas {nota1}, {nota2} e {nota3} é {media}')

if media == 10:
    print("Nota maxima!!!")

if media >= 7:
    print("Parabéns, você foi aprovado!!")
    print("Parabéns para você que está programando pq entrou no if")
elif media >= 5:
    print("Você está na final")
else:
    print("Eita, não foi dessa vez. Você foi reprovado. Estude mais...")

print("Encerrou o programa")
