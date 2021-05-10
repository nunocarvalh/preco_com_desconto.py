preço = float(input('Digite o preço do produto?'))
desconto = preço - (preço * 10 / 100)
print('O valor do preço R${:.2f}, com desconto de 10% arrendontado R${:.2f}'.format(preço,desconto))


