preco_original = float(input('Digite o preço original do produto:'))
procentagem_desconto = float (input('Digite o valor do desconto:'))

valor_desconto = preco_original * (procentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f'Preço final após desconto: R$ {preco_final}')
print('Preço final após desconto: R$', preco_final)