##Primeira Questao
celsius = float(input('Digite a temperatura em Celsius: '))

f = celsius * 1.8 + 32

print(f'A temperatura {celsius}C em Fahrenheit é: {f}')

#Segunda questão
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

print(f'A media das notas {nota1}, {nota2} e {nota3} é {media}')

#Terceira Questao
peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura**2)

print(f'O seu IMC é de {imc}')