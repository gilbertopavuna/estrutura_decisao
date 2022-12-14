numero_1 = float(input('Entre com o primeiro número: '))
numero_2 = float(input('Entre com o segundo número: '))
numero_3 = float(input('Entre com o terceiro número: '))
if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'O maior número é o {numero_1}')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'O maior número é o {numero_2}')
else:
    print(f'O maior número é o {numero_3}')
