produto_1 = input('Entre com o primeiro produto: ')
preco_1 = float(input('Entre com o preço: '))
produto_2 = input('Entre com o segundo produto: ')
preco_2 = float(input('Entre com o preço: '))
produto_3 = input('Entre com o terceiro produto: ')
preco_3 = float(input('Entre com o preço: '))

if preco_1 < preco_2 and preco_1 < preco_3:
    print(f'Compre o(a) {produto_1} pois está mais barato.')
elif preco_2 < preco_1 and preco_2 < preco_3:
    print(f'Compre o(a) {produto_2} pois está mais barato.')
else:
    print(f'Compre o(a) {produto_3} pois está mais barato.')