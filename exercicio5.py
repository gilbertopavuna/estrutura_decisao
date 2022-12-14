nota1 = float(input('Entre com sua primeira nota: '))
nota2 = float(input('Entre com sua segunda nota: '))
media = (nota1+nota2)/2
if media >= 7:
    print('Aprovado')
elif media == 10:
    print('Aprovado com distinção')
else:
    print('Reprovado')
